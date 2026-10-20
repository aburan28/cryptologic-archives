#!/usr/bin/env python3
"""Build the international collection, profiles, evidence records and PDF."""
from collections import Counter
from html import escape
import json
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether

ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'data/international.json').read_text())
catalog=json.loads((ROOT/'data/sources.json').read_text())
sources={s['id']:s for s in catalog['sources'] if 'international' in s.get('collections',[])}
profiles=data['profiles']
events=data['events']
AS_OF=data['research_as_of']
companion=json.loads((ROOT/'data/standards.json').read_text())
families_for_profile={}
for family in companion['families']:
    for profile in family['profiles']:
        families_for_profile.setdefault(profile['path'],[]).append(family)

def write(path,text):
    p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf8')

def citations(refs,prefix='../'):
    return '; '.join(f"[{r['source_id']}]({prefix}sources/README.md#{r['source_id'].lower()}), {r['locator']}" for r in refs)

def profile_md(p,standalone=False):
    prefix='../../' if standalone else '../'
    lines=[f"{'#' if standalone else '##'} {p['name']}",'',p['synopsis'],'',f"Region: {p['region']}  ",f"Role: {p['role']}  ",f"Construction: {p['primitive']}  ",f"Parameters: {p['parameters']}",'','### Documented statements','']
    for f in p['facts']:lines += [f"- **{f['claim_id']}** — {f['text']} ({citations(f['source_refs'],prefix)})"]
    lines+=['','### Technical inferences','']
    for i in p['inferences']:
        lines+=[f"- **{i['claim_id']} · {i['confidence']}** — {i['text']} Basis: {', '.join(i['depends_on'])}."]
        if i.get('assumption'):lines+=['  Assumption: '+i['assumption']]
    lines+=['','### Unresolved details','']+['- '+u for u in p['unknowns']]
    for family in families_for_profile.get('profiles/international/'+p['slug']+'.md',[]):
        lines+=['',f"[Companion standards: {family['name']}]({prefix}docs/companion-standards.md#{family['id']})"]
    return '\n'.join(lines)+'\n'

INTRO='''This collection extends the archive across Soviet/Russian, Chinese, German, Japanese, Korean, Swiss and Swedish cryptographic records, with French recommendation and evaluation context in the companion guide. It records public national standards, historical military machines and government systems for which only limited architectural information is public.

Regional labels describe design or historical context. They are not assertions of exclusive use, present-day approval or equivalence to NSA Suite A. Hashes, signatures, key-establishment protocols and encryption ciphers have distinct roles.

Every profile separates source-reported statements, deductions and unresolved details. A patent application, standard issue, implementation date, procurement contract, RFC publication and approval withdrawal are different event types. A public standards document does not identify a country's entire classified cryptographic inventory.
'''

