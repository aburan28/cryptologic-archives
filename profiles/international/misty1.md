# MISTY1

A designer-authored public specification with explicit nonlinear functions, S-boxes and test data.

Region: Japan  
Role: Symmetric encryption  
Construction: Nested Feistel construction with FL, FO and FI functions  
Parameters: 64-bit block; 128-bit key; eight-round configuration recommended in RFC 2994

### Documented statements

- **INTL-MISTY1-F1** — RFC 2994 describes a 64-bit block cipher with a 128-bit key and variable round count, recommending eight rounds. Its FI function uses 7-bit and 9-bit S-boxes; FO and FL and the key schedule are explicitly described. ([S118](../../sources/README.md#s118), Sections 1, 2.2 and 2.3)
- **INTL-MISTY1-F2** — The preserved designer-authored RFC is dated November 2000 and cites Matsui’s FSE 1997 MISTY publication. The RFC is Informational; the publisher index labels its stream Legacy. ([S118](../../sources/README.md#s118), Header; Section 6 reference [1]; [S100](../../sources/README.md#s100), RFC2994 entry)

### Technical inferences

- **INTL-MISTY1-I1 · conditional** — A reported eight-round MISTY1 implementation can be compared with the published S-boxes, schedule and example data, rather than characterized only by its name or key length. Basis: INTL-MISTY1-F1.
  Assumption: The implementation claims the RFC’s specified eight-round configuration.

### Unresolved details

- A 1997 publication citation and a 2000 RFC are not first governmental approval records. A present-day security recommendation is outside this historical profile.

[Companion standards: Japan: selection lists, additional primitives and Camellia profiles](../../docs/companion-standards.md#japan)
