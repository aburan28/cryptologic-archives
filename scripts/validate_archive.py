#!/usr/bin/env python3
"""Check archive integrity, evidence references and generated documents."""
import hashlib
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
errors = []
catalog = json.loads((ROOT/'data/sources.json').read_text())
sources = catalog['sources']
ids = [s['id'] for s in sources]
if len(ids) != len(set(ids)):
    errors.append('Duplicate source IDs')
paths = [s['archive_path'] for s in sources]
if len(paths) != len(set(paths)):
    errors.append('Duplicate source archive paths')
source_ids = set(ids)
sources_by_id = {s['id']:s for s in sources}
claims = []
for claim_file in sorted((ROOT/'data').glob('*claims.json')):
    claims.extend(json.loads(claim_file.read_text())['claims'])
claim_ids = {c['id'] for c in claims}
if len(claim_ids) != len(claims):
    errors.append('Duplicate claim IDs')
for claim in claims:
    if claim['kind'] == 'documented' and not claim.get('source_refs'):
        errors.append('Documented claim lacks evidence: '+claim['id'])
    for ref in claim.get('source_refs', []):
        if ref['source_id'] not in source_ids or not ref.get('locator'):
            errors.append(f"Invalid reference in {claim['id']}")
        elif claim['kind'] == 'documented' and sources_by_id[ref['source_id']]['download']['status'] != 'archived':
            errors.append(f"Unpreserved evidence in {claim['id']}: {ref['source_id']}")
    for dep in claim.get('depends_on', []):
        if dep not in claim_ids:
            errors.append(f"Missing premise {dep} in {claim['id']}")
international = json.loads((ROOT/'data/international.json').read_text())
standards = json.loads((ROOT/'data/standards.json').read_text())
for profile in international['profiles']:
    canonical = {item['claim_id']:(kind,item) for kind,key in [('documented','facts'),('inference','inferences')]
                 for item in profile[key]}
    normalized = {c['id']:c for c in claims if c.get('collection') == 'international' and c.get('profile') == profile['slug']}
    if canonical.keys() != normalized.keys() or any(
        normalized[cid]['kind'] != kind or any(normalized[cid].get(k) != value for k,value in item.items())
        for cid,(kind,item) in canonical.items()
    ):
        errors.append('Stale generated international claims: '+profile['slug'])
continuation = standards.get('continuation',{})
for sid in continuation.get('new_source_ids',[]):
    source = sources_by_id.get(sid,{})
    if not source or source.get('download',{}).get('status') != 'archived':
        errors.append('Missing continuation acquisition: '+sid)
    for field in ['publisher','provenance','document_date','version','extent','host']:
        if field not in source:
            errors.append(f'Missing continuation metadata {field}: {sid}')
for family in standards['families']:
    for sid in family['source_ids']:
        if sid not in source_ids or 'standards' not in sources_by_id[sid].get('collections',[]):
            errors.append(f"Invalid companion source in {family['id']}: {sid}")
    for profile in family['profiles']:
        if not (ROOT/profile['path']).is_file():
            errors.append('Missing mapped profile: '+profile['path'])
    canonical = {item['claim_id']:item for item in family['findings']}
    normalized = {c['id']:c for c in claims if c.get('collection') == 'standards' and c.get('family') == family['id']}
    if canonical.keys() != normalized.keys() or any(
        any(normalized[cid].get(k) != value for k,value in item.items()) for cid,item in canonical.items()
    ):
        errors.append('Stale generated companion claims: '+family['id'])
for layer in standards['layers']:
    for sid in layer['source_ids']:
        if sid not in source_ids:
            errors.append('Invalid source in standards layer: '+sid)
events = json.loads((ROOT/'data/timeline.json').read_text())['events'] + international['events'] + standards['milestones']
for event in events:
    if event['source_id'] not in source_ids:
        errors.append('Invalid timeline source '+event['source_id'])
