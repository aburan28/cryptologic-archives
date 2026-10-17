# Cryptologic Archives

A historical research archive of public cryptologic records, original documents, and technical inferences from multiple countries. Collections cover NSA Suite A and Soviet/Russian, Chinese, German, Japanese and Korean cryptography.

## Start here

- [International research report](docs/international-cryptography.md) and [PDF edition](reports/international-cryptography.pdf)
- [International profiles](profiles/international/README.md) and [historical timeline](docs/international-timeline.md)
- [NSA Suite A report](docs/suite-a-research.md) and [PDF edition](reports/suite-a-research.pdf)
- [Algorithm profiles](profiles/README.md)
- [Additional codeword and scheme index](docs/name-index.md)
- [NSA Suite A historical timeline](docs/timeline.md)
- [Source catalogue and preservation status](sources/README.md)
- [Research method](docs/methodology.md)
- [Suite A claims](data/claims.json), [international claims](data/international-claims.json), [sources](data/sources.json), and [international profiles and timeline](data/international.json)

## What the archive records

Each profile separates documented statements, technical inferences with assumptions, and unresolved questions. Dates distinguish program history, specifications, public documentation, requirements, and certification of a particular implementation. A date is not labeled the first appearance or first approval without evidence for that claim.

Original source files, including PDFs and publisher-supplied RFC text, are stored in `sources/originals/`; raw web snapshots are stored in `sources/web/`. The catalogue records retrieval time, resolved URL, file size and SHA-256 for preserved copies. A preserved file's hash confirms byte identity, not its truth, authenticity or release authorization.

The international collection includes GOST 28147-89, Magma, Kuznyechik, Streebog, GOST signatures, Fialka, SM2, SM3, SM4, ZUC, Enigma, Lorenz/Tunny, CHIASMUS, LIBELLE/SINA, Camellia, CLEFIA, SEED and ARIA. Regional labels describe design or historical context. Each profile identifies the operation and type of evidence rather than treating all national standards as equivalents of Suite A.

## Reproduce and check

```sh
python -m pip install -r requirements.txt
python scripts/fetch_sources.py
python scripts/build_report.py
python scripts/build_international.py
python scripts/validate_archive.py
```

Use Python 3.9 or later. The PDF builder uses DejaVu Sans fonts from `/usr/share/fonts/truetype/dejavu/` (the `fonts-dejavu-core` package on Debian/Ubuntu).

The downloader keeps existing verified copies. Use `--ids S001,S003` to retry selected sources, or `--refresh` to replace a snapshot and its acquisition record. Commit the current edition before refreshing to retain it in Git history. An `acquisition_url` records an explicitly selected archival copy when the publisher URL is unavailable. Live-page snapshots remain dated observations.

## Scope and rights

This is an expanding research archive, not an official algorithm inventory or current deployment guide. Original notices remain with the source documents. No blanket license is applied to third-party material; repository-specific licensing has not been selected.