def markdown():
    lines=['# International cryptography: constructions and historical records','',f'Research snapshot: {AS_OF}','',INTRO,'## Comparison','', '| Region | Scheme | Role / construction | Parameters |','|---|---|---|---|']
    for p in profiles:lines += [f"| {p['region']} | [{p['name']}](../profiles/international/{p['slug']}.md) | {p['role']}; {p['primitive']} | {p['parameters']} |"]
    lines+=['','See the [international timeline](international-timeline.md), [profile index](../profiles/international/README.md), [companion standards](companion-standards.md), and [source catalogue](../sources/README.md).','']
    lines += [profile_md(p) for p in profiles]
    lines += ['## Translation and preservation notes','','The seven English SM2/SM3/SM4 files are preserved as hosted by Alipay. Their covers lack official dated Chinese standard identifiers; the filenames alone do not verify an edition or an authorized translation. In particular, the SM2 Part 5 filename contains 2016 while RFC 8998 cites a 2017 standard. The catalogue keeps this discrepancy visible. Official Chinese records and the contemporary OSCCA announcement provide separate date evidence.','','Official 2010 SM2 Parts 1–4, the recommended-curve sheet, and the original SM3 release are now preserved separately (S096–S098), together with the 2010-12-17 announcements (S070–S071). These earlier release texts are distinct from the hosted English translations and later GM/T/GB/T editions.','','The Chinese-language 2012/2014 companion scans (S109–S114) are pinned third-party mirror copies. S109 includes all body pages 1–7; the earlier S074 remains incomplete. Russian mirror copies retain host-added advertising/link text. New French distribution links point to different PDF editions (2026 rules and a 2021 selection guide). These provenance and edition distinctions remain explicit in the companion guide.','','The Fialka manual copy explicitly lacks original pages 2, 4 and 60. Turing Chapter 1, the Newmanry report portion and the Bletchley dictionary are edited transcriptions. They are labeled as such. Original RFC text is preserved when that is the publisher\'s available source format.','','## Further acquisitions','','French ANSSI guides, original Swiss NEMA instructions and Swedish FRA historical records are now preserved. Further targets include original Swiss approval records, additional Swedish contemporary machine documents, Israeli and Indian collections, earlier Chinese cryptologic history, and public records of further Soviet equipment. Original first-approval and full revised standards remain separate acquisition questions. This edition does not claim worldwide completeness.','']
    write('docs/international-cryptography.md','\n'.join(lines))
    index=['# International algorithm and system profiles','',f'{len(profiles)} profiles. Detailed evidence is linked from each page.','']
    for p in profiles:
        index += [f"- [{p['name']}]({p['slug']}.md) — {p['region']}; {p['role']}."]
        write('profiles/international/'+p['slug']+'.md',profile_md(p,True))
    write('profiles/international/README.md','\n'.join(index)+'\n')
    timeline=['# International historical timeline','','Events describe particular records and milestones; an early record is not automatically the earliest use or first approval.','','| Date | Subject | Kind | Interpretation | Evidence |','|---|---|---|---|---|']
    for e in events:
        timeline += [f"| {e['date']} | {e['subject']} | {e['date_kind'].replace('_',' ')} | {e['interpretation']} | [{e['source_id']}](../sources/README.md#{e['source_id'].lower()}), {e['locator']} |"]
    write('docs/international-timeline.md','\n'.join(timeline)+'\n')
    claims=[]
    for p in profiles:
        for kind,items in [('documented',p['facts']),('inference',p['inferences'])]:
            claims.extend({'id':i['claim_id'],'profile':p['slug'],'kind':kind,'collection':'international',**i} for i in items)
    write('data/international-claims.json',json.dumps({'schema_version':1,'claims':claims},indent=2,ensure_ascii=False)+'\n')

