# MEDLEY

A symmetric encryption primitive exposed through familiar block-cipher modes.

### Documented statements

- **MEDLEY-F1** — Viasat advertises MEDLEY-256 with GCM, CTR, OFB and CFB. ([S005](../sources/README.md#s005), Multiple-mission capable > KG-42 ECM)
- **MEDLEY-F2** — Standard GCM uses a 128-bit block cipher and does not use its inverse function. ([S003](../sources/README.md#s003), Section 5.1)
- **MEDLEY-F3** — The NGLD-M requirements list MEDLEY for data-at-rest and non-security software confidentiality. ([S010](../sources/README.md#s010), Table 9, printed p.42; PDF p.48)

### Technical inferences

- **MEDLEY-I1 · conditional** — The advertised GCM profile implies a keyed 128-bit block permutation interface. Basis: MEDLEY-F1, MEDLEY-F2.
  Assumption: GCM denotes the standard NIST mode.
- **MEDLEY-I2 · conditional** — The advertised modes can process message encryption and decryption using only the forward block-cipher function. Basis: MEDLEY-F1, MEDLEY-F2.
  Assumption: The modes follow their standard definitions; see S004 sections 6.3-6.5.
- **MEDLEY-I3 · moderate** — The -256 designation suggests a 256-bit key variant, but does not by itself establish entropy or attack cost. Basis: MEDLEY-F1.

### Unresolved details

- Round function, key schedule and relationship to AES are not established by these records.
- The original 2001 mode set need not equal the later advertised mode set.
