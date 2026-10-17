# SM4 / SMS4

A public block cipher whose earlier name SMS4 and later standard numbers describe different historical milestones.

Region: China  
Role: Symmetric encryption  
Construction: Unbalanced Feistel-style word transformation  
Parameters: 128-bit block; 128-bit key; 32 rounds

### Documented statements

- **INTL-SM4-F1** — The published transformation uses four 32-bit state words, 32 rounds, byte S-box substitution and a linear layer built from XOR and rotations. Both block and key are 128 bits. ([S027](../../sources/README.md#s027), Sections 4, 6 and 7)
- **INTL-SM4-F2** — In compact notation, the update is X[i+4]=X[i] XOR T(X[i+1] XOR X[i+2] XOR X[i+3] XOR rk[i]); output reverses the final four words. ([S027](../../sources/README.md#s027), Sections 6.1 and 7.1)
- **INTL-SM4-F3** — Diffie and Ledin's dated May 2008 translation reports that SMS4 was issued in January 2006. OSCCA explicitly identified SM4 as formerly SMS4 in its March 2012 announcement. ([S053](../../sources/README.md#s053), Cover and introductory paragraph; [S034](../../sources/README.md#s034), Announcement list, GM/T0002-2012)
- **INTL-SM4-F4** — The official national record gives GB/T 32907-2016 an issue date of 29 August 2016 and an implementation date of 1 March 2017. ([S035](../../sources/README.md#s035), Publication and implementation metadata)

### Technical inferences

- **INTL-SM4-I1 · strong** — A protocol entry such as SM4-GCM identifies a block cipher plus a mode. Its authentication and nonce rules belong to the full protocol profile, rather than to the SM4 round function alone. Basis: INTL-SM4-F1, INTL-SM4-F2.

### Unresolved details

- The hosted English translation lacks an official dated Chinese cover; its edition is not established by its filename.

[Companion standards: China: original releases, parameters and successive standards](../../docs/companion-standards.md#shangmi)