def pdf():
    fonts=Path('/usr/share/fonts/truetype/dejavu')
    for name,file in [('Intl','DejaVuSans.ttf'),('IntlBold','DejaVuSans-Bold.ttf')]:pdfmetrics.registerFont(TTFont(name,str(fonts/file)))
    pdfmetrics.registerFontFamily('Intl',normal='Intl',bold='IntlBold',italic='Intl',boldItalic='IntlBold')
    navy=colors.HexColor('#152D42');teal=colors.HexColor('#087F83');light=colors.HexColor('#EAF3F4')
    styles={
        'body':ParagraphStyle('IntlBody',fontName='Intl',fontSize=9.2,leading=14,spaceAfter=7,textColor=navy),
        'small':ParagraphStyle('IntlSmall',fontName='Intl',fontSize=7.3,leading=10.5,spaceAfter=6,textColor=colors.HexColor('#516371')),
        'url':ParagraphStyle('IntlURL',fontName='Intl',fontSize=6.4,leading=8.6,spaceAfter=5,wordWrap='CJK',textColor=navy),
        'title':ParagraphStyle('IntlTitle',fontName='IntlBold',fontSize=29,leading=36,spaceAfter=16,textColor=navy),
        'h1':ParagraphStyle('IntlH1',fontName='IntlBold',fontSize=18,leading=23,spaceBefore=12,spaceAfter=9,keepWithNext=True,textColor=navy),
        'h2':ParagraphStyle('IntlH2',fontName='IntlBold',fontSize=10.5,leading=15,spaceBefore=8,spaceAfter=5,keepWithNext=True,textColor=teal),
        'cell':ParagraphStyle('IntlCell',fontName='Intl',fontSize=7,leading=10,spaceAfter=0,textColor=navy)}
    story=[]
    def para(text,style='body'):return Paragraph(escape(text).replace('\n','<br/>'),styles[style])
    def add(text,style='body'):story.append(para(text,style))
    def refs(items):return '; '.join(r['source_id']+': '+r['locator'] for r in items)
    def table(rows,widths):
        t=Table([[para(c,'cell') for c in row] for row in rows],colWidths=[x*mm for x in widths],repeatRows=1,hAlign='LEFT')
        t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),light),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F5F8FA')]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3),('LINEBELOW',(0,0),(-1,0),0.8,teal)]))
        story.append(t)
    story+=[Spacer(1,20*mm),para('CRYPTOLOGIC ARCHIVES / COLLECTION 02','h2'),Spacer(1,7*mm),para('International\ncryptography','title'),para('Constructions and historical records','h1'),Spacer(1,9*mm)]
    add('Soviet Union and Russia / China / Germany / Japan / Republic of Korea / Switzerland / Sweden / international standards')
    add(f'Research snapshot {AS_OF}','small')
    story.append(Spacer(1,12*mm))
    add(f'{len(profiles)} profiles; {len(events)} dated milestones; {len(sources)} source records in this collection.')
    add('Original documents, public specifications, mathematical structure and carefully bounded deductions.')
    add('Companion collection: NSA Suite A, preserved separately in the same archive.','small')
    story.append(PageBreak())
    add('Scope and evidence','h1')
    for text in INTRO.strip().split('\n\n'):add(text)
    add('What can be made concrete','h2')
    add('Published specifications expose operations such as modular addition, byte substitution, linear diffusion, elliptic-curve point multiplication and rotor permutations. Government product histories sometimes establish only a role, implementation boundary or migration. Each profile states what its cited records actually support.')
    add('Source formats and translations','h2')
    add('The archive preserves PDFs, original RFC text and raw web snapshots. Each acquired file has a SHA-256, timestamp and original/resolved URL in data/sources.json. English translations, edited transcriptions and scans are distinguished.')
    add('The seven hosted Chinese standard translations lack official dated Chinese covers. Their filenames do not independently establish an edition or translation authority. SM2 Part 5 illustrates the issue: the filename contains 2016, while RFC 8998 cites a 2017 standard.')
    add('Official 2010 SM2 Parts 1–4, the recommended-curve sheet, and the original SM3 release are preserved separately in S096–S098. The 2010-12-17 announcements in S070–S071 provide direct release-date evidence. These are distinct from later GM/T/GB/T editions.','small')
    add('The 2026-10-20 continuation preserves Chinese-language companion scans, German ECC/Brainpool records, MISTY1/KCipher-2/KASUMI and SNOW 3G specifications, an original NEMA manual and Swedish agency historical accounts. S109 fills the missing body pages in the earlier GM/T 0009-2012 acquisition; S074 remains unchanged and incomplete.','small')
    add('The Fialka manual copy explicitly lacks pages 2, 4 and 60. The Tunny/Newmanry PDF preserves only part of the complete wartime report. These limitations remain visible in the catalogue.','small')
    story.append(PageBreak())
    add('Comparison of constructions','h1')
    rows=[['Region','Scheme','Role / construction','Parameters']]
    rows += [[p['region'],p['name'],p['role']+'\n'+p['primitive'],p['parameters']] for p in profiles]
    table(rows,[28,33,55,54])
    story.append(PageBreak())
    add('Historical milestones','h1')
    add('These dates distinguish applications, publications, standards, system development and approval withdrawal. They are not a uniform list of invention or first-approval dates.','small')
    rows=[['Date / subject','Kind / evidence','Interpretation']]
    rows += [[e['date']+'\n'+e['subject'],e['date_kind'].replace('_',' ')+'\n'+e['source_id']+' · '+e['locator'],e['interpretation']] for e in events]
    table(rows,[44,51,75])
    for p in profiles:
        story.append(PageBreak())
        add(p['name'],'h1');add(p['region']+' | '+p['role'],'small');add(p['synopsis'])
        add(p['primitive'],'h2');add(p['parameters'])
        add('Documented statements','h2')
        for f in p['facts']:
            story.append(KeepTogether([para(f['text']),para(f['claim_id']+' | '+refs(f['source_refs']),'small')]))
        add('Technical inferences','h2')
        for i in p['inferences']:
            block=[para(i['confidence'].capitalize()+' — '+i['text'])]
            if i.get('assumption'):block.append(para('Assumption: '+i['assumption'],'small'))
            block.append(para(i['claim_id']+' | Basis: '+', '.join(i['depends_on']),'small'))
            story.append(KeepTogether(block))
        add('Unresolved details','h2')
        for text in p['unknowns']:add(text)
    story.append(PageBreak())
    add('Source catalogue','h1')
    add('This catalogue covers the international collection. The repository catalogue additionally includes the earlier Suite A sources. Files retain their original notices.','small')
    for s in sources.values():
        d=s['download']
        block=[para(s['id']+' · '+s['title'],'h2'),para(s['publisher'],'small'),para('Document date: '+(s['document_date'] or 'not verified')+' | Language: '+s.get('language','English')+' | Format: '+s['format'],'small'),para('Provenance: '+s['provenance'],'small')]
        if s['date_note']:block.append(para(s['date_note'],'small'))
        for key,label in [('version','Edition'),('original_issue_date','Initial issue'),('revision_date','Revision'),
                          ('effective_date','Effective'),('printed_edition_date','Printing'),
                          ('declassification_date','Declassification annotation'),
                          ('publication_category','RFC category'),('publication_stream','RFC stream'),('extent','Extent')]:
            if s.get(key):block.append(para(label+': '+s[key],'small'))
        block.append(para(s['url'],'url'))
        if s.get('acquisition_url'):block.append(para('Acquisition URL: '+s['acquisition_url'],'url'))
        if d['status']=='archived':
            block += [para(f"Preserved: {s['archive_path']} | {d['bytes']:,} bytes"+(f" | {d['page_count']} pages" if 'page_count' in d else ''),'small'),para('Retrieved UTC: '+d['retrieved_at_utc'],'small'),para('SHA-256: '+d['sha256'],'url')]
        else:block.append(para('Preservation status: '+d['status']+'; '+d.get('error',''),'small'))
        story.append(KeepTogether(block));story.append(Spacer(1,3*mm))
    def frame(canvas,doc):
        canvas.saveState();width,height=A4;canvas.setStrokeColor(teal);canvas.line(20*mm,height-17*mm,width-20*mm,height-17*mm)
        canvas.setFillColor(navy);canvas.setFont('Intl',7);canvas.drawString(20*mm,height-13*mm,'CRYPTOLOGIC ARCHIVES / INTERNATIONAL COLLECTION')
        canvas.drawString(20*mm,12*mm,'Research snapshot '+AS_OF);canvas.drawRightString(width-20*mm,12*mm,str(doc.page));canvas.restoreState()
    target=ROOT/'reports/international-cryptography.pdf'
    doc=SimpleDocTemplate(str(target),pagesize=A4,leftMargin=20*mm,rightMargin=20*mm,topMargin=24*mm,bottomMargin=22*mm,title='International Cryptography: Constructions and Historical Records',author='Cryptologic Archives')
    doc.build(story,onFirstPage=frame,onLaterPages=frame)
    print('Built',target)

if __name__=='__main__':
    markdown();pdf()
