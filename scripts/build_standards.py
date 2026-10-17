#!/usr/bin/env python3
"""Build the companion standards guide, normalized claims, and PDF edition."""
from html import escape
import json
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether,
)

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT/'data/standards.json').read_text())
catalog = json.loads((ROOT/'data/sources.json').read_text())
sources = {s['id']: s for s in catalog['sources'] if 'standards' in s.get('collections', [])}
AS_OF = data['research_as_of']
families = data['families']
preserved = sum(s['download']['status'] == 'archived' for s in sources.values())
new_preserved = sum(s['download']['status'] == 'archived' and int(sid[1:]) >= 57 for sid,s in sources.items())


def write(path, text):
    (ROOT/path).write_text(text, encoding='utf8')


def citations(refs):
    return '; '.join(f"[{r['source_id']}](../sources/README.md#{r['source_id'].lower()}), {r['locator']}" for r in refs)


def source_links(ids):
    return ', '.join(f'[{sid}](../sources/README.md#{sid.lower()})' for sid in ids)


def edition(source):
    fields = [('version','Edition'), ('original_issue_date','Initial issue'),
              ('revision_date','Revision'), ('publication_category','RFC category'),
              ('publication_stream','RFC stream'), ('extent','Extent')]
    return ' | '.join(label+': '+source[key] for key,label in fields if source.get(key))


def build_markdown():
    lines = ['# '+data['title'], '', f'Research snapshot: {AS_OF}', '']
    lines += [p+'\n' for p in data['scope']]
    lines += [f'This guide maps **{len(families)} families**, **{sum(len(f["findings"]) for f in families)} claims** and **{len(data["milestones"])} dated milestones** to {len(sources)} source records. {preserved} copies are preserved, including {new_preserved} newly added documents and snapshots. Three KISA pages remain acquisition gaps.', '',
              '[PDF edition](../reports/companion-standards.pdf) · [Source catalogue](../sources/README.md) · [Structured research](../data/standards.json) · [Normalized claims](../data/standards-claims.json)', '',
              '## Read the layers', '', '| Layer | Question | Examples | Evidence |', '|---|---|---|---|']
    for layer in data['layers']:
        lines += [f"| {layer['name']} | {layer['question']} | {layer['examples']} | {source_links(layer['source_ids'])} |"]
    lines += ['', 'A recommendation list can name a primitive and a mode while leaving the protocol unspecified. A product certificate requires its own version, scope and approval record. An interface can reveal block sizes or encodings even when an algorithm’s internal construction remains unpublished.', '',
              '## Reading map', '', '| Family | Companion records | What the records resolve |', '|---|---|---|']
    for family in families:
        lines += [f"| [{family['name']}](#{family['id']}) | {source_links(family['source_ids'])} | {family['reading_order']} |"]
    claims = []
    for family in families:
        lines += ['', f'<a id="{family["id"]}"></a>', '', '## '+family['name'], '',
                  'Existing profiles: '+', '.join(f'[{p["name"]}](../{p["path"]})' for p in family['profiles'])+'.', '',
                  family['reading_order'], '', '**Scope limit:** '+family['boundary'], '', '### Documented statements', '']
        for finding in family['findings']:
            claims.append({'id':finding['claim_id'], 'collection':'standards', 'family':family['id'], **finding})
            if finding['kind'] == 'documented':
                lines += [f"- **{finding['claim_id']}** — {finding['text']} ({citations(finding['source_refs'])})"]
        lines += ['', '### Inference', '']
        for finding in family['findings']:
            if finding['kind'] == 'inference':
                lines += [f"- **{finding['claim_id']} · {finding['confidence']}** — {finding['text']} Basis: {', '.join(finding['depends_on'])}.",
                          '  Assumption: '+finding['assumption']]
    lines += ['', '## Publication and effective dates', '',
              'These events distinguish releases, revisions, list selections and publication categories. None is automatically an invention date or first classified approval.', '',
              '| Date | Subject | Event type | Interpretation | Evidence |', '|---|---|---|---|---|']
    for event in data['milestones']:
        lines += [f"| {event['date']} | {event['subject']} | {event['date_kind']} | {event['interpretation']} | {source_links([event['source_id']])}, {event['locator']} |"]
    lines += ['', '## Preservation and coverage limits', '']
    for limitation in data['limitations']:
        lines += ['### '+limitation['title'], '', limitation['text']+(f" ({source_links(limitation['source_ids'])})" if limitation['source_ids'] else ''), '']
    lines += ['## Source catalogue', '', 'The following records are the editions used for this companion collection. The global catalogue also covers the earlier historical collections. Successful retrieval, completeness of a document, publication status and implementation approval remain separate attributes.', '']
    for source in sources.values():
        d = source['download']
        lines += ['### '+source['id']+' — '+source['title'], '',
                  f"Publisher: {source['publisher']}  ",
                  f"Document date: {source['document_date'] or 'not printed / not verified'}  ",
                  f"Language: {source.get('language','English')} · Format: {source['format']}  ",
                  f"Provenance: {source['provenance']}", '']
        if edition(source): lines += [edition(source), '']
        if source.get('date_note'): lines += [source['date_note'], '']
        lines += [f"Original URL: <{source['url']}>", '']
        if source.get('acquisition_url'): lines += [f"Acquisition URL: <{source['acquisition_url']}>", '']
        if d['status'] == 'archived':
            lines += [f"[Preserved file](../{source['archive_path']}) · {d['bytes']:,} bytes"+(f" · {d['page_count']} PDF pages" if 'page_count' in d else ''), '',
                      f"Retrieved UTC: {d['retrieved_at_utc']}  ", f"SHA-256: `{d['sha256']}`", '']
        else:
            lines += [f"**Not preserved:** {d['status']}; {d.get('error','no acquired copy')}  ",
                      'Attempt UTC: '+d.get('attempted_at_utc', d.get('retrieved_at_utc','not recorded')), '']
    write('docs/companion-standards.md', '\n'.join(lines).rstrip()+'\n')
    write('data/standards-claims.json', json.dumps({'schema_version':1,'claims':claims},indent=2,ensure_ascii=False)+'\n')


