#!/usr/bin/env python3
"""Check archive integrity, evidence references and generated documents."""
import hashlib
import json
from pathlib import Path
import re
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
errors = []
catalog = json.loads((ROOT/'data/sources.json').read_text())
sources = catalog['sources']
ids = [s['id'] for s in sources]
if len(ids) != len(set(ids)):
    errors.append('Duplicate source IDs')
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
for source in sources:
    info = source['download']
    if info['status'] != 'archived':
        continue
    archived += 1
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
