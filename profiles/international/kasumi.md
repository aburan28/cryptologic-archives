# KASUMI

The preserved Release 17 specification exposes the cipher core and distinguishes it from the complete confidentiality and integrity algorithms.

Region: International mobile standards / Japanese design context  
Role: Symmetric encryption primitive for cellular algorithms  
Construction: Eight-round Feistel cipher with FL, FO and FI functions  
Parameters: 64-bit block; 128-bit key; eight rounds

### Documented statements

- **INTL-KASUMI-F1** — KASUMI has a 64-bit data block, a 128-bit key and eight Feistel rounds. Its FI function uses 7-bit and 9-bit S-boxes, and the specification gives round-key derivation and tables. ([S120](../../sources/README.md#s120), Sections 3 and 4.1–4.6)
- **INTL-KASUMI-F2** — The archived PDF is ETSI TS 135 202 V17.0.0 dated April 2022, incorporating 3GPP TS 35.202 Release 17. It specifies KASUMI as the component used by f8 and f9, rather than the complete algorithms. ([S120](../../sources/README.md#s120), Cover; Section 0 Scope)
- **INTL-KASUMI-F3** — 3GPP’s December 2002 design report identifies KASUMI as a modification of MISTY1 and describes separate data-path and key-schedule changes. The preserved report is explicitly a development copy not approved by the Organizational Partners. ([S139](../../sources/README.md#s139), Cover; Sections 9.2–9.3, printed/PDF pp.14–15)

### Technical inferences

- **INTL-KASUMI-I1 · conditional** — The core cipher’s block/key sizes are insufficient to specify a cellular packet-protection operation; the f8/f9 construction and input handling also matter. Basis: INTL-KASUMI-F1, INTL-KASUMI-F2.
  Assumption: The implementation uses KASUMI through a cellular confidentiality or integrity algorithm.

### Unresolved details

- This later standards edition does not establish KASUMI’s original invention or first approval date. Similar function names in MISTY1 do not establish interchangeability.

[Companion standards: Japan: selection lists, additional primitives and Camellia profiles](../../docs/companion-standards.md#japan)