def build_pdf():
    font_root = Path('/usr/share/fonts/truetype/dejavu')
    for name, filename in [('Standards','DejaVuSans.ttf'),('StandardsBold','DejaVuSans-Bold.ttf')]:
        pdfmetrics.registerFont(TTFont(name,str(font_root/filename)))
    pdfmetrics.registerFontFamily('Standards',normal='Standards',bold='StandardsBold',italic='Standards',boldItalic='StandardsBold')
    navy = colors.HexColor('#152D42')
    teal = colors.HexColor('#087F83')
    light = colors.HexColor('#EAF3F4')
    styles = {
        'body':ParagraphStyle('StandardsBody',fontName='Standards',fontSize=9.2,leading=14,spaceAfter=7,textColor=navy),
        'small':ParagraphStyle('StandardsSmall',fontName='Standards',fontSize=7.2,leading=10.5,spaceAfter=6,textColor=colors.HexColor('#516371')),
        'url':ParagraphStyle('StandardsURL',fontName='Standards',fontSize=6.4,leading=8.6,spaceAfter=5,wordWrap='CJK',textColor=navy),
        'title':ParagraphStyle('StandardsTitle',fontName='StandardsBold',fontSize=29,leading=36,spaceAfter=16,textColor=navy),
        'h1':ParagraphStyle('StandardsH1',fontName='StandardsBold',fontSize=18,leading=23,spaceBefore=12,spaceAfter=9,keepWithNext=True,textColor=navy),
        'h2':ParagraphStyle('StandardsH2',fontName='StandardsBold',fontSize=10.5,leading=15,spaceBefore=8,spaceAfter=5,keepWithNext=True,textColor=teal),
        'cell':ParagraphStyle('StandardsCell',fontName='Standards',fontSize=7.1,leading=10.5,spaceAfter=0,textColor=navy),
    }
    story = []

    def para(text,style='body'):
        return Paragraph(escape(text).replace('\n','<br/>'),styles[style])

    def add(text,style='body'):
        story.append(para(text,style))

    def ref_para(items):
        content = '; '.join(f'<link href="#{r["source_id"]}" color="#087F83">{r["source_id"]}</link>: '+escape(r['locator']) for r in items)
        return Paragraph(content,styles['small'])

    def table(rows,widths):
        t = Table([[para(c,'cell') for c in row] for row in rows],colWidths=[w*mm for w in widths],repeatRows=1,hAlign='LEFT')
        t.setStyle(TableStyle([
            ('BACKGROUND',(0,0),(-1,0),light),
            ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F5F8FA')]),
            ('VALIGN',(0,0),(-1,-1),'TOP'),
            ('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),
            ('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),
            ('LINEBELOW',(0,0),(-1,0),0.8,teal),
        ]))
        story.append(t)

    story += [Spacer(1,20*mm),para('CRYPTOLOGIC ARCHIVES / COLLECTION 03','h2'),Spacer(1,7*mm),
              para('Companion\nstandards','title'),para('From primitives to implementations','h1'),Spacer(1,9*mm)]
    add('Modes / parameters / encodings / protocol profiles / selection and evaluation')
    add('Research snapshot '+AS_OF,'small')
    story.append(Spacer(1,12*mm))
    add(f'{len(families)} family maps; {sum(len(f["findings"]) for f in families)} sourced claims and deductions; {len(data["milestones"])} dated milestones.')
    add(f'{new_preserved} additional preserved documents and snapshots. This guide references {len(sources)} records, of which {preserved} are preserved.')
    add('Includes official 2010 SM2/SM3 releases, Russian GOST companion RFCs, ZUC specification and evaluation records, Japanese selection lists, German protocol guidance and Korean cipher profiles.','small')
    story.append(PageBreak())
    add('Scope and how to read','h1')
    for p in data['scope']:add(p)
    add('Layers of a usable cryptographic system','h2')
    rows = [['Layer','Question and examples','Evidence']]
    rows += [[l['name'],l['question']+'\n'+l['examples'],', '.join(l['source_ids'])] for l in data['layers']]
    table(rows,[30,108,32])
    add('Source IDs in the evidence notes link to the source catalogue within this PDF. Original files, checksums, retrieval times and editable research are also in the repository.','small')
    story.append(PageBreak())
    add('Reading map','h1')
    rows = [['Family','Start here','Question resolved']]
    for f in families:
        rows += [[f['name'],', '.join(f['source_ids']),f['reading_order']]]
    table(rows,[39,36,95])
    for f in families:
        story.append(PageBreak())
        add(f['name'],'h1')
        add('Existing profiles: '+', '.join(p['name'] for p in f['profiles']),'small')
        add(f['reading_order'])
        add('Scope limit: '+f['boundary'],'small')
        add('Documented statements','h2')
        for finding in f['findings']:
            if finding['kind'] == 'documented':
                story.append(KeepTogether([para(finding['text']),para(finding['claim_id'],'small'),ref_para(finding['source_refs'])]))
        add('Inference and assumptions','h2')
        for finding in f['findings']:
            if finding['kind'] == 'inference':
                story.append(KeepTogether([
                    para(finding['text']),
                    para('Assumption: '+finding['assumption'],'small'),
                    para(finding['claim_id']+' | Confidence: '+finding['confidence']+' | Basis: '+', '.join(finding['depends_on']),'small'),
                ]))
    story.append(PageBreak())
    add('Publication and effective dates','h1')
    add('These are particular release, revision and publication events. A dated record is not automatically the first invention, first classified use or original algorithm approval.','small')
    rows = [['Date / subject','Event / evidence','Interpretation']]
    rows += [[e['date']+'\n'+e['subject'],e['date_kind']+'\n'+e['source_id']+': '+e['locator'],e['interpretation']] for e in data['milestones']]
    table(rows,[43,59,68])
    story.append(PageBreak())
    add('Preservation and coverage limits','h1')
    for item in data['limitations']:
        story.append(KeepTogether([para(item['title'],'h2'),para(item['text']),para(', '.join(item['source_ids']),'small')]))
    story.append(PageBreak())
    add('Source catalogue','h1')
    add('Only the companion collection is catalogued in this PDF. Original third-party notices remain in the files. A checksum identifies the acquired bytes; it does not authenticate the publisher or establish permission, completeness or implementation approval.','small')
    for source in sources.values():
        d = source['download']
        heading = Paragraph(f'<a name="{source["id"]}"/>'+escape(source['id']+' — '+source['title']),styles['h2'])
        block = [heading,para(source['publisher'],'small'),
                 para('Document date: '+(source['document_date'] or 'not printed / not verified')+' | '+source.get('language','English')+' | '+source['format'],'small'),
                 para('Provenance: '+source['provenance'],'small')]
        if edition(source):block.append(para(edition(source),'small'))
        if source.get('date_note'):block.append(para(source['date_note'],'small'))
        block.append(Paragraph('<link href="'+escape(source['url'],quote=True)+'">'+escape(source['url'])+'</link>',styles['url']))
        if source.get('acquisition_url'):block.append(para('Acquisition URL: '+source['acquisition_url'],'url'))
        if d['status'] == 'archived':
            block += [para(f"Preserved: {source['archive_path']} | {d['bytes']:,} bytes"+(f" | {d['page_count']} pages" if 'page_count' in d else ''),'small'),
                      para('Retrieved UTC: '+d['retrieved_at_utc'],'small'),para('SHA-256: '+d['sha256'],'url')]
        else:
            block += [para('NOT PRESERVED: '+d['status']+'; '+d.get('error','no acquired copy'),'small'),
                      para('Attempt UTC: '+d.get('attempted_at_utc',d.get('retrieved_at_utc','not recorded')),'small')]
        story.append(KeepTogether(block))
        story.append(Spacer(1,3*mm))

    def frame(canvas,doc):
        canvas.saveState()
        width,height = A4
        canvas.setStrokeColor(teal)
        canvas.line(20*mm,height-17*mm,width-20*mm,height-17*mm)
        canvas.setFillColor(navy)
        canvas.setFont('Standards',7)
        canvas.drawString(20*mm,height-13*mm,'CRYPTOLOGIC ARCHIVES / COMPANION STANDARDS')
        canvas.drawString(20*mm,12*mm,'Research snapshot '+AS_OF)
        canvas.drawRightString(width-20*mm,12*mm,str(doc.page))
        canvas.restoreState()

    target = ROOT/'reports/companion-standards.pdf'
    doc = SimpleDocTemplate(str(target),pagesize=A4,leftMargin=20*mm,rightMargin=20*mm,topMargin=24*mm,bottomMargin=22*mm,
                            title=data['title'],author='Cryptologic Archives')
    doc.build(story,onFirstPage=frame,onLaterPages=frame)
    print('Built',target)


if __name__ == '__main__':
    build_markdown()
    build_pdf()
