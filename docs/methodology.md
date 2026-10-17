# Research method

## Evidence categories

- **Documented:** what a specified source states, with its exact locator. Manufacturer statements remain manufacturer statements.
- **Strong inference:** a consequence supported by identified premises.
- **Conditional inference:** a consequence that depends on an explicit assumption, such as an advertised mode following its standard definition.
- **Moderate inference:** a plausible reading with competing explanations.
- **Unknown:** a detail that the cited records do not establish.

Every inference in `data/claims.json` names the documented claim IDs on which it depends. This makes it possible to revise a deduction when its evidence changes.

## Date semantics

Keep event date, document date, public-release date and retrieval time separate. A later public catalogue can establish the existence of an earlier dated specification; it does not make that specification publicly available in its original year. Fiscal years remain fiscal years. A platform certification does not establish the first approval date of every supported algorithm.

## Preservation

Preserve source bytes unchanged. Record publisher, host, original and resolved URLs, retrieval timestamp, content type, size and SHA-256. A mirror is labeled as a mirror or transcription. Failed retrievals remain visible in the source catalogue, with no fabricated copy or checksum. An HTML snapshot may depend on external resources and is not necessarily a complete offline rendering.

## Boundaries of inference

Distinguish algorithms, modes, protocols, equipment personalities and product families. A shared API does not establish a shared round function. Encoded key length is not necessarily entropy or attack cost. A protocol identifier is not a key length. Throughput describes a particular implementation. An anticipated feature is not evidence of a shipped capability.

The archive does not treat aggregate lists or a codeword's presence alone as an original algorithm specification. Unknowns are retained as research questions rather than filled with guesses.
