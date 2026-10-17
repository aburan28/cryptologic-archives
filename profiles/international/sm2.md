# SM2 family

SM2 names several related algorithms; the operation and protocol must be identified.

Region: China  
Role: Signatures, key exchange and public-key encryption  
Construction: Elliptic-curve cryptography  
Parameters: TLS profile uses a 256-bit prime-field curve

### Documented statements

- **INTL-SM2-F1** — The preserved parts separately describe general elliptic-curve operations, signatures, key exchange, public-key encryption and parameter definition. ([S029](../../sources/README.md#s029), Title and Scope; companion parts S030-S033; [S030](../../sources/README.md#s030), Title and Scope; companion parts S031-S033)
- **INTL-SM2-F2** — The signature algorithm hashes an identity-bound value with the message; its signing equations include r=(e+x1) mod n and s=(1+d)^(-1)*(k-r*d) mod n, with required retry conditions. ([S030](../../sources/README.md#s030), Sections 5.5 and 6.1)
- **INTL-SM2-F3** — RFC 8998 specifies a 256-bit prime-field curve and uses SM2 signatures with SM3. Its TLS key exchange is ECDHE over that curve. ([S026](../../sources/README.md#s026), Sections 1, 3.2.1 and 3.3)
- **INTL-SM2-F4** — OSCCA announced the GM/T SM2 family in March 2012. The official GB/T Part 1 record was issued in August 2016 and implemented in March 2017. ([S036](../../sources/README.md#s036), Publication and implementation metadata; [S034](../../sources/README.md#s034), Announcement list, GM/T0003-2012)

### Technical inferences

- **INTL-SM2-I1 · strong** — Using the SM2 curve for ECDHE in TLS does not by itself mean that the native SM2 Part 3 key-exchange protocol is being executed. Basis: INTL-SM2-F1, INTL-SM2-F3.

### Unresolved details

- The English Part 5 filename says 2016, whereas RFC 8998 cites GB/T 32918.5-2017. The filename must not be treated as authoritative edition metadata.
