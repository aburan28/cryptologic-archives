# CHIASMUS

A German government example where public lifecycle evidence is clearer than the primitive's internals.

Region: Germany  
Role: Government file encryption and historical SINA use  
Construction: Proprietary symmetric-encryption system; internal construction unresolved here  
Parameters: Key material and format are product-specific in the cited agency account

### Documented statements

- **INTL-CHIASMUS-F1** — BSI dates the Windows Chiasmus file-encryption program to 2001, followed by a Linux command-line version. Partners had to exchange secret key material beforehand. ([S042](../../sources/README.md#s042), Section 1, printed p.4)
- **INTL-CHIASMUS-F2** — BSI describes non-open algorithms and standards and proprietary software; it says Chiasmus key material is incompatible with replacement products. ([S042](../../sources/README.md#s042), Section 1, printed p.4)
- **INTL-CHIASMUS-F3** — BSI states that the VS-NfD approval was withdrawn on 30 June 2022. Its SINA history separately records replacing CHIASMUS by AES at lower classification levels. ([S042](../../sources/README.md#s042), Section 1, printed p.4; [S041](../../sources/README.md#s041), Cryptographic migration paragraph)

### Technical inferences

- **INTL-CHIASMUS-I1 · strong** — A file archive or migration tool needs the actual container, key format and implementation behavior; merely selecting another symmetric cipher cannot make a Chiasmus file readable. Basis: INTL-CHIASMUS-F1, INTL-CHIASMUS-F2.

### Unresolved details

- The cited agency records do not expose a complete round function or establish the cipher's original design date.
- Independent reverse engineering should be catalogued separately from an official design release.

[Companion standards: Germany: ECC constructions, Brainpool and protocol guidance](../../docs/companion-standards.md#germany)
