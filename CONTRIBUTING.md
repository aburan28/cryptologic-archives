# Contributing

Add the source record before adding claims. Prefer primary standards, manufacturer records, government documents and contemporary research. Include a page, section or table locator.

Separate a quotation or source-reported fact from your own inference. State assumptions and link the premise claim IDs. Keep unresolved alternatives visible. Do not replace a historical date with a file download or search-crawl date.

Preserve original files unchanged and retain their notices. Run `python scripts/build_report.py`, `python scripts/build_international.py` and `python scripts/validate_archive.py` after changing the data. The generated report and profile pages should agree with the structured records.

International profiles and timeline events live in `data/international.json`; their normalized claims are generated in `data/international-claims.json`. Add source collection, region, language and translation/transcription provenance. Identify a profile's role before comparing key sizes, block sizes or dates across countries.

Useful next acquisitions include original first-approval records, contemporary SAVILLE design history, and independently dated implementation records for less documented names. An acquisition request should identify the exact record sought and the question it would resolve.
