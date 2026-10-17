# Magma

The updated 64-bit cipher in GOST R 34.12-2015, with important compatibility details.

Region: Russia  
Role: Symmetric encryption  
Construction: Feistel block cipher  
Parameters: 64-bit block; 256-bit key; 32 round keys

### Documented statements

- **INTL-MAGMA-F1** — Magma uses a 64-bit block and 256-bit key; its specified encryption composition uses 32 round keys. ([S021](../../sources/README.md#s021), Abstract; Sections 4.2, 4.3 and 5.1)
- **INTL-MAGMA-F2** — Relative to GOST 28147-89, the RFC fixes the S-box set and changes key/block parsing conventions, including big-endian key parsing. ([S021](../../sources/README.md#s021), Appendix B, Background)
- **INTL-MAGMA-F3** — Its national-standard edition is 2015; RFC 8891 was published in September 2020. ([S021](../../sources/README.md#s021), Header, Introduction and normative reference GOSTR3412-2015)

### Technical inferences

- **INTL-MAGMA-I1 · strong** — Replacing a legacy GOST implementation by changing its displayed algorithm name is insufficient: representation and parameter choices can change ciphertext. Basis: INTL-MAGMA-F1, INTL-MAGMA-F2.

### Unresolved details

- The 2020 RFC date is an English-publication milestone, not the cipher invention date.
