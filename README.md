# Cryptologic Archives

A historical research archive of public cryptologic records, original documents, and technical inferences. The first collection examines NSA Suite A and the surrounding equipment, key-management, and software-protection ecosystem.

## Start here

- [Research report](docs/suite-a-research.md) and [PDF edition](reports/suite-a-research.pdf)
- [Algorithm profiles](profiles/README.md)
- [Additional codeword and scheme index](docs/name-index.md)
- [Historical timeline](docs/timeline.md)
- [Source catalogue and preservation status](sources/README.md)
- [Research method](docs/methodology.md)
- [Machine-readable claims](data/claims.json), [sources](data/sources.json), and [timeline](data/timeline.json)

## What the archive records

Each profile separates documented statements, technical inferences with assumptions, and unresolved questions. Dates distinguish program history, specifications, public documentation, requirements, and certification of a particular implementation. A date is not labeled the first appearance or first approval without evidence for that claim.

Original PDFs are stored in `sources/originals/`; raw web snapshots are stored in `sources/web/`. The catalogue records retrieval time, resolved URL, file size and SHA-256 for preserved copies. A preserved file's hash confirms byte identity, not its truth, authenticity or release authorization.

## Reproduce and check

```sh
python -m pip install -r requirements.txt
python scripts/fetch_sources.py
python scripts/build_report.py
python scripts/validate_archive.py
```

Use Python 3.9 or later. The PDF builder uses DejaVu Sans fonts from `/usr/share/fonts/truetype/dejavu/` (the `fonts-dejavu-core` package on Debian/Ubuntu).

The downloader keeps existing verified copies. Use `--ids S001,S003` to retry selected sources, or `--refresh` to replace a snapshot and its acquisition record. Commit the current edition before refreshing to retain it in Git history. An `acquisition_url` records an explicitly selected archival copy when the publisher URL is unavailable. Live-page snapshots remain dated observations.

## Scope and rights

This is an initial, sourced collection, not an official algorithm inventory or current deployment guide. Original notices remain with the source documents. No blanket license is applied to third-party material; repository-specific licensing has not been selected.
