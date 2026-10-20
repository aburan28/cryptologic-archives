# Research method

## Evidence categories

- **Documented:** what a specified source states, with its exact locator. Manufacturer statements remain manufacturer statements.
- **Strong inference:** a consequence supported by identified premises.
- **Conditional inference:** a consequence that depends on an explicit assumption, such as an advertised mode following its standard definition.
- **Moderate inference:** a plausible reading with competing explanations.
- **Unknown:** a detail that the cited records do not establish.

Every inference in the collection claim files (`data/claims.json`, `data/international-claims.json`, and `data/standards-claims.json`) names the premise claim IDs on which it depends. This makes it possible to revise a deduction when its evidence changes.

## Date semantics

Keep event date, document date, public-release date and retrieval time separate. A later public catalogue can establish the existence of an earlier dated specification; it does not make that specification publicly available in its original year. Fiscal years remain fiscal years. A platform certification does not establish the first approval date of every supported algorithm.

## Preservation

Preserve source bytes unchanged. Record publisher, host, original and resolved URLs, retrieval timestamp, content type, size and SHA-256. A mirror is labeled as a mirror or transcription. Failed retrievals remain visible in the source catalogue, with no fabricated copy or checksum. An HTML snapshot may depend on external resources and is not necessarily a complete offline rendering.

Original RFC text is retained where it is the publisher's source format. A digitized scan, edited transcription, English translation and original national-language standard are recorded as distinct kinds of evidence. Filenames and hosting-page dates do not establish a translation's edition or authorization. Missing pages and known discrepancies remain explicit.

A mirror may have added advertising links, watermarks or OCR before acquisition. Preserve those acquired bytes while identifying the host's additions; do not call such a copy an authenticated publisher original. A pinned Git revision identifies the mirror snapshot, not the issuing authority's approval. Assess completeness against contents and page sequences, and state the extent of inspection rather than treating a valid PDF header as proof of a complete document.

Retain earlier failed acquisition records when retrying. An HTTP 200 interstitial or a former PDF URL redirected to a current HTML page is not the requested historical document. Alternative editions are catalogued separately. The acquisition-attempt log records unresolved URLs and rejected responses without treating them as source evidence.

Successful retrieval does not mean a document is complete. The three-page GM/T 0009 booklet scan is an incomplete source, even though its acquired bytes are fully preserved. A revision announcement establishes the revisions and dates it actually lists; it does not supply the complete revised standard. Mutable publisher URLs identify a location, while the recorded hash and retrieval time identify the acquired edition.

Record an RFC's publication category and stream separately: IETF Informational, IRTF Informational and Informational Independent Submissions have different provenance. These labels describe publication status at issue. They do not establish national approval, implementation certification or current deployment suitability. Check explicit version references: a later standards wrapper can incorporate an earlier algorithm edition.

For older RFCs whose headers predate explicit stream labels, cite the preserved publisher index rather than infer a stream from “Network Working Group.” Record the original category, index publication status and index current status separately. An index snapshot is a dated metadata observation, not a complete errata or deployment-approval audit. Contradictory encoding definitions remain explicit specification questions until independent evidence resolves them.

## International context

Record design origin, standardization jurisdiction, service use and cryptanalytic source separately. British wartime analysis can be primary evidence about a German machine; an English RFC can describe a Russian standard without becoming its original Russian issuance. Regional labels do not imply exclusive use or a complete national inventory.

Treat public national standards, historical military systems and government products as separate evidence contexts. A government product may change algorithms while retaining its family name. Record system procurement, national standard issue, implementation date, RFC publication and approval withdrawal as different milestones.

## Boundaries of inference

Distinguish algorithms, modes, protocols, equipment personalities and product families. A shared API does not establish a shared round function. Encoded key length is not necessarily entropy or attack cost. A protocol identifier is not a key length. Throughput describes a particular implementation. An anticipated feature is not evidence of a shipped capability.

The archive does not treat aggregate lists or a codeword's presence alone as an original algorithm specification. Unknowns are retained as research questions rather than filled with guesses.
