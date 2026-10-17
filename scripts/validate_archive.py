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
claims = []
for claim_file in sorted((ROOT/'data').glob('*claims.json')):
    claims.extend(json.loads(claim_file.read_text())['claims'])
claim_ids = {c['id'] for c in claims}
if len(claim_ids) != len(claims):
    errors.append('Duplicate claim IDs')
for claim in claims:
    for ref in claim.get('source_refs', []):
        if ref['source_id'] not in source_ids or not ref.get('locator'):
            errors.append(f"Invalid reference in {claim['id']}")
    for dep in claim.get('depends_on', []):
        if dep not in claim_ids:
            errors.append(f"Missing premise {dep} in {claim['id']}")
international = json.loads((ROOT/'data/international.json').read_text())
events = json.loads((ROOT/'data/timeline.json').read_text())['events'] + international['events']
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
            page_count = len(PdfReader(target, strict=False).pages)
            if page_count < 1:
                errors.append('Empty PDF '+source['id'])
            if info.get('page_count',page_count) != page_count:
                errors.append('PDF page-count mismatch '+source['id'])
        except Exception as error:
            errors.append(f"Unreadable PDF {source['id']}: {error}")
for markdown in ROOT.rglob('*.md'):
    for link in re.findall(r'\]\(([^)]+)\)', markdown.read_text()):
        if '://' in link or link.startswith('#'):
            continue
        path = link.split('#',1)[0]
        if path and not (markdown.parent/path).exists():
            errors.append(f'Broken local link in {markdown.relative_to(ROOT)}: {link}')
reports = [('suite-a-research.pdf',['MEDLEY','BATON','JOSEKI','SAVILLE','Source catalogue','1987-10-30']),
           ('international-cryptography.pdf',[p['name'] for p in international['profiles']]+['Source catalogue','1918-02-23','2022-06-30'])]
for filename,phrases in reports:
    try:
        reader = PdfReader(ROOT/'reports'/filename)
        text = '\n'.join(page.extract_text() or '' for page in reader.pages)
        for phrase in phrases:
            if phrase not in text:
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
