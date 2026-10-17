# SEED

A Korean national cipher with a public description of its round structure.

Region: Republic of Korea  
Role: Symmetric encryption  
Construction: 16-round Feistel network  
Parameters: 128-bit block; 128-bit key

### Documented statements

- **INTL-SEED-F1** — RFC 4269 describes SEED as developed by KISA since 1998 and as a Korean national standard. It specifies a 128-bit block, a 128-bit key and 16 Feistel rounds. ([S045](../../sources/README.md#s045), Section 1.2)
- **INTL-SEED-F2** — The public round description includes S-box transformations, permutations, XOR and addition, with an explicit key schedule and test data. ([S045](../../sources/README.md#s045), Sections 2 and 3; appendices)
- **INTL-SEED-F3** — The preserved RFC is dated December 2005 and replaces the earlier RFC 4009 description. ([S045](../../sources/README.md#s045), Header and Abstract)

### Technical inferences

- **INTL-SEED-I1 · strong** — SEED provides an example where both the primitive's structure and development period can be stated from a published specification, while product certification remains a separate question. Basis: INTL-SEED-F1, INTL-SEED-F2.

### Unresolved details

- This profile concerns the 128-bit SEED specification in RFC 4269, not every later similarly named variant.

[Companion standards: Republic of Korea: SEED and ARIA protocol profiles](../../docs/companion-standards.md#korea)
