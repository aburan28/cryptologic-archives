#!/usr/bin/env python3
"""Build the editable Markdown edition, profile pages, catalogue and PDF."""
from collections import Counter
from html import escape
import json
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
catalog = json.loads((ROOT/'data/sources.json').read_text())
sources = {s['id']:s for s in catalog['sources']}
profiles = json.loads((ROOT/'data/profiles.json').read_text())['profiles']
events = json.loads((ROOT/'data/timeline.json').read_text())['events']
AS_OF = catalog['research_as_of']


def write(path, text):
    (ROOT/path).write_text(text, encoding='utf-8')


def citations(refs):
    return '; '.join(f"[{r['source_id']}](../sources/README.md#{r['source_id'].lower()}), {r['locator']}" for r in refs)


def profile_markdown(profile, report=False):
    parts = [f"{'##' if report else '#'} {profile['name']}", '', profile['synopsis'], '', '### Documented statements', '']
    for item in profile['facts']:
        parts.append(f"- **{item['claim_id']}** — {item['text']} ({citations(item['source_refs'])})")
    parts += ['', '### Technical inferences', '']
    for item in profile['inferences']:
        parts.append(f"- **{item['claim_id']} · {item['confidence']}** — {item['text']} Basis: {', '.join(item['depends_on'])}.")
        if item.get('assumption'):
            parts.append(f"  Assumption: {item['assumption']}")
    parts += ['', '### Unresolved details', ''] + [f'- {text}' for text in profile['unknowns']]
    return '\n'.join(parts)+'\n'


