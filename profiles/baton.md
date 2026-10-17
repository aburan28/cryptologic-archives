# BATON

A block-oriented cipher with structured key representation and token-controlled initialization.

### Documented statements

- **BATON-F1** — PKCS #11 encodes a BATON key value in 40 bytes and identifies 160 bits as checksum material. ([S001](../sources/README.md#s001), Section 2.9.2)
- **BATON-F2** — Named mechanisms include ECB128, ECB96, CBC128, COUNTER, SHUFFLE and WRAP; encryption-mode IV parameters are 24 bytes and token-selected. ([S001](../sources/README.md#s001), Sections 2.9.4-2.9.9)
- **BATON-F3** — NSA described BATON as supporting higher throughput than SKIPJACK with then-current microelectronics. ([S015](../sources/README.md#s015), Written question 6)

### Technical inferences

- **BATON-I1 · conditional** — If the checksum bits are determined by the remaining bits, this encoding contains at most 160 independent key bits: 320 minus 160. Basis: BATON-F1.
  Assumption: The checksum is deterministic from the remaining encoded key material.
- **BATON-I2 · strong** — The interface places encryption initialization policy inside the device. Basis: BATON-F2.

### Unresolved details

- The entropy bound is not a demonstrated cryptanalytic attack cost.
- The 192-bit IV parameter does not establish a 192-bit block size or internal state size.
