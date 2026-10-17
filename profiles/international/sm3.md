# SM3

A public hash specification built from Boolean functions, word additions, rotations and message expansion.

Region: China  
Role: Cryptographic hashing  
Construction: Iterated word-oriented compression  
Parameters: 256-bit digest; 512-bit message blocks; 64 compression steps

### Documented statements

- **INTL-SM3-F1** — SM3 pads messages into 512-bit blocks and updates a 256-bit chaining value with a compression function. That function iterates j from 0 to 63. ([S028](../../sources/README.md#s028), Sections 5.1-5.3.3)
- **INTL-SM3-F2** — The compression state comprises eight 32-bit words, using specified Boolean functions, rotations, additions and permutations P0/P1. ([S028](../../sources/README.md#s028), Sections 3, 4 and 5.3.3)
- **INTL-SM3-F3** — OSCCA announced GM/T 0004-2012 for SM3 on 21 March 2012. RFC 8998 later specifies SM3 in its SM TLS 1.3 profile. ([S034](../../sources/README.md#s034), Announcement list, GM/T0004-2012; [S026](../../sources/README.md#s026), Sections 1.1 and 3.4)
- **INTL-SM3-F4** — The official announcement of 2010-12-17 released SM3 with an attached algorithm specification whose cover is dated December 2010, preceding the 2012 industry-standard announcement. ([S071](../../sources/README.md#s071), Announcement date and attachment link; [S098](../../sources/README.md#s098), Cover and Sections 4–5)

### Technical inferences

- **INTL-SM3-I1 · strong** — The concrete object is a digest computation, with message expansion and compression, rather than a bulk-encryption key schedule. Basis: INTL-SM3-F1, INTL-SM3-F2.

### Unresolved details

- A 256-bit digest length alone does not establish every security property or interoperability with other 256-bit hashes.

[Companion standards: China: original releases, parameters and successive standards](../../docs/companion-standards.md#shangmi)