archived = 0
archived_hashes = {}
for source in sources:
    info = source['download']
    if info['status'] != 'archived':
        continue
    archived += 1
    for field in ['retrieved_at_utc','resolved_url','content_type','bytes','sha256']:
        if not info.get(field):
            errors.append(f'Missing acquisition field {field}: {source["id"]}')
    if info.get('sha256') in archived_hashes:
        errors.append(f'Duplicate acquired bytes: {source["id"]}, {archived_hashes[info["sha256"]]}')
    archived_hashes[info.get('sha256')] = source['id']
    target = ROOT/source['archive_path']
    if not target.is_file():
        errors.append('Missing archived file '+source['id'])
        continue
    h = hashlib.sha256()
    with target.open('rb') as handle:
        for block in iter(lambda: handle.read(1024*1024), b''):
            h.update(block)
    if h.hexdigest() != info['sha256'] or target.stat().st_size != info['bytes']:
        errors.append('Integrity mismatch '+source['id'])
    if source['format'] == 'pdf':
        try:
            source_pdf = PdfReader(target, strict=False)
            page_count = len(source_pdf.pages)
            if page_count < 1:
                errors.append('Empty PDF '+source['id'])
            if info.get('page_count',page_count) != page_count:
                errors.append('PDF page-count mismatch '+source['id'])
        except Exception as error:
            errors.append(f"Unreadable PDF {source['id']}: {error}")
    if source['format'] == 'xml':
        try:
            xml_root = ET.parse(target).getroot()
            if source['id'] == 'S100' and xml_root.tag != '{https://www.rfc-editor.org/rfc-index}rfc-index':
                errors.append('Incorrect publisher-index XML root: '+source['id'])
        except ET.ParseError as error:
            errors.append(f"Unreadable XML {source['id']}: {error}")
    rfc = re.match(r'RFC (\d+):',source['title'])
    if rfc:
        number = rfc.group(1)
        if not re.search(r'/rfc'+number+r'\.(?:txt|pdf)(?:$|[?#])',source['url']):
            errors.append('RFC title/URL mismatch: '+source['id'])
        if source['format'] == 'text':
            header = target.read_text()[:6000]
        elif source['format'] == 'pdf':
            header = '\n'.join(p.extract_text() or '' for p in PdfReader(target).pages[:2])
        else:
            header = ''
        if not re.search(r'(?:Request for Comments:|RFC:|RFC)\s*'+number+r'\b',header):
            errors.append('RFC identity missing from acquired header: '+source['id'])
        if source.get('metadata_source_id') == 'S100':
            ns = {'r':'https://www.rfc-editor.org/rfc-index'}
            index = ET.parse(ROOT/sources_by_id['S100']['archive_path']).getroot()
            entry = next((e for e in index.findall('r:rfc-entry',ns)
                          if e.findtext('r:doc-id',namespaces=ns) == 'RFC'+number),None)
            if entry is None:
                errors.append('RFC absent from preserved index: '+source['id'])
            else:
                stream = entry.findtext('r:stream',namespaces=ns)
                expected_stream = {'INDEPENDENT':'Independent Submission',
                    'Legacy':'Legacy (publisher index; original header predates stream labels)'}.get(stream,stream)
                if source['publication_stream'] != expected_stream:
                    errors.append('RFC stream differs from preserved index: '+source['id'])
                for field,tag in [('publication_status','publication-status'),('current_status_at_retrieval','current-status')]:
                    if source[field] != entry.findtext('r:'+tag,namespaces=ns):
                        errors.append('RFC status differs from preserved index: '+source['id'])
for markdown in ROOT.rglob('*.md'):
    for link in re.findall(r'\]\(([^)]+)\)', markdown.read_text()):
        if '://' in link or link.startswith('#'):
            continue
        path = link.split('#',1)[0]
        if path and not (markdown.parent/path).exists():
            errors.append(f'Broken local link in {markdown.relative_to(ROOT)}: {link}')
reports = [('suite-a-research.pdf',['MEDLEY','BATON','JOSEKI','SAVILLE','Source catalogue','1987-10-30']),
           ('international-cryptography.pdf',[p['name'] for p in international['profiles']]+['Source catalogue','1918-02-23','2022-06-30']),
           ('companion-standards.pdf',[f['name'] for f in standards['families']]+
            [item['claim_id'] for f in standards['families'] for item in f['findings']]+
            ['Source catalogue','2010-12-17','2024-06-01','NOT PRESERVED','incomplete','v1.7','v1.8'])]
for filename,phrases in reports:
    try:
        reader = PdfReader(ROOT/'reports'/filename)
        text = '\n'.join(page.extract_text() or '' for page in reader.pages)
        normalized_text = ' '.join(text.split())
        for phrase in phrases:
            if ' '.join(phrase.split()) not in normalized_text:
                errors.append('Missing content in '+filename+': '+phrase)
        print(f'{filename}: {len(reader.pages)} pages; {len(text):,} extractable characters')
    except Exception as error:
        errors.append('Report inspection failed: '+filename+': '+str(error))
if errors:
    for error in errors:
        print('ERROR:', error)
    raise SystemExit(1)
print(f'PASS: {len(claims)} claims; {len(sources)} source records; {archived} preserved files; checksums and local links verified.')
pending = [s['id'] for s in sources if s['download']['status'] != 'archived']
if pending:
    print('Unpreserved sources remain explicit in the catalogue:', ', '.join(pending))
