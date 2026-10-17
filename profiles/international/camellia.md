# Camellia

A designer-published cipher from NTT and Mitsubishi Electric with early CRYPTREC records.

Region: Japan  
Role: Symmetric encryption  
Construction: Feistel network with FL/FLINV layers  
Parameters: 128-bit block; 128/192/256-bit keys; 18 or 24 rounds

### Documented statements

- **INTL-CAMELLIA-F1** — Camellia was jointly developed by NTT and Mitsubishi Electric. It has a 128-bit block and 128-, 192- and 256-bit key options. ([S043](../../sources/README.md#s043), Abstract and Section 1.1)
- **INTL-CAMELLIA-F2** — The data path has 18 rounds for 128-bit keys and 24 rounds for the larger keys, with FL and FLINV functions inserted every six rounds. ([S043](../../sources/README.md#s043), Sections 2.3 and 2.4)
- **INTL-CAMELLIA-F3** — The designer archive identifies a 12 July 2000 CRYPTREC specification and a 26 September 2001 version 2.0. The English RFC followed in April 2004. ([S047](../../sources/README.md#s047), Version 2.0 title and revision record; companion 2000 submission S052; [S052](../../sources/README.md#s052), 2000 designer submission; [S043](../../sources/README.md#s043), Header)

### Technical inferences

- **INTL-CAMELLIA-I1 · strong** — A 128-bit block interface with several key sizes does not imply AES internals: Camellia's specified data path is a Feistel construction with additional keyed layers. Basis: INTL-CAMELLIA-F1, INTL-CAMELLIA-F2.

### Unresolved details

- A submission, an algorithm publication and a national procurement approval are separate historical milestones.

[Companion standards: Japan: CRYPTREC selections and Camellia protocol profiles](../../docs/companion-standards.md#japan)
