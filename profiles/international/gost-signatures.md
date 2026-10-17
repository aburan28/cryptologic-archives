# GOST R 34.10-2012

The GOST signature standard is a separate mathematical object from GOST block ciphers.

Region: Russia  
Role: Digital signatures  
Construction: Elliptic-curve discrete-logarithm scheme  
Parameters: Prime-field elliptic curves; 512- or 1024-bit encoded signatures

### Documented statements

- **INTL-GOST-SIGNATURES-F1** — The standard defines signing and verification using an elliptic-curve point group over a prime finite field. It specifies signature encodings of 512 or 1024 bits. ([S024](../../sources/README.md#s024), Sections 1.2, 4 and 5)
- **INTL-GOST-SIGNATURES-F2** — The signing rule uses an ephemeral scalar k, point C=kP, r=x_C mod q, and s=(r*d+k*e) mod q, with the specified hash-to-integer and retry rules. ([S024](../../sources/README.md#s024), Section 6.1)
- **INTL-GOST-SIGNATURES-F3** — The standard edition is 2012 and the English RFC is dated December 2013. ([S024](../../sources/README.md#s024), Header and Section 1.1)

### Technical inferences

- **INTL-GOST-SIGNATURES-I1 · strong** — GOST can name an ecosystem containing signatures, hashes and ciphers. A signature length alone cannot identify the block cipher used by a product. Basis: INTL-GOST-SIGNATURES-F1, INTL-GOST-SIGNATURES-F2.

### Unresolved details

- A product profile must additionally identify curve parameters, hash function and encoding conventions.
