# KCipher-2

A public Japanese stream-cipher specification distinct from the block-cipher families in the archive.

Region: Japan  
Role: Keystream generation  
Construction: Word-oriented stream cipher with feedback registers and nonlinear operations  
Parameters: 128-bit key; 128-bit IV; 32-bit state words

### Documented statements

- **INTL-KCIPHER2-F1** — RFC 7008 specifies a 128-bit key and 128-bit IV, state registers, feedback shifts, nonlinear functions and keystream generation. It includes sample implementation code and test vectors. ([S119](../../sources/README.md#s119), Abstract; Sections 2.2–2.5; Appendices B–C)
- **INTL-KCIPHER2-F2** — The RFC was published in August 2013 as an Informational Independent Submission. It reports that KCipher-2 was published in 2007; this is a source-reported historical statement, not an original approval record. ([S119](../../sources/README.md#s119), Header; Abstract; Status of This Memo)

### Technical inferences

- **INTL-KCIPHER2-I1 · conditional** — The 128-bit IV does not make the primitive a 128-bit block cipher; its specified interface produces a keystream from word-oriented state. Basis: INTL-KCIPHER2-F1.
  Assumption: The name refers to the generator specified in RFC 7008.

### Unresolved details

- The RFC’s historical security statements describe its publication context and are not treated as a current cryptanalytic guarantee.

[Companion standards: Japan: selection lists, additional primitives and Camellia profiles](../../docs/companion-standards.md#japan)
