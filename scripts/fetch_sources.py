#!/usr/bin/env python3
"""Preserve original source bytes and write a reproducible acquisition record."""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / 'data/sources.json'
MAX_BYTES = 95 * 1024 * 1024


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def acquire(source, refresh=False):
    target = ROOT / source['archive_path']
    previous = source.get('download', {})
    if not refresh and target.is_file() and previous.get('status') == 'archived':
        if digest(target) == previous.get('sha256'):
            return previous, 'verified existing copy'
        return {'status':'failed', 'error':'Existing file does not match its recorded checksum; preserved for review.'}, 'checksum mismatch'
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_name(target.name + '.part')
    now = datetime.now(timezone.utc).isoformat()
    request = urllib.request.Request(source.get('acquisition_url', source['url']), headers={'User-Agent':'CryptologicArchives/0.1 (historical research archive)'})
    try:
        with urllib.request.urlopen(request, timeout=45) as response, temporary.open('wb') as output:
            first = response.read(8192)
            if source['format'] == 'pdf' and b'%PDF-' not in first[:1024]:
                raise ValueError('Response does not contain a PDF header')
            if source['format'] == 'text' and b'Request for Comments:' not in first:
                raise ValueError('Response does not contain the expected original RFC text header')
            if source['format'] == 'html' and any(marker in first.lower() for marker in (
                b'your request originates from an undeclared automated tool',
                b'<title>access denied', b'<title>just a moment')):
                raise ValueError('Response is an automated-access interstitial, not the source page')
            h = hashlib.sha256()
            size = 0
            for block in iter(lambda: response.read(1024 * 1024), b''):
                if first:
                    output.write(first)
                    h.update(first)
                    size += len(first)
                    first = b''
                size += len(block)
                if size > MAX_BYTES:
                    raise ValueError('Source exceeds the per-file archive size limit')
                output.write(block)
                h.update(block)
            if first:
                output.write(first)
                h.update(first)
                size += len(first)
            record = {'status':'archived', 'retrieved_at_utc':now,
                      'resolved_url':response.geturl(), 'http_status':response.status,
                      'content_type':response.headers.get('Content-Type', ''),
                      'bytes':size, 'sha256':h.hexdigest()}
        temporary.replace(target)
        if source['format'] == 'pdf':
            try:
                from pypdf import PdfReader
                record['page_count'] = len(PdfReader(target, strict=False).pages)
            except Exception as error:
                record['pdf_inspection_note'] = f'{type(error).__name__}: {error}'
        return record, f'archived {size:,} bytes'
    except (OSError, urllib.error.URLError, ValueError) as error:
        temporary.unlink(missing_ok=True)
        return {'status':'failed', 'attempted_at_utc':now, 'error':f'{type(error).__name__}: {error}'}, f'failed: {error}'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ids', help='Comma-separated source IDs to retrieve')
    parser.add_argument('--refresh', action='store_true', help='Retrieve new snapshots even if verified copies exist')
    parser.add_argument('--workers', type=int, default=4)
    args = parser.parse_args()
    data = json.loads(CATALOG.read_text())
    selected = set(args.ids.split(',')) if args.ids else None
    known = {s['id'] for s in data['sources']}
    if selected and selected - known:
        parser.error('Unknown source IDs: ' + ', '.join(sorted(selected - known)))
    sources = [s for s in data['sources'] if selected is None or s['id'] in selected]
    with ThreadPoolExecutor(max_workers=max(1, min(args.workers, 8))) as pool:
        pending = {pool.submit(acquire, source, args.refresh):source for source in sources}
        for future in as_completed(pending):
            source = pending[future]
            source['download'], message = future.result()
            CATALOG.write_text(json.dumps(data, indent=2) + '\n')
            print(f"{source['id']}: {message}", flush=True)
    archived = sum(s.get('download', {}).get('status') == 'archived' for s in data['sources'])
    print(f'Preserved {archived}/{len(data["sources"])} source records. Retrieval failures remain in the catalogue.', flush=True)


if __name__ == '__main__':
    main()
