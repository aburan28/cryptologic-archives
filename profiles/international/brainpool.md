# Brainpool elliptic curves

Published curve parameters are distinguished from the signature, agreement and transport protocols that use them.

Region: Germany / international  
Role: Elliptic-curve domain parameters  
Construction: Prime-field elliptic curves and specified parameter-generation procedures  
Parameters: Named r1/t1 curves at 160, 192, 224, 256, 320, 384 and 512 bits in RFC 5639

### Documented statements

- **INTL-BRAINPOOL-F1** — RFC 5639 gives prime-field curve parameter sets, requirements, OIDs and generation procedures. Its listed field sizes range from 160 to 512 bits. ([S123](../../sources/README.md#s123), Sections 2–4; Appendix A)
- **INTL-BRAINPOOL-F2** — RFC 8734 defines separate Brainpool groups and signature scheme identifiers for TLS 1.3. Both RFCs are Informational Independent Submissions. ([S124](../../sources/README.md#s124), Header; Sections 2–3; [S123](../../sources/README.md#s123), Header)
- **INTL-BRAINPOOL-F3** — BSI TR-03111 separately specifies signature, key-agreement and encoding operations. ANSSI’s 2021 selection guide lists selected Brainpool curves, which is a different kind of evidence from the original curve definition. ([S125](../../sources/README.md#s125), Sections 4.2–4.4 and 5; [S130](../../sources/README.md#s130), Section 5.3, printed pp.31–32 / PDF pp.33–34)

### Technical inferences

- **INTL-BRAINPOOL-I1 · conditional** — Sharing a curve does not imply sharing a signature scheme, key-agreement protocol or encoding; these are independent choices in the preserved records. Basis: INTL-BRAINPOOL-F1, INTL-BRAINPOOL-F2, INTL-BRAINPOOL-F3.
  Assumption: The implementations use a named Brainpool domain parameter set through the cited schemes.

### Unresolved details

- Listing a curve in the 2010 parameter document is not a present-day recommendation for every listed size or evidence of classified product approval.

[Companion standards: Germany: ECC constructions, Brainpool and protocol guidance](../../docs/companion-standards.md#germany)

[Companion standards: France: ANSSI selection and mechanism rules](../../docs/companion-standards.md#france)
