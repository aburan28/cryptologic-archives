# JUNIPER

A historical block-cipher interface closely resembling BATON at the API boundary.

### Documented statements

- **JUNIPER-F1** — JUNIPER has a 40-byte key representation containing 160 checksum bits, with ECB128, CBC128, counter, shuffle and wrapping mechanisms. ([S001](../sources/README.md#s001), Section 2.10)
- **JUNIPER-F2** — A public JUNIPER mechanism description appears in the December 1999 PKCS #11 standard. ([S002](../sources/README.md#s002), Section 12.23)

### Technical inferences

- **JUNIPER-I1 · moderate** — Shared key-format and mechanism conventions support reuse of integration infrastructure. Basis: JUNIPER-F1.

### Unresolved details

- A common API does not establish a common round function, key schedule or design ancestry.