def build_markdown():
    header = f'''# Suite A: a public-source technical and historical record

Research snapshot: {AS_OF}

This first collection translates codeword names into technical roles and bounded inferences. It preserves a distinction between what a source states, what follows under stated assumptions, and what remains unknown. It is a research record rather than an official inventory or current deployment guide.

Suite A names a family of classified cryptographic algorithms. The historical NIST glossary describes its purpose as protecting certain restricted, mission-critical information (S019, printed p.190; PDF p.195). Individual names cover several different cryptographic functions. Product support lists can also contain published algorithms such as AES and equipment compatibility entries.

The evidence spans tactical secure voice, block-cipher interfaces, key establishment, key protection and software distribution. A name in a catalogue may designate an algorithm, a mode, a protocol or an equipment personality.

## From names to primitives

| Function | Examples in this collection | What the evidence exposes |
|---|---|---|
| Symmetric traffic or storage encryption | BATON, JUNIPER, MEDLEY | Block-oriented interfaces, key encodings, mode names and deployment roles; the round functions remain unspecified. |
| Key establishment | FIREFLY, SPONDULIX-S | A public-key description or a key-agreement role; exact mathematical groups and authentication details remain open. |
| Key protection | ACCORDION | Versioned key-wrapping roles; the protected-object format and internal construction remain open. |
| Software confidentiality | JOSEKI, WATARI | Tools and requirements for encrypted software loading; the underlying primitive remains open. |
| Software authenticity | KM-TG schemes, SILVER LINING | Signing and validation roles; the mathematical signature construction remains open. |
| Legacy secure voice | SAVILLE | Program history and an implementation throughput measurement; detailed internal structure needs separate evidence. |

The strongest deductions concern interfaces and roles. An advertised standard mode can constrain a primitive's block size, while a product's support list alone rarely establishes its internal design or cryptanalytic strength.

## How to read the record

Documented statements are source-reported facts, with locators. Inferences identify their premise claim IDs and any conditions. Dates distinguish development, specifications, public acknowledgment, requirements and implementation certification. A later public catalogue does not establish the public availability of the older records it lists.

See [the research method](methodology.md), [the timeline](timeline.md), the [additional-name index](name-index.md), and the [source catalogue](../sources/README.md). Source documents retain their original notices and have not been modified.

'''
    body = header + '\n'.join(profile_markdown(p, report=True) for p in profiles)
    body += '''
## Additional names and catalogue boundaries

Manufacturer records also attest PADSTONE, CRAYON, KEESEE, GOODSPEED, PHALANX, SHILLELAGH, VALLOR, WALBURN, WEASEL, ACME, JACKKNIFE and Mark XII (CADMUS). Viasat lists CAROUSEL, CARDHOLDER and BELSHAZZAR together with equipment compatibility entries. The [additional-name index](name-index.md) records each name's actual evidence, including several names known only from specification titles. Their presence is not a complete design specification or uniform proof of Suite A membership. See S006, S007, S008, S010 and S018.

## Implementation approval

Harris reports that Sierra II received NSA certification in Harris fiscal 2005 (S016). This is a platform milestone, distinct from the development or first approval of every algorithm it can execute. Original first-approval dates for the individual schemes remain open research questions.
'''
    write('docs/suite-a-research.md', body)
    write('profiles/README.md', '# Algorithm and scheme profiles\n\n[International collection: Soviet/Russian, Chinese, German, Japanese and Korean profiles](international/README.md)\n\n## NSA Suite A collection\n\n' + '\n'.join(f"- [{p['name']}]({p['slug']}.md) — {p['synopsis']}" for p in profiles) + '\n')
    for profile in profiles:
        write('profiles/'+profile['slug']+'.md', profile_markdown(profile))
    timeline = ['# Historical timeline', '', 'These are verified record milestones, not claims of the earliest possible appearance or original approval.', '', '| Date | Subject | Date kind | Interpretation | Evidence |', '|---|---|---|---|---|']
    timeline += [f"| {e['date']} | {e['subject']} | {e['date_kind'].replace('_',' ')} | {e['interpretation']} | [{e['source_id']}](../sources/README.md#{e['source_id'].lower()}), {e['locator']} |" for e in events]
    write('docs/timeline.md', '\n'.join(timeline)+'\n')
    counts = Counter(s['download']['status'] for s in sources.values())
    source_doc = ['# Source catalogue', '', f"Research snapshot: {AS_OF}. Preserved: {counts.get('archived',0)}/{len(sources)} records.", '', 'Original source bytes (PDF, RFC text and raw web snapshots) are preserved unchanged. Retrieval time is separate from document date. A checksum identifies the local copy; it is not an authentication certificate.', '']
    for source in sources.values():
        d = source['download']
        source_doc += [f"## {source['id']}", '', f"**{source['title']}**", '', f"Publisher: {source['publisher']}  ", f"Document date: {source['document_date'] or 'Not verified'}  ", f"Provenance: {source['provenance']}  ", f"Original URL: <{source['url']}>  ", f"Preservation status: **{d['status']}**", '']
        if source['date_note']:
            source_doc += [source['date_note'], '']
        source_doc += [f"Collection: {', '.join(source.get('collections',['suite-a']))}  ",f"Region: {source.get('region','United States')}  ",f"Language: {source.get('language','English')}  ",f"Format: {source['format']}", '']
        if source.get('acquisition_url'):
            source_doc += [f"Acquisition URL: <{source['acquisition_url']}>", '']
        if d['status'] == 'archived':
            local = source['archive_path'].removeprefix('sources/')
            source_doc += [f"[Preserved file]({local}) · {d['bytes']:,} bytes" + (f" · {d['page_count']} pages" if 'page_count' in d else ''), '', f"Retrieved: {d['retrieved_at_utc']}  ", f"SHA-256: `{d['sha256']}`", '']
        else:
            source_doc += [f"Retrieval note: {d.get('error','Not yet retrieved.')}", '']
        source_doc += [source['rights'], '']
    write('sources/README.md', '\n'.join(source_doc)+'\n')


