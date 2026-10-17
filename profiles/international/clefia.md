# CLEFIA

Sony's published cipher gives an explicit alternative to a two-branch Feistel network.

Region: Japan  
Role: Symmetric encryption  
Construction: Four-branch generalized Feistel network  
Parameters: 128-bit block; 128/192/256-bit keys; 18/22/26 rounds

### Documented statements

- **INTL-CLEFIA-F1** — Sony's version 1.0 specification is dated 1 June 2007. It uses four 32-bit data branches and 18, 22 or 26 rounds for the three key sizes. ([S049](../../sources/README.md#s049), Cover; Sections 1 and 4.2)
- **INTL-CLEFIA-F2** — The data-processing part uses a four-branch generalized Feistel network; an eight-branch construction also appears in scheduling larger keys. ([S044](../../sources/README.md#s044), Section 4)
- **INTL-CLEFIA-F3** — The English RFC specification was published in March 2011 and dates the algorithm's public publication to 2007. ([S044](../../sources/README.md#s044), Header and Introduction)

### Technical inferences

- **INTL-CLEFIA-I1 · strong** — The four-branch structure is a concrete design distinction, despite sharing a 128-bit block interface and key-size choices with several other ciphers. Basis: INTL-CLEFIA-F1, INTL-CLEFIA-F2.

### Unresolved details

- The preserved design dates do not establish when every Sony product first deployed CLEFIA.

[Companion standards: Japan: CRYPTREC selections and Camellia protocol profiles](../../docs/companion-standards.md#japan)
