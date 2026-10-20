# SNOW 3G

An explicitly specified generator with separately preserved UEA2/UIA2 algorithms, tests and design rationale.

Region: International mobile standards  
Role: Keystream generation for confidentiality and integrity constructions  
Construction: 16-word LFSR and three-register nonlinear finite-state machine  
Parameters: 128-bit key; 128-bit IV; 32-bit output words

### Documented statements

- **INTL-SNOW3G-F1** — The generator produces 32-bit keystream words from a 128-bit key and IV and combines a 16-word LFSR with a three-register FSM. ([S131](../../sources/README.md#s131), Sections 2.1, 3.2 and 3.3)
- **INTL-SNOW3G-F2** — The design report traces SNOW 3G to SNOW 2.0 and specifies the reasoning for changing the nonlinear/FSM components. This is documented design history rather than an inference from a shared name. ([S134](../../sources/README.md#s134), Sections 8.1.2–8.3)
- **INTL-SNOW3G-F3** — Document 2 v1.1 is dated 2006-09-06; Document 1 v2.1 is dated 2009-03-16; Document 3 v1.1 is dated 2012-10-25. They describe different layers and have separate histories. ([S131](../../sources/README.md#s131), Cover and Document History; [S132](../../sources/README.md#s132), Cover and Document History; [S133](../../sources/README.md#s133), Cover and Document History)

### Technical inferences

- **INTL-SNOW3G-I1 · conditional** — A comparison with ZUC should distinguish generator architecture from the surrounding packet confidentiality/integrity algorithms; the public specifications expose both layers. Basis: INTL-SNOW3G-F1, INTL-SNOW3G-F3, INTL-ZUC-F1, INTL-ZUC-F2.
  Assumption: The comparison concerns the preserved 128-bit-key generator families, not an unpreserved later variant.

### Unresolved details

- The 2006 evaluation does not establish immunity to later attacks, and packet-algorithm conformance is not established solely by generator test vectors.

[Companion standards: International mobile standards: SNOW 3G, UEA2 and UIA2](../../docs/companion-standards.md#mobile-snow)