def build_pdf():
    pdf_sources = {sid:s for sid,s in sources.items() if 'suite-a' in s.get('collections',['suite-a'])}
    font_root = Path('/usr/share/fonts/truetype/dejavu')
    for name, filename in [('Archive','DejaVuSans.ttf'), ('ArchiveBold','DejaVuSans-Bold.ttf'), ('ArchiveItalic','DejaVuSans-Oblique.ttf')]:
        pdfmetrics.registerFont(TTFont(name, str(font_root/filename)))
    pdfmetrics.registerFontFamily('Archive', normal='Archive', bold='ArchiveBold', italic='ArchiveItalic', boldItalic='ArchiveBold')
    navy = colors.HexColor('#152D42')
    teal = colors.HexColor('#087F83')
    light = colors.HexColor('#EAF3F4')
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='ArchiveBody', fontName='Archive', fontSize=9.3, leading=14, spaceAfter=7, textColor=navy))
    styles.add(ParagraphStyle(name='ArchiveSmall', parent=styles['ArchiveBody'], fontSize=7.4, leading=10.4, textColor=colors.HexColor('#516371')))
    styles.add(ParagraphStyle(name='ArchiveURL', parent=styles['ArchiveSmall'], fontSize=6.5, leading=8.7, wordWrap='CJK'))
    styles.add(ParagraphStyle(name='ArchiveTitle', fontName='ArchiveBold', fontSize=32, leading=38, textColor=navy, spaceAfter=16))
    styles.add(ParagraphStyle(name='ArchiveH1', fontName='ArchiveBold', fontSize=18, leading=23, textColor=navy, spaceBefore=13, spaceAfter=9, keepWithNext=True))
    styles.add(ParagraphStyle(name='ArchiveH2', fontName='ArchiveBold', fontSize=10.5, leading=15, textColor=teal, spaceBefore=8, spaceAfter=5, keepWithNext=True))
    styles.add(ParagraphStyle(name='ArchiveCell', parent=styles['ArchiveSmall'], fontSize=7.1, leading=10, textColor=navy))
    story = []
    def para(text, style='ArchiveBody'):
        return Paragraph(escape(text).replace('\n', '<br/>'), styles[style])
    def add(text, style='ArchiveBody'):
        story.append(para(text, style))
    def refs(items):
        return '; '.join(f"{r['source_id']}: {r['locator']}" for r in items)
    story += [Spacer(1, 20*mm), para('CRYPTOLOGIC ARCHIVES', 'ArchiveH2'), Spacer(1, 7*mm), para('Suite A', 'ArchiveTitle'), para('A public-source technical and historical record', 'ArchiveH1'), Spacer(1, 9*mm)]
    add('From codeword names to technical roles, interfaces and bounded inferences.')
    add(f'Initial collection | Research snapshot {AS_OF}', 'ArchiveSmall')
    story.append(Spacer(1, 15*mm))
    add('What this edition contains', 'ArchiveH2')
    add(f'{len(profiles)} scheme profiles; {len(events)} dated milestones; {len(pdf_sources)} source records; an explicit distinction between documented statements, inference and unresolved questions.')
    add('The accompanying repository contains editable research, structured claims and provenance records, and preserved original documents where retrieval succeeded.')
    add('Original source notices remain in place. This report is not an official algorithm inventory or current deployment guide.', 'ArchiveSmall')
    story.append(PageBreak())
    add('What the names describe', 'ArchiveH1')
    add('Suite A names a family of classified cryptographic algorithms. The historical NIST glossary describes its purpose as protecting certain restricted, mission-critical information. Source: S019, printed p.190; PDF p.195.')
    add('Public records expose several kinds of object: symmetric encryption primitives, key-establishment schemes, key-wrapping mechanisms and software-protection schemes. Manufacturer lists also include published algorithms and equipment compatibility entries.')
    role_rows = [[para(t,'ArchiveCell') for t in ('Function','Names','What public evidence exposes')]]
    for row in [
        ('Symmetric encryption','BATON, JUNIPER, MEDLEY','Block-oriented interfaces, encoded key sizes, mode names and deployment roles.'),
        ('Key establishment','FIREFLY, SPONDULIX-S','Public-key descriptions or key-agreement roles, with parameters unresolved.'),
        ('Key protection','ACCORDION','Versioned wrapping roles in a key-management system.'),
        ('Software confidentiality','JOSEKI, WATARI','Tools and requirements for encrypted software loading.'),
        ('Software authenticity','KM-TG schemes, SILVER LINING','Signing, device-side validation and a prospective migration path.'),
        ('Legacy secure voice','SAVILLE','Program history and implementation throughput; internal design unresolved.')]:
        role_rows.append([para(t,'ArchiveCell') for t in row])
    role_table = Table(role_rows,colWidths=[36*mm,48*mm,86*mm],repeatRows=1,hAlign='LEFT')
    role_table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),light),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F5F8FA')]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
    story.append(role_table)
    story.append(Spacer(1,6*mm))
    add('The strongest deductions concern interfaces and roles. An advertised standard mode can constrain a primitive\'s block size. A product support list alone rarely establishes an internal design, design ancestry or cryptanalytic strength.')
    story.append(PageBreak())
    add('Reading the evidence', 'ArchiveH1')
    add('A manufacturer statement establishes what that manufacturer advertised. A dated specification establishes the existence of a record by that date. Neither automatically establishes deployment, an original approval date, or the internal mathematics of an algorithm.')
    for label, text in [('Documented','A source-reported statement with a page, section or table locator.'), ('Strong inference','A consequence supported by identified premises.'), ('Conditional inference','A consequence that depends on a stated assumption.'), ('Moderate inference','A plausible reading with competing explanations.'), ('Unknown','A detail that the cited records do not establish.')]:
        add(label, 'ArchiveH2'); add(text)
    add('Dates and versions', 'ArchiveH2')
    add('Keep event date, document date, public-release date and retrieval time separate. Fiscal years remain fiscal years. A later public catalogue can identify an older specification without proving that it was publicly available in the older year.')
    add('Preservation', 'ArchiveH2')
    add('Each preserved source has an original URL, resolved URL, retrieval timestamp, byte count and SHA-256 in data/sources.json. Mirrors and transcriptions are labeled. Hashes identify local bytes, not the truth or authenticity of the document. Failed retrievals remain visible.')
    story.append(PageBreak())
    add('Dated milestones', 'ArchiveH1')
    add('These are record milestones. They are not earliest-ever or original-approval claims.', 'ArchiveSmall')
    rows = [[para(t,'ArchiveCell') for t in ('Date / subject','Kind / evidence','Interpretation')]]
    for event in events:
        rows.append([para(event['date']+'\n'+event['subject'],'ArchiveCell'), para(event['date_kind'].replace('_',' ')+'\n'+event['source_id']+' · '+event['locator'],'ArchiveCell'), para(event['interpretation'],'ArchiveCell')])
    table = Table(rows, colWidths=[43*mm,47*mm,80*mm], repeatRows=1, hAlign='LEFT')
    table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),light), ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F5F8FA')]), ('VALIGN',(0,0),(-1,-1),'TOP'), ('LEFTPADDING',(0,0),(-1,-1),7), ('RIGHTPADDING',(0,0),(-1,-1),7), ('TOPPADDING',(0,0),(-1,-1),7), ('BOTTOMPADDING',(0,0),(-1,-1),7), ('LINEBELOW',(0,0),(-1,0),1,teal)]))
    story.append(table)
    story.append(PageBreak())
    add('Technical profiles', 'ArchiveH1')
    for profile in profiles:
        story.append(KeepTogether([para(profile['name'],'ArchiveH1'), para(profile['synopsis'])]))
        add('Documented statements', 'ArchiveH2')
        for item in profile['facts']:
            story.append(KeepTogether([para(item['text']),para(refs(item['source_refs']),'ArchiveSmall')]))
        add('Technical inferences', 'ArchiveH2')
        for item in profile['inferences']:
            block = [para(item['confidence'].capitalize()+' — '+item['text'])]
            if item.get('assumption'):
                block.append(para('Assumption: '+item['assumption'], 'ArchiveSmall'))
            block.append(para(refs(item['source_refs']),'ArchiveSmall'))
            story.append(KeepTogether(block))
        add('Unresolved details', 'ArchiveH2')
        for text in profile['unknowns']:
            add(text)
        story.append(Spacer(1, 5*mm))
    story.append(PageBreak())
    add('Further names and approval records', 'ArchiveH1')
    add('Manufacturer records attest PADSTONE, CRAYON, KEESEE, GOODSPEED, PHALANX, SHILLELAGH, VALLOR, WALBURN, WEASEL, ACME, JACKKNIFE and Mark XII (CADMUS). Viasat lists CAROUSEL, CARDHOLDER and BELSHAZZAR alongside compatibility entries. These names are research leads rather than complete design descriptions or a uniform inventory. Sources: S006, S007, S008, S018.')
    add('The 2019 requirements bibliography also identifies MAYFLY, SAFEBOX-E, SAFEBOX-S, ALDERFLY II and SPONDULIX-E. Titles and document dates alone do not disclose their constructions or prove that similarly named variants are interchangeable. Source: S010, printed pp.4-5.')
    add('The companion docs/name-index.md records all of these additional leads, with evidence locators and limits. Motorola\'s original AIM leaflet additionally advertises PHALANX at 1.39 bits per input clock and KEESEE at 1.00; these are implementation measurements rather than security estimates. Source: S006, p.1.')
    add('Harris reports Sierra II certification in Harris fiscal 2005 (S016). This is a platform milestone, distinct from the development or first approval of every algorithm it can execute. Original first-approval records for the individual schemes remain a useful acquisition target.')
    add('Questions for the next edition', 'ArchiveH2')
    for text in ['Find original first-approval records for individual schemes.', 'Verify precise publication and release dates for manufacturer leaflets.', 'Locate a primary design record for detailed SAVILLE reconstructions.', 'Determine the construction behind the 2002 An ACCORDION MEDLEY reference.', 'Locate public parameter or interface specifications for SPONDULIX-S and SILVER LINING.']:
        add(text)
    story.append(PageBreak())
    add('Source catalogue', 'ArchiveH1')
    counts = Counter(s['download']['status'] for s in pdf_sources.values())
    add(f"Preserved {counts.get('archived',0)} of {len(pdf_sources)} source records for this collection. The repository catalogue additionally covers the international collection.", 'ArchiveSmall')
    for source in pdf_sources.values():
        d = source['download']
        block = [para(source['id']+' · '+source['title'],'ArchiveH2'),para(source['publisher']+' | Document date: '+(source['document_date'] or 'not verified'), 'ArchiveSmall')]
        if source['date_note']:
            block.append(para(source['date_note'], 'ArchiveSmall'))
        block.append(para('Provenance: '+source['provenance'], 'ArchiveSmall'))
        block.append(para(source['url'], 'ArchiveURL'))
        if source.get('acquisition_url'):
            block.append(para('Acquisition URL: '+source['acquisition_url'], 'ArchiveURL'))
        if d['status'] == 'archived':
            block.append(para(f"Preserved: {source['archive_path']} | {d['bytes']:,} bytes" + (f" | {d['page_count']} pages" if 'page_count' in d else ''), 'ArchiveSmall'))
            block.append(para('Retrieved (UTC): '+d['retrieved_at_utc'], 'ArchiveSmall'))
            block.append(para('SHA-256: '+d['sha256'], 'ArchiveURL'))
        else:
            block.append(para('Preservation status: '+d['status']+'. '+d.get('error',''), 'ArchiveSmall'))
        story.append(KeepTogether(block))
        story.append(Spacer(1, 3*mm))
    def page_frame(canvas, doc):
        canvas.saveState()
        width, height = A4
        canvas.setStrokeColor(teal)
        canvas.setLineWidth(0.8)
        canvas.line(20*mm, height-17*mm, width-20*mm, height-17*mm)
        canvas.setFont('Archive',7)
        canvas.setFillColor(navy)
        canvas.drawString(20*mm, height-13*mm, 'CRYPTOLOGIC ARCHIVES / PUBLIC-SOURCE RESEARCH')
        canvas.drawString(20*mm, 12*mm, 'Research snapshot '+AS_OF)
        canvas.drawRightString(width-20*mm,12*mm,str(doc.page))
        canvas.restoreState()
    target = ROOT/'reports/suite-a-research.pdf'
    doc = SimpleDocTemplate(str(target), pagesize=A4, leftMargin=20*mm, rightMargin=20*mm, topMargin=24*mm, bottomMargin=22*mm, title='Suite A: A Public-Source Technical and Historical Record', author='Cryptologic Archives')
    doc.build(story, onFirstPage=page_frame, onLaterPages=page_frame)
    print('Built', target)


if __name__ == '__main__':
    claims = []
    for profile in profiles:
        for kind, items in [('documented',profile['facts']),('inference',profile['inferences'])]:
            claims.extend({'id':item['claim_id'],'profile':profile['slug'],'kind':kind,**item} for item in items)
    write('data/claims.json',json.dumps({'schema_version':1,'claims':claims},indent=2)+'\n')
    build_markdown()
    build_pdf()
