# Streebog / GOST R 34.11-2012

A hash-function standard, with a fully specified compression construction.

Region: Russia  
Role: Cryptographic hashing  
Construction: Iterated compression with substitution, permutation and linear transforms  
Parameters: 256- or 512-bit digest; 512-bit chaining state

### Documented statements

- **INTL-STREEBOG-F1** — GOST R 34.11-2012 defines 256-bit and 512-bit digest variants. Both use a 512-bit chaining state and specified S, P and L transformations. ([S023](../../sources/README.md#s023), Sections 5-9)
- **INTL-STREEBOG-F2** — The compression function combines a keyed internal transformation with the previous chaining value and message block by XOR; finalization also processes message length and a block sum. ([S023](../../sources/README.md#s023), Sections 8 and 9)
- **INTL-STREEBOG-F3** — The standard edition is 2012; the preserved English publication is RFC 6986 of August 2013. ([S023](../../sources/README.md#s023), Header and normative reference GOST3411-2012)

### Technical inferences

- **INTL-STREEBOG-I1 · strong** — A 256-bit digest is an output length. It is not a 256-bit encryption key, and a hash interface does not provide a decryption operation. Basis: INTL-STREEBOG-F1, INTL-STREEBOG-F2.

### Unresolved details

- This profile records the specified construction, not a complete survey of subsequent cryptanalysis.
