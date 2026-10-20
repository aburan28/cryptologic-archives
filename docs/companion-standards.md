# Companion standards: from primitives to implementations

Research snapshot: 2026-10-20

This collection links the archive’s algorithm profiles to the surrounding specifications: modes, parameters, key formats, protocol profiles, selection lists and validation records. It preserves particular editions and their dates rather than claiming to hold every standard or the latest version of every document.

An algorithm release, a national-standard issue, an effective date, an RFC publication and a product certificate describe different events. A protocol profile can expose exact mathematical and wire-format choices while leaving deployment and implementation approval unresolved.

The original files remain unchanged. Documented statements have source locators; deductions identify their premises and assumptions. Acquisition failures and incomplete copies are listed alongside successful preservation.

The 2026-10-20 continuation adds Russian national-language modes and correction records, complete-body Chinese companion scans, Japanese and Korean protocol records, German ECC/Brainpool material, French ANSSI guides, international mobile specifications, and Swiss/Swedish historical records. The original 2010 SM2/SM3 releases remain the earlier preserved editions.

This guide maps **10 families**, **77 claims** and **40 dated milestones** to 92 source records. 89 copies are preserved, including 40 additions since the 2026-10-17 baseline. Three KISA pages remain acquisition gaps after a 2026-10-20 retry.

[PDF edition](../reports/companion-standards.pdf) · [Source catalogue](../sources/README.md) · [Structured research](../data/standards.json) · [Normalized claims](../data/standards-claims.json)

## Read the layers

| Layer | Question | Examples | Evidence |
|---|---|---|---|
| Primitive | What mathematical transformation is specified? | SM2 point arithmetic; SM3 compression; Magma and Kuznyechik block transformations. | [S096](../sources/README.md#s096), [S098](../sources/README.md#s098), [S037](../sources/README.md#s037) |
| Mode and parameters | How are messages, nonces, tags, curves and keys selected? | GCM, CCM, CMAC, MGM; concrete SM2 and GOST curve parameters. | [S003](../sources/README.md#s003), [S057](../sources/README.md#s057), [S059](../sources/README.md#s059), [S067](../sources/README.md#s067), [S068](../sources/README.md#s068), [S097](../sources/README.md#s097) |
| API and encoding | How does software represent and invoke the operation? | PKCS #11 objects and mechanisms; X.509 identifiers, public keys and signatures. | [S001](../sources/README.md#s001), [S061](../sources/README.md#s061), [S064](../sources/README.md#s064), [S066](../sources/README.md#s066) |
| Protocol profile | How do peers negotiate and combine the parts? | TLS, IPsec/IKEv2, SRTP, and cellular EEA3/EIA3. | [S026](../sources/README.md#s026), [S060](../sources/README.md#s060), [S062](../sources/README.md#s062), [S063](../sources/README.md#s063), [S065](../sources/README.md#s065), [S076](../sources/README.md#s076), [S091](../sources/README.md#s091) |
| Selection and policy | Which algorithms and lifetimes does a dated policy recommend? | CRYPTREC list categories and BSI TR-02102 recommendations. | [S078](../sources/README.md#s078), [S079](../sources/README.md#s079), [S080](../sources/README.md#s080), [S081](../sources/README.md#s081) |
| Implementation evaluation | What evidence concerns a particular implementation or evaluation? | Known-answer tests, design evaluation reports, and separately dated product certificates. | [S092](../sources/README.md#s092), [S093](../sources/README.md#s093) |

A recommendation list can name a primitive and a mode while leaving the protocol unspecified. A product certificate requires its own version, scope and approval record. An interface can reveal block sizes or encodings even when an algorithm’s internal construction remains unpublished.

## Reading map

| Family | Companion records | What the records resolve |
|---|---|---|
| [Common modes, formats and Suite A interfaces](#interfaces) | [S001](../sources/README.md#s001), [S003](../sources/README.md#s003), [S004](../sources/README.md#s004), [S064](../sources/README.md#s064), [S065](../sources/README.md#s065), [S066](../sources/README.md#s066), [S067](../sources/README.md#s067), [S068](../sources/README.md#s068), [S069](../sources/README.md#s069), [S100](../sources/README.md#s100), [S126](../sources/README.md#s126), [S127](../sources/README.md#s127) | Read the primitive or mechanism interface, then the mode definition, then the protocol that uses it. The PKCS #11 Base and Historical Mechanisms copies deliberately share the v3.0 publication date. |
| [Russia: GOST parameters, modes and protocol bindings](#gost) | [S050](../sources/README.md#s050), [S057](../sources/README.md#s057), [S058](../sources/README.md#s058), [S059](../sources/README.md#s059), [S060](../sources/README.md#s060), [S061](../sources/README.md#s061), [S062](../sources/README.md#s062), [S063](../sources/README.md#s063), [S064](../sources/README.md#s064), [S065](../sources/README.md#s065), [S101](../sources/README.md#s101), [S102](../sources/README.md#s102), [S103](../sources/README.md#s103), [S104](../sources/README.md#s104), [S105](../sources/README.md#s105), [S106](../sources/README.md#s106), [S107](../sources/README.md#s107), [S108](../sources/README.md#s108) | Start with the Russian modes text, official registration record, separate 2018 correction and per-key data-volume recommendation. Then choose the algorithm generation, parameter/KDF documents, certificate or PFX encoding, and the required TLS/IPsec/CMS profile. RFC 9337’s integer-counter notation is an explicit unresolved compatibility question. |
| [China: original releases, parameters and successive standards](#shangmi) | [S026](../sources/README.md#s026), [S034](../sources/README.md#s034), [S035](../sources/README.md#s035), [S036](../sources/README.md#s036), [S070](../sources/README.md#s070), [S071](../sources/README.md#s071), [S072](../sources/README.md#s072), [S073](../sources/README.md#s073), [S074](../sources/README.md#s074), [S096](../sources/README.md#s096), [S097](../sources/README.md#s097), [S098](../sources/README.md#s098), [S109](../sources/README.md#s109), [S110](../sources/README.md#s110), [S111](../sources/README.md#s111), [S112](../sources/README.md#s112), [S113](../sources/README.md#s113), [S114](../sources/README.md#s114) | Read the original 2010 release and curve sheet, then the acquired 2012 application/message/certificate/token standards and historical 2014 SSL VPN specification. S109 fills the missing GM/T 0009 body pages. Compare each with its exact later revision and the separate RFC 8998 TLS 1.3 profile. |
| [China and 3GPP: ZUC, EEA3 and EIA3](#zuc) | [S037](../sources/README.md#s037), [S075](../sources/README.md#s075), [S076](../sources/README.md#s076), [S092](../sources/README.md#s092), [S093](../sources/README.md#s093) | Read ZUC Document 2 for the keystream generator, Document 1 for the EEA3/EIA3 packet algorithms, Document 3 for implementer test data and Document 4 for design/evaluation history. The Release 19 ETSI wrapper records the later standards context. |
| [Japan: selection lists, additional primitives and Camellia profiles](#japan) | [S077](../sources/README.md#s077), [S078](../sources/README.md#s078), [S079](../sources/README.md#s079), [S080](../sources/README.md#s080), [S086](../sources/README.md#s086), [S087](../sources/README.md#s087), [S094](../sources/README.md#s094), [S115](../sources/README.md#s115), [S116](../sources/README.md#s116), [S117](../sources/README.md#s117), [S118](../sources/README.md#s118), [S119](../sources/README.md#s119), [S120](../sources/README.md#s120), [S139](../sources/README.md#s139) | Compare dated CRYPTREC selections with the primitive specification. Camellia’s mode/test-vector, IPsec and TLS documents have different RFC categories. MISTY1, KCipher-2 and KASUMI are separately specified primitives; a later RFC or standards wrapper does not date their invention. |
| [Republic of Korea: SEED and ARIA protocol profiles](#korea) | [S084](../sources/README.md#s084), [S085](../sources/README.md#s085), [S088](../sources/README.md#s088), [S089](../sources/README.md#s089), [S090](../sources/README.md#s090), [S091](../sources/README.md#s091), [S099](../sources/README.md#s099), [S121](../sources/README.md#s121), [S122](../sources/README.md#s122) | Use the existing SEED and ARIA primitive specifications, then the TLS and IPsec/SRTP bindings as relevant. The KCMVP programme pages are acquisition leads only until their original bytes can be preserved. |
| [Germany: ECC constructions, Brainpool and protocol guidance](#germany) | [S081](../sources/README.md#s081), [S082](../sources/README.md#s082), [S083](../sources/README.md#s083), [S095](../sources/README.md#s095), [S123](../sources/README.md#s123), [S124](../sources/README.md#s124), [S125](../sources/README.md#s125) | Read TR-03111 for concrete signature/key-agreement operations and encodings, RFC 5639 for Brainpool parameters and RFC 8734 for its TLS 1.3 binding. TR-02102 supplies the separately dated recommendation and protocol context. |
| [France: ANSSI selection and mechanism rules](#france) | [S128](../sources/README.md#s128), [S129](../sources/README.md#s129), [S130](../sources/README.md#s130), [S123](../sources/README.md#s123), [S126](../sources/README.md#s126), [S127](../sources/README.md#s127) | Read the distribution-page snapshot, then the exact cover and history of each guide. The rules PDF is version 3.00 of March 2026; the selection guide is version 1.0 of March 2021. Use cited specifications for the actual algorithm and encoding. |
| [International mobile standards: SNOW 3G, UEA2 and UIA2](#mobile-snow) | [S131](../sources/README.md#s131), [S132](../sources/README.md#s132), [S133](../sources/README.md#s133), [S134](../sources/README.md#s134), [S135](../sources/README.md#s135) | Read Document 2 for the generator, Document 1 for packet confidentiality/integrity, Document 3 for tests and Document 5 for design history. The GSMA distribution index records the provenance of these copies. |
| [Swiss and Swedish historical machine records](#historical-archives) | [S136](../sources/README.md#s136), [S137](../sources/README.md#s137), [S138](../sources/README.md#s138) | Start with the original bilingual NEMA instructions and their cover stamp. For Siemens T52, separate FRA’s retrospective institutional history from Borelius’s explicitly hypothetical reconstruction of Beurling’s working method. |

<a id="interfaces"></a>

## Common modes, formats and Suite A interfaces

Existing profiles: [MEDLEY](../profiles/medley.md), [BATON](../profiles/baton.md), [JUNIPER](../profiles/juniper.md), [ACCORDION](../profiles/accordion.md).

Read the primitive or mechanism interface, then the mode definition, then the protocol that uses it. The PKCS #11 Base and Historical Mechanisms copies deliberately share the v3.0 publication date.

**Scope limit:** A public API can constrain roles, sizes and representation without publishing a classified round function. Generic NIST modes do not establish NSA approval of a named Suite A algorithm.

### Documented statements

- **STD-COM-F1** — SP 800-38A specifies ECB, CBC, CFB, OFB and CTR confidentiality modes; SP 800-38D specifies GCM and GMAC and requires a 128-bit block cipher for GCM. ([S004](../sources/README.md#s004), Abstract; Sections 6.1–6.5; [S003](../sources/README.md#s003), Section 5.1)
- **STD-COM-F2** — CMAC supplies message authentication, CCM combines counter-mode encryption with CBC-MAC, and SP 800-38F specifies methods for cryptographic key wrapping. These documents address distinct operations. ([S067](../sources/README.md#s067), Abstract; Section 6; [S068](../sources/README.md#s068), Abstract; Section 6; [S069](../sources/README.md#s069), Abstract; Sections 1 and 4)
- **STD-COM-F3** — The preserved PKCS #11 Base and Historical Mechanisms specifications are both OASIS v3.0 standards dated 2020-06-15. The base API and historical mechanism descriptions are separate companion documents. ([S066](../sources/README.md#s066), Cover; Sections 1 and 2; [S001](../sources/README.md#s001), Cover; Scope)
- **STD-COM-F4** — RFC 5280 profiles X.509 certificates and certificate revocation lists; RFC 8446 specifies TLS 1.3. Their publication category is Standards Track, which is distinct from the Informational categories of several national-algorithm profiles. ([S064](../sources/README.md#s064), Header; Abstract; Sections 4 and 5; [S065](../sources/README.md#s065), Header; Abstract)
- **STD-COM-F5** — HKDF separates extraction of a pseudorandom key from expansion of output keying material. PKCS #5 v2.1 separately specifies PBKDF2, PBES2 and PBMAC1 for password-based derivation, encryption and authentication. ([S126](../sources/README.md#s126), Sections 2.1–2.3; Appendix A; [S127](../sources/README.md#s127), Sections 5.2, 6.2 and 7.1)
- **STD-COM-F6** — The preserved RFC index supplies stream, publication-status and current-status fields. For example it labels RFC 2994 Legacy, RFC 5528 IETF and Informational, and RFC 5529 IETF and Proposed Standard. The category printed in each RFC and the index’s more specific status remain distinct fields. ([S100](../sources/README.md#s100), rfc-entry elements RFC2994, RFC5528 and RFC5529: stream, publication-status, current-status; [S115](../sources/README.md#s115), Header and Status of This Memo; [S116](../sources/README.md#s116), Header and Status of This Memo)

### Inference

- **STD-COM-I1 · conditional** — If a product uses MEDLEY with GCM exactly as defined in SP 800-38D, the block cipher supplied to that mode has 128-bit blocks. This deduction supplies neither its key length nor its round construction. Basis: MEDLEY-F1, STD-COM-F1.
  Assumption: The manufacturer’s GCM label refers to the standard mode without a proprietary change in its block interface.

<a id="gost"></a>

## Russia: GOST parameters, modes and protocol bindings

Existing profiles: [GOST 28147-89](../profiles/international/gost-28147.md), [Magma](../profiles/international/magma.md), [Kuznyechik](../profiles/international/kuznyechik.md), [Streebog](../profiles/international/streebog.md), [GOST signatures](../profiles/international/gost-signatures.md).

Start with the Russian modes text, official registration record, separate 2018 correction and per-key data-volume recommendation. Then choose the algorithm generation, parameter/KDF documents, certificate or PFX encoding, and the required TLS/IPsec/CMS profile. RFC 9337’s integer-counter notation is an explicit unresolved compatibility question.

**Scope limit:** The preserved GOST binding RFCs are Informational Independent Submissions. RFC 8645 is an IRTF Informational document. These distinct streams do not imply IETF standards-track endorsement or establish the original Russian approval dates. The Russian printing and separate erratum are reproduced by a mirror with advertising-link text; they are not authenticated publisher downloads. RFC publication category varies across generations.

### Documented statements

- **STD-GOST-F1** — RFC 4357 provides additional modes, key meshing, wrapping, parameter sets and identifiers for the older GOST algorithm family. RFC 7836 adds HMAC, VKO key agreement, KDF and wrapping constructions and elliptic-curve parameters for the 2012 family. ([S050](../sources/README.md#s050), Abstract; Sections 2–8; [S057](../sources/README.md#s057), Sections 4 and 5; Appendix A)
- **STD-GOST-F2** — MGM is an authenticated-encryption mode defined for both 64-bit and 128-bit block ciphers. RFC 9058 supplies test vectors for Kuznyechik and Magma. ([S059](../sources/README.md#s059), Abstract; Section 4; Appendices A.1 and A.2)
- **STD-GOST-F3** — RFC 9227 binds Magma and Kuznyechik in MGM, with external rekeying, to ESP and IKEv2. RFC 9189 profiles GOST for TLS 1.2; RFC 9367 separately defines cipher suites, signature schemes and key exchange for TLS 1.3. ([S060](../sources/README.md#s060), Abstract; Section 1; [S062](../sources/README.md#s062), Abstract; [S063](../sources/README.md#s063), Abstract; Sections 4–6)
- **STD-GOST-F4** — RFC 9215 specifies GOST signature/hash identifiers, parameters and encodings for the Internet X.509 PKI, including public-key encoding and signature representation. ([S061](../sources/README.md#s061), Abstract; Sections 2–4)
- **STD-GOST-F5** — RFCs 7836, 9058, 9189, 9215, 9227 and 9367 are Informational Independent Submissions. RFC 8645 is Informational in the IRTF stream and describes symmetric rekeying mechanisms. ([S057](../sources/README.md#s057), Header; Status of This Memo; [S058](../sources/README.md#s058), Header; Abstract; Status of This Memo; [S059](../sources/README.md#s059), Header; [S060](../sources/README.md#s060), Header; [S061](../sources/README.md#s061), Header; [S062](../sources/README.md#s062), Header; [S063](../sources/README.md#s063), Header)
- **STD-GOST-F6** — GOST R 34.13-2015 cites approval order 750-st of 2015-06-19 and an effective date of 2016-01-01. The acquired Russian printing has a 2016 cover and an imprint signed for printing on 2016-03-28; these are separate milestones. ([S101](../sources/README.md#s101), Foreword, PDF p.2; printed p.1 / PDF p.6; imprint, PDF p.29; [S103](../sources/README.md#s103), Registration in the fund: order number, order date and effective date)
- **STD-GOST-F7** — The Russian modes standard defines ECB, CTR, OFB, CBC, CFB and MAC procedures and supplies examples for 128-bit and 64-bit block ciphers. Its Magma CBC example uses a 192-bit initialization register for a 64-bit block cipher. ([S101](../sources/README.md#s101), Sections 5.1–5.6; Appendix A; A.2.4.1, printed p.21 / PDF p.26)
- **STD-GOST-F8** — The separately preserved IUS No.6/2018 correction changes Section 5.3.2, rule (7), of GOST R 34.13-2015. It is retained as a correction document, without altering the earlier printing’s acquired bytes. ([S102](../sources/README.md#s102), Entire one-page correction, location column and corrected formula; [S103](../sources/README.md#s103), Changes and corrections: IUS 6-2018)
- **STD-GOST-F9** — R 1323565.1.005-2017 addresses permissible plaintext-block volumes processed under one key for certain GOST modes. It cites approval on 2017-10-25 and states effective 2018-04-01. Its scope assumes the adversary cannot obtain additional information about the key. ([S104](../sources/README.md#s104), Foreword, PDF p.2; Introduction, PDF p.4; Section 1, printed p.1 / PDF p.5)
- **STD-GOST-F10** — RFCs 4490 and 4491 were issued as Standards Track in May 2006 and bind the older GOST signature/hash family to CMS and X.509 respectively. RFC 9215 is a separate 2022 profile for the 2012 signature/hash algorithms; the editions are not interchangeable. ([S105](../sources/README.md#s105), Header; Sections 1–2; [S106](../sources/README.md#s106), Header; Section 1; [S061](../sources/README.md#s061), Header; Sections 1–2; [S100](../sources/README.md#s100), RFC4490, RFC4491 and RFC9215 entries)
- **STD-GOST-F11** — RFC 9337 specifies password-based derivation with HMAC using the 512-bit GOST R 34.11-2012 hash output, plus PBES2, PBMAC1 and ASN.1 identifiers. RFC 9548 separately profiles PKCS #12 PFX containers, private-key representations and certificates for GOST R 34.10-2012. Both are Informational Independent Submissions. ([S107](../sources/README.md#s107), Header; Sections 3–7; Appendix A; [S108](../sources/README.md#s108), Header; Sections 4–7 and 10; Appendix A)
- **STD-GOST-F12** — There is a visible counter-encoding discrepancy between the preserved texts: RFC 8018 Section 5.2 defines INT(i) as four octets with the most significant octet first, while RFC 9337 Section 3 defines Int(i) using i=i1+2^8*i2+2^16*i3+2^24*i4 and Section 4 uses S || INT(i). This is recorded as a specification question, not a verified implementation failure or a completed errata audit. ([S127](../sources/README.md#s127), Section 5.2, step 3 definition of INT(i); [S107](../sources/README.md#s107), Section 3, Table 1 Int(i); Section 4, U_1(i) equation)

### Inference

- **STD-GOST-I1 · conditional** — An implementation described only as supporting GOST is underspecified: interoperation also requires agreement on the primitive generation, curve or parameter set, mode, rekeying rules, encoding and protocol profile. Basis: STD-GOST-F1, STD-GOST-F2, STD-GOST-F3, STD-GOST-F4.
  Assumption: The parties exchange keys, signatures or protected messages using the cited protocol families.
- **STD-GOST-I2 · conditional** — An IV length alone cannot identify the cipher’s block size: the preserved GOST example explicitly uses an initialization register longer than one block. Basis: STD-GOST-F7.
  Assumption: The interface implements the cited GOST mode and its generalized register construction.
- **STD-GOST-I3 · conditional** — Literal implementations of the two counter definitions require an explicit compatibility decision before assuming identical PBKDF2 outputs. No claim is made here about deployed implementations or the resolution of any erratum. Basis: STD-GOST-F12.
  Assumption: The Int/INT notation in RFC 9337 denotes its tabulated integer encoding; no external correction or implementation-specific convention overrides it.

<a id="shangmi"></a>

## China: original releases, parameters and successive standards

Existing profiles: [SM2](../profiles/international/sm2.md), [SM3](../profiles/international/sm3.md), [SM4](../profiles/international/sm4.md).

Read the original 2010 release and curve sheet, then the acquired 2012 application/message/certificate/token standards and historical 2014 SSL VPN specification. S109 fills the missing GM/T 0009 body pages. Compare each with its exact later revision and the separate RFC 8998 TLS 1.3 profile.

**Scope limit:** The new Chinese scans are third-party mirror copies, not authenticated publisher downloads. S109 supplies the full 2012 application body, while S074 remains incomplete. The 2023 revision announcement still does not supply full revised texts. The 2012/2014 companion editions and the RFC’s TLS profile remain separate.

### Documented statements

- **STD-SM-F1** — The Chinese authority’s announcements No.21 and No.22 are dated 2010-12-17 and release SM2 and SM3 respectively. Their attached official algorithm PDFs carry December 2010 covers. ([S070](../sources/README.md#s070), Release date and announcement text; attachment links; [S071](../sources/README.md#s071), Release date and announcement text; attachment link; [S096](../sources/README.md#s096), Covers at PDF pages 1, 47, 61 and 80; [S098](../sources/README.md#s098), Cover)
- **STD-SM-F2** — The 93-page SM2 release combines Parts 1–4: general elliptic-curve rules, signatures, key exchange and public-key encryption. A separate one-page official attachment recommends a 256-bit prime-field curve and gives p, a, b, n, Gx and Gy. ([S096](../sources/README.md#s096), Part covers at PDF pages 1, 47, 61 and 80; [S097](../sources/README.md#s097), Entire one-page parameter sheet)
- **STD-SM-F3** — The recommended SM2 curve has p = FFFFFFFE FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF 00000000 FFFFFFFF FFFFFFFF and a = p − 3. Its equation is y² = x³ + ax + b over that prime field. This parameter choice is more specific than the general label elliptic-curve cryptography. ([S097](../sources/README.md#s097), Curve equation and parameter lines p and a)
- **STD-SM-F4** — The original SM3 specification uses 512-bit message blocks, 32-bit words, 64 compression rounds, modular addition, XOR, rotations and Boolean functions, and outputs 256 bits. ([S098](../sources/README.md#s098), Sections 2–5, especially 4.3–4.4 and 5.2–5.4)
- **STD-SM-F5** — The 2012-11-22 announcement lists GM/T 0009-2012 for SM2 applications, GM/T 0010-2012 for signed/enveloped message syntax, GM/T 0014-2012 for certificate-authentication protocols and GM/T 0015-2012 for certificate format. ([S072](../sources/README.md#s072), Announcement No.24; numbered standards list)
- **STD-SM-F6** — Announcement No.45, posted 2023-12-23, lists 2023 revisions of GM/T 0009, 0010, 0014 and 0015 among other standards and states an effective date of 2024-06-01. The web posting date is recorded separately from each standard’s issue date. ([S073](../sources/README.md#s073), Posting date; announcement; attached standards list)
- **STD-SM-F7** — The official GB/T records for SM2 Part 1 and SM4 record issue on 2016-08-29 and implementation on 2017-03-01. These are later national-standard milestones, separate from the 2010 SM2 release and 2012 industry-standard announcements. ([S035](../sources/README.md#s035), Issue and implementation metadata; [S036](../sources/README.md#s036), Issue and implementation metadata; [S070](../sources/README.md#s070), Release date; [S034](../sources/README.md#s034), Announcement No.23 and standards list)
- **STD-SM-F8** — RFC 8998 profiles SM2, SM3 and SM4 for TLS 1.3, including SM4-GCM and SM4-CCM cipher suites. It is an Informational Independent Submission, while the underlying TLS 1.3 specification RFC 8446 is Standards Track. ([S026](../sources/README.md#s026), Header; Sections 2 and 3; [S065](../sources/README.md#s065), Header)
- **STD-SM-F9** — A second GM/T 0009-2012 acquisition contains 12 PDF pages, including all printed body pages 1–7. Its cover prints issue and implementation on 2012-11-22; its final imprint says first edition and printing in January 2013. The older S074 remains a separately preserved incomplete scan. ([S109](../sources/README.md#s109), Cover; contents; printed body pp.1–7 / PDF pp.5–11; imprint / PDF p.12)
- **STD-SM-F10** — GM/T 0009-2012 specifies private/public-key and encryption/signature data formats. Its public-key BIT STRING contains 04 || X || Y, with 256-bit coordinates. Its encryption structure lists XCoordinate, YCoordinate, a 32-byte hash and ciphertext; its signature representation contains integer R and S fields. ([S109](../sources/README.md#s109), Sections 5.1–5.2 and 7.1–7.3, printed pp.1–3 / PDF pp.5–7)
- **STD-SM-F11** — The application standard defines identity preprocessing and, absent a special agreement, the 16-byte user identity represented by the ASCII string 1234567812345678. RFC 8998 instead specifies a TLS-specific SM2 signature identity for its handshake context and separately discusses certificate identities. ([S109](../sources/README.md#s109), Section 8, printed p.4 / PDF p.8; Section 10, printed p.7 / PDF p.11; [S026](../sources/README.md#s026), Section 3.2.1, SM2 signature scheme identity values)
- **STD-SM-F12** — GM/T 0010-2012 defines object identifiers and signed, enveloped, signed-and-enveloped, encrypted and key-agreement message structures, with SM2 key syntax in normative Appendix A. These are message encodings around the primitive. ([S110](../sources/README.md#s110), Section 5; Sections 8–12; normative Appendix A, printed p.9 / PDF p.12)
- **STD-SM-F13** — GM/T 0014-2012 specifies certificate-system protocols and associated message formats; Section 5 refers SM2 key structures to GM/T 0009 and encapsulation to GM/T 0010. GM/T 0015-2012 separately specifies DER-based certificate and CRL structures and encoding examples. ([S111](../sources/README.md#s111), Section 5, printed p.2 / PDF p.7; Section 6; Appendices A–B; [S112](../sources/README.md#s112), Sections 5.2 and 6; Appendices A–D)
- **STD-SM-F14** — GM/T 0017-2012 is a smart-token interface data-format specification whose Sections 7–9 cover command/response APDUs, instruction/status-byte encoding and commands. The scan’s cover prints the 2012 edition and 2012-11-22 issue/effective dates. ([S113](../sources/README.md#s113), Cover, PDF p.1; contents, PDF pp.2–5; Sections 7–9)
- **STD-SM-F15** — The acquired GM/T 0024-2014 is an SSL VPN specification with issue and effective dates 2014-02-13 on its cover. It is a historical Chinese VPN specification, separate from the 2021 RFC 8998 TLS 1.3 profile. ([S114](../sources/README.md#s114), Cover, PDF p.1; contents and Scope; [S026](../sources/README.md#s026), Header; Abstract; Section 1)

### Inference

- **STD-SM-I1 · conditional** — The curve sheet and SM3 text allow concrete descriptions of arithmetic, parameters and hashing without inferring those choices from a codeword. The published record does not, by itself, identify the original classified design date or every government use. Basis: STD-SM-F1, STD-SM-F2, STD-SM-F3, STD-SM-F4.
  Assumption: The question concerns the preserved public specifications and their dated releases, rather than an undocumented earlier variant.
- **STD-SM-I2 · conditional** — Interoperation requires agreement on identity preprocessing, point/ciphertext/signature representation and the protocol binding. The label SM2 support alone leaves choices visible in these companion documents unresolved. Basis: STD-SM-F10, STD-SM-F11, STD-SM-F12, STD-SM-F13.
  Assumption: The implementations exchange the specified SM2 objects or signatures, rather than merely using elliptic-curve arithmetic internally.

<a id="zuc"></a>

## China and 3GPP: ZUC, EEA3 and EIA3

Existing profiles: [ZUC / Zu Chongzhi](../profiles/international/zuc.md).

Read ZUC Document 2 for the keystream generator, Document 1 for the EEA3/EIA3 packet algorithms, Document 3 for implementer test data and Document 4 for design/evaluation history. The Release 19 ETSI wrapper records the later standards context.

**Scope limit:** These copies come from different dated editions; they are not a single synchronized conformance package. In particular, the Release 19 wrapper specifically references Document 1 v1.7, whereas the separately preserved Document 1 is v1.8. Test vectors and design evaluation are separate kinds of evidence.

### Documented statements

- **STD-ZUC-F1** — The archive holds ZUC Document 2 v1.6 (2011-06-28), EEA3/EIA3 Document 1 v1.8 (2019-01-24), Implementor’s Test Data v1.1 (2011-01-04), and Design and Evaluation Report v2.0 (2011-09-09). ([S037](../sources/README.md#s037), Cover; [S076](../sources/README.md#s076), Cover; [S092](../sources/README.md#s092), Cover; [S093](../sources/README.md#s093), Cover)
- **STD-ZUC-F2** — The EEA3/EIA3 document history records initial publication on 2010-06-18, an EIA3 modification on 2011-01-04, and maximum-message-length changes in 2011 and 2019. The design report records the first public release of that report on 2010-08-11 and a ZUC/EIA3 modification in January 2011. ([S076](../sources/README.md#s076), Document History, PDF page 2; [S093](../sources/README.md#s093), Document History, PDF page 2)
- **STD-ZUC-F3** — The test-data preface includes internal ZUC state and input/output examples, but expressly says conformance with the test data does not guarantee a correct implementation. ([S092](../sources/README.md#s092), Preface, PDF page 3)
- **STD-ZUC-F4** — ETSI TS 135 221 v19.0.0 is dated October 2025 and identifies 3GPP TS 35.221 Release 19. Its technical provisions are incorporated by reference to EEA3/EIA3 Document 1 v1.7; the separately archived Document 1 is v1.8. ([S075](../sources/README.md#s075), Cover; Section 2 reference [2]; Section 4; [S076](../sources/README.md#s076), Cover)

### Inference

- **STD-ZUC-I1 · conditional** — The name ZUC alone does not fully specify the cellular confidentiality or integrity operation: EEA3 and EIA3 define different uses of the generator, with packet inputs and initialization rules. Version history is necessary when interpreting early analyses. Basis: STD-ZUC-F1, STD-ZUC-F2, STD-ZUC-F4.
  Assumption: The implementation or historical analysis concerns the 128-EEA3/128-EIA3 family covered by these records.

<a id="japan"></a>

## Japan: selection lists, additional primitives and Camellia profiles

Existing profiles: [Camellia](../profiles/international/camellia.md), [CLEFIA](../profiles/international/clefia.md), [MISTY1](../profiles/international/misty1.md), [KCipher-2](../profiles/international/kcipher2.md), [KASUMI](../profiles/international/kasumi.md).

Compare dated CRYPTREC selections with the primitive specification. Camellia’s mode/test-vector, IPsec and TLS documents have different RFC categories. MISTY1, KCipher-2 and KASUMI are separately specified primitives; a later RFC or standards wrapper does not date their invention.

**Scope limit:** CRYPTREC list membership and category are dated policy evidence. They do not establish first invention, implementation certification or universal government approval.

### Documented statements

- **STD-JP-F1** — The preserved legacy CRYPTREC list is dated 2003-02-20 and includes a 2005-10-12 correction appendix. The archive also holds the 2013-03-01 list and the list revised 2026-03-30, whose family cover date is 2023-03-30. ([S094](../sources/README.md#s094), Cover and correction appendix; [S079](../sources/README.md#s079), Cover; [S078](../sources/README.md#s078), Cover)
- **STD-JP-F2** — The March 2026 list places Camellia among e-Government Recommended Ciphers and CLEFIA among Candidate Recommended Ciphers. A separate Monitored Ciphers category also exists. ([S078](../sources/README.md#s078), e-Government Recommended, Candidate Recommended and Monitored tables; PDF pages 1, 4 and 5)
- **STD-JP-F3** — The strength-requirements PDF’s revision table records first publication on 2022-07-01 and corrections on 2023-03-30. Its cover still states March 2022; the archive retains that internal date discrepancy. ([S080](../sources/README.md#s080), Cover; revision table in introductory pages)
- **STD-JP-F4** — RFC 5932 specifies Camellia cipher suites for TLS (June 2010), and RFC 4312 specifies Camellia for IPsec (December 2005). Both were published with the Standards Track category. ([S086](../sources/README.md#s086), Header; Abstract; [S087](../sources/README.md#s087), Header; Abstract)
- **STD-JP-F5** — RFC 5528 gives Camellia CTR/CCM algorithms and test vectors; RFC 5529 binds CBC/CTR/CCM to IPsec. Both date to April 2009, but the first is IETF Informational and the second Standards Track. RFC 6367 adds Camellia TLS cipher suites in September 2011 as IETF Informational. ([S115](../sources/README.md#s115), Header; Sections 3–4; [S116](../sources/README.md#s116), Header; Sections 1 and 3–6; [S117](../sources/README.md#s117), Header; Abstract; Sections 2–3; [S100](../sources/README.md#s100), RFC5528, RFC5529 and RFC6367 stream/status entries)
- **STD-JP-F6** — The new primitive records include MISTY1 (RFC 2994, November 2000), KCipher-2 (RFC 7008, August 2013) and an April 2022 Release 17 KASUMI specification. These are concrete preserved editions, not common first-approval dates. ([S118](../sources/README.md#s118), Header; Sections 1–2; [S119](../sources/README.md#s119), Header; Abstract; Section 2; [S120](../sources/README.md#s120), Cover; Sections 0 and 3)
- **STD-JP-F7** — The December 2002 3GPP TR 55.919 design/evaluation report explicitly describes KASUMI’s changes from MISTY1 in the data-encryption part and key schedule. Its cover marks the preserved copy as not approved by the Organizational Partners and not for implementation; its design history is not an approval record. ([S139](../sources/README.md#s139), Cover; Sections 9.2–9.3, printed/PDF pp.14–15)

### Inference

- **STD-JP-I1 · conditional** — A claim that Camellia and CLEFIA have the same CRYPTREC recommendation status loses a distinction visible in the preserved 2026 list. An accurate claim names both the edition and category. Basis: STD-JP-F2.
  Assumption: The claim refers to the March 2026 CRYPTREC list, rather than a different selection program or edition.

<a id="korea"></a>

## Republic of Korea: SEED and ARIA protocol profiles

Existing profiles: [SEED](../profiles/international/seed.md), [ARIA](../profiles/international/aria.md).

Use the existing SEED and ARIA primitive specifications, then the TLS and IPsec/SRTP bindings as relevant. The KCMVP programme pages are acquisition leads only until their original bytes can be preserved.

**Scope limit:** The three KISA pages returned HTTP 503 and were not preserved. No current KCMVP eligibility list, complete validation procedure, or certificate is asserted from those unavailable pages.

### Documented statements

- **STD-KR-F1** — RFCs 4162 and 4196 bind SEED to TLS and IPsec, with publication dates August and October 2005. Their preserved headers give the Standards Track category. ([S088](../sources/README.md#s088), Header; Abstract; [S089](../sources/README.md#s089), Header; Abstract)
- **STD-KR-F2** — RFC 6209 defines ARIA cipher suites for TLS (April 2011). RFC 8269 defines ARIA for SRTP (October 2017), including CTR/GCM, key derivation, DTLS-SRTP profiles and MIKEY parameters. Both are IETF Informational documents. ([S090](../sources/README.md#s090), Header; Abstract; Status of This Memo; [S091](../sources/README.md#s091), Header; Abstract; Status of This Memo)
- **STD-KR-F3** — RFC 4010, issued Standards Track in February 2005, specifies SEED in CMS and supplies identifiers for its use. It is an encoding/protocol companion rather than a module-validation certificate. ([S122](../sources/README.md#s122), Header; Abstract; Sections 2–3; [S100](../sources/README.md#s100), RFC4010 stream/status entry)
- **STD-KR-F4** — RFC 5669, issued IETF Standards Track in August 2010, specifies SEED for SRTP/SRTCP, including CTR, CCM and GCM, nonce formats, SEED-CTR key derivation and test vectors. ([S121](../sources/README.md#s121), Header; Sections 2–4; Appendix A)

### Inference

- **STD-KR-I1 · conditional** — The protocol records establish specified interoperability choices, but they do not by themselves show that a named product passed Korean module validation. Such a claim needs a product-specific validation record and its scope. Basis: STD-KR-F1, STD-KR-F2.
  Assumption: The proposed claim concerns implementation validation rather than publication of a protocol profile.

<a id="germany"></a>

## Germany: ECC constructions, Brainpool and protocol guidance

Existing profiles: [CHIASMUS](../profiles/international/chiasmus.md), [LIBELLE / SINA](../profiles/international/libelle.md), [Brainpool curves](../profiles/international/brainpool.md).

Read TR-03111 for concrete signature/key-agreement operations and encodings, RFC 5639 for Brainpool parameters and RFC 8734 for its TLS 1.3 binding. TR-02102 supplies the separately dated recommendation and protocol context.

**Scope limit:** General BSI technical guidance is not a public specification of LIBELLE or proof that a particular SINA product is approved for a classification level. It also does not establish CHIASMUS’s internal construction.

### Documented statements

- **STD-DE-F1** — The archived TR-02102-1 is version 2026-01, as of 2026-01-23. It provides general cryptographic mechanism and key-length recommendations. ([S081](../sources/README.md#s081), Cover; Section 1)
- **STD-DE-F2** — TR-02102 Parts 2, 3 and 4 address TLS, IPsec/IKEv2 and SSH respectively. Each preserved edition’s history dates version 2026-01 to 2026-01-27. ([S082](../sources/README.md#s082), Cover; Document history; Section 1; [S083](../sources/README.md#s083), Cover; Document history; Section 1; [S095](../sources/README.md#s095), Cover; Document history; Section 1)
- **STD-DE-F3** — BSI TR-03111’s cover and history identify version 2.10 dated 2018-06-01 and its initial public version on 2007-02-14. The URL filename’s V-2-1 token is not the printed version number. ([S125](../sources/README.md#s125), Cover, PDF p.1; History, PDF p.2)
- **STD-DE-F4** — TR-03111 separately specifies ECDSA, ECGDSA, EC Schnorr signatures, elliptic-curve key agreement, derivation functions and PACE, then gives public-key/signature input-output formats and OIDs. ([S125](../sources/README.md#s125), Sections 4.2–4.4; Sections 5.1–5.4)
- **STD-DE-F5** — RFC 5639 supplies Brainpool curve parameters and generation procedures. RFC 8734 separately specifies Brainpool groups and signature schemes for TLS 1.3. Both are Informational Independent Submissions; a curve definition and a TLS binding are different records. ([S123](../sources/README.md#s123), Header; Sections 2–4; Appendix A; [S124](../sources/README.md#s124), Header; Sections 2–3)

### Inference

- **STD-DE-I1 · conditional** — The TR series supplies a public policy and protocol context for German deployments; identifying the mathematics or approval scope of an opaque product still requires a record that names that product and its algorithm or certification boundary. Basis: STD-DE-F1, STD-DE-F2.
  Assumption: No additional product-specific approval or algorithm specification is supplied by the generic guidance citation.

<a id="france"></a>

## France: ANSSI selection and mechanism rules

Existing profiles: [Brainpool curves](../profiles/international/brainpool.md).

Read the distribution-page snapshot, then the exact cover and history of each guide. The rules PDF is version 3.00 of March 2026; the selection guide is version 1.0 of March 2021. Use cited specifications for the actual algorithm and encoding.

**Scope limit:** A distribution page’s date does not redetermine a linked PDF’s edition. Recommendation, reference-rule compliance and product certification remain different attributes. The earlier v2.04 PDF was not recovered in this pass.

### Documented statements

- **STD-FR-F1** — The current ANSSI distribution page is dated 2026-03-20 and links two guides. The mechanisms rules PDF is version 3.00 dated 2026-03-20; the algorithm-selection PDF remains the initial version 1.0 dated 2021-03-08. ([S128](../sources/README.md#s128), Publication date and two download links; [S129](../sources/README.md#s129), Cover; version history, PDF p.3; [S130](../sources/README.md#s130), Cover; version history, PDF p.3)
- **STD-FR-F2** — The mechanisms guide’s revision history records a first applicable version on 2004-11-19, v2.04 on 2020-01-01 and v3.00 on 2026-03-20, with the quantum threat added to the latter. These are guide-version milestones. ([S129](../sources/README.md#s129), Version history, PDF p.3)
- **STD-FR-F3** — The 2021 selection guide separately recommends key-wrapping mechanisms SIV and AES-KeyWrap, KDFs including HKDF and PBKDF2, and selected elliptic-curve families including Brainpool. Recommendations are attached to specified mechanisms and implementation notes. ([S130](../sources/README.md#s130), Sections 4.6–4.8, printed pp.26–28 / PDF pp.28–30; Section 5.3, printed pp.31–32 / PDF pp.33–34)
- **STD-FR-F4** — The 2026 rules guide recommends seeking post-quantum security for mechanisms expected to remain in use after 2030-01-01 or exposed to retrospective decryption risk. The guide states that general rule compliance alone is insufficient to guarantee mechanism security. ([S129](../sources/README.md#s129), Section 2, RecoSécuLongTerme, printed p.8 / PDF p.10; Section 1.4, printed p.5 / PDF p.7)

### Inference

- **STD-FR-I1 · conditional** — The two currently linked guides must be interpreted with their own dates and scopes. A 2026 webpage does not establish a 2026 revision of every recommendation in the 2021 PDF. Basis: STD-FR-F1, STD-FR-F2, STD-FR-F3.
  Assumption: The historical question concerns the acquired PDF editions, not an unpreserved later revision.

<a id="mobile-snow"></a>

## International mobile standards: SNOW 3G, UEA2 and UIA2

Existing profiles: [SNOW 3G](../profiles/international/snow3g.md).

Read Document 2 for the generator, Document 1 for packet confidentiality/integrity, Document 3 for tests and Document 5 for design history. The GSMA distribution index records the provenance of these copies.

**Scope limit:** The preserved companion documents have different dates and version numbers. The historical evaluation describes its contemporary design rationale; it is not a present-day security guarantee. This is an international standardization context, not a national approval inventory.

### Documented statements

- **STD-MOBILE-F1** — SNOW 3G Document 2 v1.1 is dated 2006-09-06 and records initial publication on 2006-01-10. The generator uses a 128-bit key and 128-bit initialization variable, a 16-word LFSR and a three-register FSM, with 32-bit output words. ([S131](../sources/README.md#s131), Cover; Document History, PDF p.2; Sections 2.1, 3.2 and 3.3)
- **STD-MOBILE-F2** — UEA2/UIA2 Document 1 v2.1 is dated 2009-03-16. Its confidentiality and integrity algorithms use distinct input mappings and generator uses; the history identifies the 2009 change as a C-code improvement. ([S132](../sources/README.md#s132), Cover; Document History, PDF p.2; Sections 3–4)
- **STD-MOBILE-F3** — The design/evaluation report describes SNOW 3G as a modification of SNOW 2.0 and explains changes to the FSM and nonlinear components. Its v1.1 cover is dated 2006-09-06; its history records v1.0 on 2006-02-06. ([S134](../sources/README.md#s134), Cover; Document History, PDF p.2; Sections 8.1.2–8.3)
- **STD-MOBILE-F4** — The implementors’ test document is v1.1 dated 2012-10-25, distinct from the 2006 primitive and design documents and 2009 packet specification. GSMA’s distribution page links these records and states its distribution role for UEA2/UIA2. ([S133](../sources/README.md#s133), Cover; Document History, PDF pp.1–2; [S135](../sources/README.md#s135), UEA2 & UIA2 distribution section and Documents 1–5 links)

### Inference

- **STD-MOBILE-I1 · conditional** — A name such as SNOW 3G identifies a generator; a complete cellular operation also needs the confidentiality or integrity construction, initialization mapping, length conventions and exact companion edition. Basis: STD-MOBILE-F1, STD-MOBILE-F2, STD-MOBILE-F4.
  Assumption: The target implementation follows the preserved UEA2/UIA2 family, rather than another use of the underlying generator.

<a id="historical-archives"></a>

## Swiss and Swedish historical machine records

Existing profiles: [NEMA](../profiles/international/nema.md), [Siemens T52 / G-schreiber](../profiles/international/siemens-t52.md).

Start with the original bilingual NEMA instructions and their cover stamp. For Siemens T52, separate FRA’s retrospective institutional history from Borelius’s explicitly hypothetical reconstruction of Beurling’s working method.

**Scope limit:** The manual’s original issue date is unverified. Borelius’s account was written in the 1980s and is not Beurling’s contemporaneous laboratory record. Raw web snapshots do not include every externally linked image.

### Documented statements

- **STD-HIST-F1** — The NEMA instructions’ cover identifies copy 717 and bears a declassification stamp dated 1992-07-09. The bilingual German/French instructions are preserved as 18 PDF pages of scanned booklet spreads; the original publication date is not established. ([S136](../sources/README.md#s136), Cover, PDF p.1; German opening, PDF p.2; French portion)
- **STD-HIST-F2** — FRA’s official history identifies the G-schreiber as Siemens und Halske T52 and dates the first interception of the relevant teleprinter traffic to 19 May 1940. It separately dates FRA’s establishment as an independent agency to 1942-07-01. ([S137](../sources/README.md#s137), G-skrivaren, printed pp.8–9 / PDF p.5; FRA bildas, printed pp.10–11 / PDF p.6)
- **STD-HIST-F3** — FRA identifies Carl-Gösta Borelius as a participant in G-schreiber cryptanalysis from 1941 and describes this account as written in the 1980s. Its introduction explicitly presents a reconstruction of how Beurling may have proceeded, rather than a disclosed account by Beurling himself. ([S138](../sources/README.md#s138), Introduction under Hur gjorde Arne Beurling för att forcera G-skrivaren?; concluding paragraphs)

### Inference

- **STD-HIST-I1 · conditional** — The 1992 declassification stamp dates release of a secrecy control on the surviving manual; it supplies no first-use or first-approval date for the NEMA machine. Basis: STD-HIST-F1.
  Assumption: The stamp is read as a declassification annotation on this copy, without an additional original approval record.

## Publication and effective dates

These events distinguish releases, revisions, list selections and publication categories. None is automatically an invention date or first classified approval.

| Date | Subject | Event type | Interpretation | Evidence |
|---|---|---|---|---|
| 1992-07-09 | NEMA operating manual | declassification annotation | Date stamped on surviving manual copy 717; original issue unverified. | [S136](../sources/README.md#s136), Cover |
| 2003-02-20 | CRYPTREC legacy list | list issue | Original list date; the preserved R1 copy also has a 2005 correction. | [S094](../sources/README.md#s094), Cover; correction appendix |
| 2005-08 | SEED / TLS | RFC publication | RFC 4162 Standards Track profile; not an invention date. | [S088](../sources/README.md#s088), Header |
| 2005-10-12 | CRYPTREC legacy list | correction | Specification-reference correction; not a new cipher design. | [S094](../sources/README.md#s094), Correction appendix |
| 2005-12 | Camellia / IPsec | RFC publication | RFC 4312 Standards Track profile. | [S087](../sources/README.md#s087), Header |
| 2006-01-10 | SNOW 3G Document 2 | recorded initial publication | Date in the preserved v1.1 history, not a first national approval. | [S131](../sources/README.md#s131), Document History, PDF p.2 |
| 2010-06-18 | EEA3/EIA3 | specification publication | Document 1 history records v1.0 publication. | [S076](../sources/README.md#s076), Document History, PDF page 2 |
| 2010-12-17 | SM2 and SM3 | public release announcements | Official releases; attached PDFs have December 2010 covers. | [S070](../sources/README.md#s070), Announcement; compare S071 |
| 2011-01-04 | ZUC/EEA3/EIA3 | algorithm revision and test edition | EIA3 modification and v1.1 implementer-test edition; see design report for ZUC change. | [S076](../sources/README.md#s076), Document History; compare S092 and S093 |
| 2011-09-09 | ZUC design evaluation | report edition | Version 2.0 final deliverable. | [S093](../sources/README.md#s093), Cover; Document History |
| 2012-03-21 | Chinese industry standards | standards announcement | No.23 lists six standards including SM3 and SM4 industry standards. | [S034](../sources/README.md#s034), Announcement; standards list |
| 2012-10-25 | UEA2/UIA2 test data | document revision | Document 3 v1.1; not the generator specification’s date. | [S133](../sources/README.md#s133), Cover |
| 2012-11-22 | SM2 application ecosystem | standards announcement | No.24 lists applications, message syntax, certificate protocols and formats. | [S072](../sources/README.md#s072), Announcement; standards list |
| 2013-01 | GM/T 0009-2012 | first printing | January 2013 first edition/printing follows the standard’s 2012-11-22 issue. | [S109](../sources/README.md#s109), Imprint, PDF p.12 |
| 2013-03-01 | CRYPTREC list | list issue | Original 2013 list retained as a historical edition. | [S079](../sources/README.md#s079), Cover |
| 2014-02-13 | GM/T 0024-2014 | standard issue and effective date | Historical SSL VPN specification; separate from the later TLS 1.3 RFC. | [S114](../sources/README.md#s114), Cover |
| 2015-06-19 | GOST R 34.13-2015 | standard approval order | Order 750-st; distinct from effective and printing dates. | [S101](../sources/README.md#s101), Foreword, PDF p.2 |
| 2016-01-01 | GOST R 34.13-2015 | effective date | Effective date printed in the standard and official catalogue. | [S101](../sources/README.md#s101), Printed p.1 / PDF p.6 |
| 2016-03-28 | GOST R 34.13-2015 | printing milestone | Signed for printing; not the standard issue date. | [S101](../sources/README.md#s101), Imprint, PDF p.29 |
| 2016-08-29 | SM2 Part 1 and SM4 | national-standard issue | GB/T issue date; later implementation date is 2017-03-01. | [S036](../sources/README.md#s036), Official metadata; compare S035 |
| 2017-03-01 | SM2 Part 1 and SM4 | national-standard implementation | Implementation date distinct from public release and issue. | [S036](../sources/README.md#s036), Official metadata; compare S035 |
| 2017-10 | ARIA / SRTP | RFC publication | RFC 8269 IETF Informational profile. | [S091](../sources/README.md#s091), Header |
| 2018-04-01 | R 1323565.1.005-2017 | effective date | Per-key data-volume recommendation; approval order is dated 2017-10-25. | [S104](../sources/README.md#s104), Printed p.1 / PDF p.5 |
| 2018-06 | GOST modes correction | corrigendum issue | IUS No.6/2018 correction to 5.3.2, rule (7); no exact day asserted. | [S102](../sources/README.md#s102), One-page correction |
| 2018-06-01 | BSI TR-03111 | guideline revision | Printed version 2.10, despite V-2-1 in the download filename. | [S125](../sources/README.md#s125), Cover and History |
| 2019-01-24 | EEA3/EIA3 | specification revision | Document 1 v1.8 increases maximum integrity-message length. | [S076](../sources/README.md#s076), Cover; Document History |
| 2020-06-15 | PKCS #11 v3.0 | OASIS standard edition | Matched Base and Historical Mechanisms editions. | [S066](../sources/README.md#s066), Cover; compare S001 |
| 2021-03-08 | ANSSI selection guide | initial guide issue | ANSSI-PA-079 v1.0; the currently linked PDF still has this date. | [S130](../sources/README.md#s130), Cover and version history |
| 2021-06 | MGM | RFC publication | RFC 9058; separate from the original Russian mode standardization. | [S059](../sources/README.md#s059), Header; Abstract |
| 2022-03 | GOST protocol and PKI profiles | RFC publications | TLS 1.2, X.509 and ESP/IKEv2 companion RFCs. | [S062](../sources/README.md#s062), Header; compare S060 and S061 |
| 2022-07-01 | CRYPTREC strength requirements | first publication in revision table | Table date conflicts with March 2022 printed cover; retain both fields. | [S080](../sources/README.md#s080), Cover; revision table |
| 2023-02 | GOST / TLS 1.3 | RFC publication | RFC 9367 Informational Independent Submission. | [S063](../sources/README.md#s063), Header |
| 2023-03-30 | CRYPTREC strength requirements | correction | R1 correction record, including publication-month correction. | [S080](../sources/README.md#s080), Revision table |
| 2023-12-23 | Chinese revised standards | announcement posting | No.45 announcement posting date, not every standard’s issue date. | [S073](../sources/README.md#s073), Posting metadata; announcement |
| 2024-06-01 | Chinese revised standards | effective date | Effective date stated in No.45 for the announced revisions. | [S073](../sources/README.md#s073), Announcement |
| 2025-10 | ETSI EEA3/EIA3 wrapper | technical-specification edition | TS 135 221 v19.0.0, Release 19. | [S075](../sources/README.md#s075), Cover |
| 2026-01-23 | BSI TR-02102-1 | guidance edition | Version 2026-01, as-of date from cover. | [S081](../sources/README.md#s081), Cover |
| 2026-01-27 | BSI TLS/IPsec/SSH guidance | guidance edition | Version 2026-01 dates from histories of Parts 2, 3 and 4. | [S082](../sources/README.md#s082), Document history; compare S083 and S095 |
| 2026-03-20 | ANSSI mechanism rules | guideline revision | ANSSI-PG-083 v3.00; adds quantum-threat treatment. | [S129](../sources/README.md#s129), Cover and version history |
| 2026-03-30 | CRYPTREC list | list revision | LS-0001-2022R2, with distinct recommended, candidate and monitored lists. | [S078](../sources/README.md#s078), Cover; list tables |

## Preservation and coverage limits

### Incomplete application-standard scan

S074 remains the original three-page incomplete booklet scan and must still be labeled incomplete. S109 is a separate 12-page mirror acquisition whose complete body sequence 1–7 has been checked against the contents. The earlier gap is filled for the 2012 application text; the old bytes are retained for provenance. This does not supply the 2023 revision. ([S074](../sources/README.md#s074), [S109](../sources/README.md#s109))

### Korean validation acquisition gaps

S084, S085 and S099 each returned HTTP 503 again on 2026-10-20 after one respectful retry. Prior errors remain in acquisition_history. No current KCMVP eligibility list, procedure page or product certificate is claimed. New SEED RFC companions do not resolve this gap. ([S084](../sources/README.md#s084), [S085](../sources/README.md#s085), [S099](../sources/README.md#s099))

### Revised standards announced but not fully acquired

S073 preserves the official announcement and list of 2023 industry-standard revisions. The archive does not claim to contain the full text of every listed revision. Historical 2012 material cannot silently substitute for a 2023 edition. ([S072](../sources/README.md#s072), [S073](../sources/README.md#s073), [S074](../sources/README.md#s074), [S109](../sources/README.md#s109), [S110](../sources/README.md#s110), [S111](../sources/README.md#s111), [S112](../sources/README.md#s112))

### Translations and mutable publisher URLs

The earlier Alipay-hosted English SM2/SM3/SM4 files remain separately labeled translations with edition uncertainties. The newly acquired official Chinese release files supply independent 2010 evidence. BSI and CRYPTREC URLs may later change their contents; SHA-256 and acquisition times identify the copies used here. ([S070](../sources/README.md#s070), [S071](../sources/README.md#s071), [S078](../sources/README.md#s078), [S081](../sources/README.md#s081), [S096](../sources/README.md#s096), [S097](../sources/README.md#s097), [S098](../sources/README.md#s098))

### Status and coverage limits

RFC categories and streams describe publication status at issue. This guide does not perform a complete present-day obsolescence, errata or approval audit. Full ISO/IEC standards and every national standard cited by the profiles are not all preserved. Historical rotor-machine records remain in their existing profiles; modern companion standards are not retroactively applied to Enigma, Lorenz or Fialka.

### Mirrors, overlays and incomplete authentication

The Chinese scans are pinned to a third-party GitHub commit and retain scan marks. The Russian Meganorm copies include host-added advertising-link text. Their acquired bytes are unchanged, but neither host is the original issuing authority. Rosstandart’s independently preserved catalogue record confirms the identified modes standard and dates, not the byte authenticity of every mirrored page. ([S101](../sources/README.md#s101), [S102](../sources/README.md#s102), [S103](../sources/README.md#s103), [S104](../sources/README.md#s104), [S109](../sources/README.md#s109), [S110](../sources/README.md#s110), [S111](../sources/README.md#s111), [S112](../sources/README.md#s112), [S113](../sources/README.md#s113), [S114](../sources/README.md#s114))

### French historical guide recovery and edition mismatch

The former v2.04 mechanisms-PDF URL now redirects to a current distribution page. The archive acquired the linked March 2026 v3.00 rules and March 2021 v1.0 selection guide separately. The historical v2.04 file and RGS key-management Annex B2 were not acquired; attempted B2 locations returned 404. data/acquisition-attempts.json records these outcomes. ([S128](../sources/README.md#s128), [S129](../sources/README.md#s129), [S130](../sources/README.md#s130))

### GOST password-KDF notation remains a specification question

The literal integer-counter encodings in RFC 8018 and RFC 9337 differ. The guide records the equations and their locators, without silently merging the definitions, asserting a deployed failure, or claiming that all errata and implementations have been audited. ([S107](../sources/README.md#s107), [S127](../sources/README.md#s127))

## Source catalogue

The following records are the editions used for this companion collection. The global catalogue also covers the earlier historical collections. Successful retrieval, completeness of a document, publication status and implementation approval remain separate attributes.

### S001 — PKCS #11 Historical Mechanisms Specification v3.0

Publisher: OASIS  
Document date: 2020-06-15  
Language: English · Format: pdf  
Provenance: Original publisher

Original URL: <https://docs.oasis-open.org/pkcs11/pkcs11-hist/v3.0/os/pkcs11-hist-v3.0-os.pdf>

[Preserved file](../sources/originals/S001-oasis-pkcs11-historical-2020.pdf) · 1,548,298 bytes · 64 PDF pages

Retrieved UTC: 2026-10-17T18:39:55.140223+00:00  
SHA-256: `d3cd42b3d17abfe068ed410967da38df97a4f14763bbf33aa10c1605ba7eb0a5`

### S003 — SP 800-38D: Galois/Counter Mode and GMAC

Publisher: NIST  
Document date: 2007-11  
Language: English · Format: pdf  
Provenance: Original publisher

Original URL: <https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38d.pdf>

[Preserved file](../sources/originals/S003-nist-gcm-2007.pdf) · 271,960 bytes · 39 PDF pages

Retrieved UTC: 2026-10-17T18:39:55.143028+00:00  
SHA-256: `d99f3921ccebca049e7522426553aba071dae14ec3d5b6041e8c111a6cb57bba`

### S004 — SP 800-38A: Block Cipher Modes of Operation

Publisher: NIST  
Document date: 2001-12  
Language: English · Format: pdf  
Provenance: Original publisher

Original URL: <https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38a.pdf>

[Preserved file](../sources/originals/S004-nist-modes-2001.pdf) · 378,266 bytes · 66 PDF pages

Retrieved UTC: 2026-10-17T18:39:55.145224+00:00  
SHA-256: `66821162de1e7130c5fb5eedb22140d8d6d013ec51af4550bb095c2a9481a00e`

### S026 — RFC 8998: ShangMi (SM) Cipher Suites for TLS 1.3

Publisher: RFC Editor; named document authors  
Document date: 2021-03  
Language: English · Format: pdf  
Provenance: RFC Editor publication; original national standards and RFC dates are distinguished

RFC category: Informational | RFC stream: Independent Submission

Preserved in the original publisher format. RFC publication does not itself establish national approval or IETF endorsement; consult the document status statement.

Original URL: <https://www.rfc-editor.org/rfc/rfc8998.pdf>

[Preserved file](../sources/originals/S026-rfc8998.pdf) · 189,766 bytes · 13 PDF pages

Retrieved UTC: 2026-10-17T18:50:43.324478+00:00  
SHA-256: `6a8296ee227a22e5fdc8551e99833181bc206c79f949809506df5d6b24fbfecd`

### S034 — Announcement No.23: release of six cryptographic industry standards

Publisher: State Cryptography Administration of China (OSCCA)  
Document date: 2012-03-21  
Language: Chinese · Format: html  
Provenance: Original publisher

Contemporary announcement of industry standards; distinct from later GB/T national standards.

Original URL: <https://oscca.gov.cn/sca/xxgk/2012-03/21/content_1002392.shtml>

[Preserved file](../sources/web/S034-oscca-standards-announcement-2012.html) · 13,246 bytes

Retrieved UTC: 2026-10-17T18:50:44.307988+00:00  
SHA-256: `86b601282319c44cf068df65a3207a7fca7ca968a036134eb80a6993e99da9af`

### S035 — Official SM4 national-standard record: GB/T 32907-2016

Publisher: State Administration for Market Regulation / national standards platform  
Document date: 2016-08-29  
Language: Chinese · Format: html  
Provenance: Original publisher

Official metadata distinguishes issue date from implementation date. A dynamic page snapshot may not preserve all rendered fields.

Original URL: <https://std.samr.gov.cn/gb/search/gbDetailed?id=71F772D81199D3A7E05397BE0A0AB82A>

[Preserved file](../sources/web/S035-samr-sm4-record.html) · 70,676 bytes

Retrieved UTC: 2026-10-17T18:50:44.456635+00:00  
SHA-256: `dfb19daab1a72a95006e24d8dc1bd9ec1469b7b891d98a1ecb4b0c4107ede5a5`

### S036 — Official SM2 Part 1 national-standard record: GB/T 32918.1-2016

Publisher: State Administration for Market Regulation / national standards platform  
Document date: 2016-08-29  
Language: Chinese · Format: html  
Provenance: Original publisher

Official record: issue 2016-08-29, implementation 2017-03-01. These dates are not first invention or first classified use.

Original URL: <https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=3EE2FD47B962578070541ED468497C5B>

[Preserved file](../sources/web/S036-samr-sm2-record.html) · 24,217 bytes

Retrieved UTC: 2026-10-17T18:50:44.572374+00:00  
SHA-256: `4933070480f36247e5983d4cc776e58138908a048177231bb11d58a4725769e1`

### S037 — ZUC Algorithm Specification, Version 1.6

Publisher: ETSI/SAGE specification hosted by GSMA  
Document date: 2011-06-28  
Language: English · Format: pdf  
Provenance: Original publisher

Algorithm specification for 128-EEA3 and 128-EIA3. The 2019 upload path is distinct from the 2011 document date.

Original URL: <https://www.gsma.com/solutions-and-impact/technologies/security/wp-content/uploads/2019/05/eea3eia3zucv16>

[Preserved file](../sources/originals/S037-zuc-specification-2011.pdf) · 293,332 bytes · 18 PDF pages

Retrieved UTC: 2026-10-17T18:50:44.844568+00:00  
SHA-256: `07db149438c92b6931eb34708df81134c4fa9a89cb2e0802cb3dd2d59f8907ae`

### S050 — RFC 4357: Additional Cryptographic Algorithms for Use with GOST Algorithms

Publisher: RFC Editor; named document authors  
Document date: 2006-01  
Language: English · Format: text  
Provenance: RFC Editor publication; original national standards and RFC dates are distinguished

RFC category: Informational | RFC stream: Not stated in the preserved header

Preserved in the original publisher format. RFC publication does not itself establish national approval or IETF endorsement; consult the document status statement.

Original URL: <https://www.rfc-editor.org/rfc/rfc4357.txt>

[Preserved file](../sources/originals/S050-rfc4357.txt) · 114,564 bytes

Retrieved UTC: 2026-10-17T18:50:52.141462+00:00  
SHA-256: `384473bcec574b8934e45346006d91efaff7f92bdfd868ec3913cc713f6e21d2`

### S057 — RFC 7836: Guidelines on the Cryptographic Algorithms to Accompany GOST R 34.10-2012 and GOST R 34.11-2012

Publisher: RFC Editor; named document authors  
Document date: 2016-03  
Language: English · Format: text  
Provenance: Original publisher

RFC category: Informational | RFC stream: Independent Submission

Publication category and stream are recorded separately from national approval. The preserved edition may be updated by later RFCs; its header governs its publication status.

Original URL: <https://www.rfc-editor.org/rfc/rfc7836.txt>

[Preserved file](../sources/originals/S057-rfc7836.txt) · 57,463 bytes

Retrieved UTC: 2026-10-17T19:11:47.934571+00:00  
SHA-256: `f92f3197751c5defd87e54b383d399d27f316761c379403af24efc8471577731`

### S058 — RFC 8645: Re-keying Mechanisms for Symmetric Keys

Publisher: RFC Editor; named document authors  
Document date: 2019-08  
Language: English · Format: text  
Provenance: Original publisher

RFC category: Informational | RFC stream: IRTF

Publication category and stream are recorded separately from national approval. The preserved edition may be updated by later RFCs; its header governs its publication status.

Original URL: <https://www.rfc-editor.org/rfc/rfc8645.txt>

[Preserved file](../sources/originals/S058-rfc8645.txt) · 141,580 bytes

Retrieved UTC: 2026-10-17T19:11:47.935555+00:00  
SHA-256: `08bad083c340eaff1072f16b0f5f57cda8a5e832ad8b1cd8efa5467e837feb38`

### S059 — RFC 9058: Multilinear Galois Mode (MGM)

Publisher: RFC Editor; named document authors  
Document date: 2021-06  
Language: English · Format: pdf  
Provenance: Original publisher

RFC category: Informational | RFC stream: Independent Submission

Publication category and stream are recorded separately from national approval. The preserved edition may be updated by later RFCs; its header governs its publication status.

Original URL: <https://www.rfc-editor.org/rfc/rfc9058.pdf>

[Preserved file](../sources/originals/S059-rfc9058.pdf) · 173,239 bytes · 25 PDF pages

Retrieved UTC: 2026-10-17T19:11:47.936282+00:00  
SHA-256: `653bd6f4313468dea174690e05958a65b3fe203a706952042315e68e9902029a`

### S060 — RFC 9227: Using GOST Ciphers in ESP and IKEv2

Publisher: RFC Editor; named document authors  
Document date: 2022-03  
Language: English · Format: pdf  
Provenance: Original publisher

RFC category: Informational | RFC stream: Independent Submission

Publication category and stream are recorded separately from national approval. The preserved edition may be updated by later RFCs; its header governs its publication status.

Original URL: <https://www.rfc-editor.org/rfc/rfc9227.pdf>

[Preserved file](../sources/originals/S060-rfc9227.pdf) · 251,876 bytes · 22 PDF pages

Retrieved UTC: 2026-10-17T19:11:47.937205+00:00  
SHA-256: `32c405af711d13d97166e0fbab6a618da4cb996ea27b5e5166ab9c484666cd1c`

### S061 — RFC 9215: Using GOST Algorithms with the Internet X.509 PKI

Publisher: RFC Editor; named document authors  
Document date: 2022-03  
Language: English · Format: pdf  
Provenance: Original publisher

RFC category: Informational | RFC stream: Independent Submission

Publication category and stream are recorded separately from national approval. The preserved edition may be updated by later RFCs; its header governs its publication status.

Original URL: <https://www.rfc-editor.org/rfc/rfc9215.pdf>

[Preserved file](../sources/originals/S061-rfc9215.pdf) · 299,153 bytes · 38 PDF pages

Retrieved UTC: 2026-10-17T19:11:48.363866+00:00  
SHA-256: `2bcba999a1025a05fc23939136d5aa6326e350458e3575a74c7f25165f4dace3`

### S062 — RFC 9189: GOST Cipher Suites for TLS Version 1.2

Publisher: RFC Editor; named document authors  
Document date: 2022-03  
Language: English · Format: pdf  
Provenance: Original publisher

RFC category: Informational | RFC stream: Independent Submission

Publication category and stream are recorded separately from national approval. The preserved edition may be updated by later RFCs; its header governs its publication status.

Original URL: <https://www.rfc-editor.org/rfc/rfc9189.pdf>

[Preserved file](../sources/originals/S062-rfc9189.pdf) · 579,033 bytes · 92 PDF pages

Retrieved UTC: 2026-10-17T19:11:48.423981+00:00  
SHA-256: `c88bbba5b99aefe100deba848c0b41fc89dc2845ce8b79d6383e0ef710a0d8c0`

### S063 — RFC 9367: GOST Cipher Suites for TLS Version 1.3

Publisher: RFC Editor; named document authors  
Document date: 2023-02  
Language: English · Format: pdf  
Provenance: Original publisher

RFC category: Informational | RFC stream: Independent Submission

Publication category and stream are recorded separately from national approval. The preserved edition may be updated by later RFCs; its header governs its publication status.

Original URL: <https://www.rfc-editor.org/rfc/rfc9367.pdf>

[Preserved file](../sources/originals/S063-rfc9367.pdf) · 450,902 bytes · 71 PDF pages

Retrieved UTC: 2026-10-17T19:11:48.758423+00:00  
SHA-256: `f78461079a798f04737503fa382d1460dea4896fd8894f789a8a3fce2a673704`

### S064 — RFC 5280: Internet X.509 Public Key Infrastructure Certificate and CRL Profile

Publisher: RFC Editor; named document authors  
Document date: 2008-05  
Language: English · Format: text  
Provenance: Original publisher

RFC category: Standards Track | RFC stream: IETF (pre-explicit-stream header)

Publication category and stream are recorded separately from national approval. The preserved edition may be updated by later RFCs; its header governs its publication status.

Original URL: <https://www.rfc-editor.org/rfc/rfc5280.txt>

[Preserved file](../sources/originals/S064-rfc5280.txt) · 352,580 bytes

Retrieved UTC: 2026-10-17T19:11:48.891486+00:00  
SHA-256: `a2f2628c0a83b873fc4786abd921f9b2c02395954b655d190bf16b831633345d`

### S065 — RFC 8446: The Transport Layer Security (TLS) Protocol Version 1.3

Publisher: RFC Editor; named document authors  
Document date: 2018-08  
Language: English · Format: text  
Provenance: Original publisher

RFC category: Standards Track | RFC stream: IETF

Publication category and stream are recorded separately from national approval. The preserved edition may be updated by later RFCs; its header governs its publication status.

Original URL: <https://www.rfc-editor.org/rfc/rfc8446.txt>

[Preserved file](../sources/originals/S065-rfc8446.txt) · 337,736 bytes

Retrieved UTC: 2026-10-17T19:11:48.984017+00:00  
SHA-256: `47871bc8820a2c3b6ea89f061055577058862cf543686b82d10131239702b3bd`

### S066 — PKCS #11 Base Specification Version 3.0

Publisher: OASIS  
Document date: 2020-06-15  
Language: English · Format: pdf  
Provenance: Original publisher

Edition selected to match the archived Historical Mechanisms v3.0 (S001), not asserted to be the newest PKCS #11 edition.

Original URL: <https://docs.oasis-open.org/pkcs11/pkcs11-base/v3.0/os/pkcs11-base-v3.0-os.pdf>

[Preserved file](../sources/originals/S066-pkcs11-base-v3-2020.pdf) · 2,235,865 bytes · 167 PDF pages

Retrieved UTC: 2026-10-17T19:11:48.994501+00:00  
SHA-256: `fbb3a84657ad7c06c982b511cc9541e9ec08f5f10e4e07dc2e0efa71f8cc7cc8`

### S067 — SP 800-38B: The CMAC Mode for Authentication

Publisher: NIST  
Document date: 2005-05  
Language: English · Format: pdf  
Provenance: Original publisher

Edition: 2005 edition with 2016 updates | Revision: 2016-10-06

First issued May 2005; the preserved publisher PDF includes updates dated 2016-10-06.

Original URL: <https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-38B.pdf>

[Preserved file](../sources/originals/S067-nist-cmac.pdf) · 253,317 bytes · 21 PDF pages

Retrieved UTC: 2026-10-17T19:11:49.274110+00:00  
SHA-256: `da9dc0f1e1f08af917caf4a831a7497cf18997b8046353af89570a812f1ec5a2`

### S068 — SP 800-38C: The CCM Mode for Authentication and Confidentiality

Publisher: NIST  
Document date: 2004-05  
Language: English · Format: pdf  
Provenance: Original publisher

Edition: 2004 edition with 2007 errata | Revision: 2007-07-20

First issued May 2004; the preserved PDF states that errata were updated 2007-07-20.

Original URL: <https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-38c.pdf>

[Preserved file](../sources/originals/S068-nist-ccm.pdf) · 287,840 bytes · 27 PDF pages

Retrieved UTC: 2026-10-17T19:11:49.306060+00:00  
SHA-256: `16ec6f99424192757b5b9928a7dcf41817be3aaf85d48366740dfdf7c16db250`

### S069 — SP 800-38F: Methods for Key Wrapping

Publisher: NIST  
Document date: 2012-12  
Language: English · Format: pdf  
Provenance: Original publisher

Original URL: <https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-38F.pdf>

[Preserved file](../sources/originals/S069-nist-key-wrapping.pdf) · 289,262 bytes · 32 PDF pages

Retrieved UTC: 2026-10-17T19:11:49.310097+00:00  
SHA-256: `b8b1052755448e5ff3913ea09dc9b5ae47a97886752525a0cccfa024fb072fa8`

### S070 — Announcement No.21: release of the SM2 elliptic-curve public-key algorithm

Publisher: State Cryptography Administration of China  
Document date: 2010-12-17  
Language: Chinese · Format: html  
Provenance: Original publisher

Contemporary public release announcement; distinct from the later GM/T and GB/T standards.

Original URL: <https://www.sca.gov.cn/sca/xwdt/2010-12/17/content_1002386.shtml>

[Preserved file](../sources/web/S070-sm2-announcement-2010.html) · 12,790 bytes

Retrieved UTC: 2026-10-17T19:11:49.381748+00:00  
SHA-256: `27fdadba38fada46c3910c484f67ee1d1471fbc0ef58148b2c7ffd5d2b5db7d6`

### S071 — Announcement No.22: release of the SM3 hash algorithm

Publisher: State Cryptography Administration of China  
Document date: 2010-12-17  
Language: Chinese · Format: html  
Provenance: Original publisher

Original URL: <https://www.oscca.gov.cn/sca/xxgk/2010-12/17/content_1002389.shtml>

[Preserved file](../sources/web/S071-sm3-announcement-2010.html) · 12,696 bytes

Retrieved UTC: 2026-10-17T19:11:49.679498+00:00  
SHA-256: `d46328faff445c1769df34d5786d59512bc7983268e2db6db8794cdbec1947be`

### S072 — Announcement No.24: fourteen cryptographic industry standards, including SM2 application and certificate specifications

Publisher: State Cryptography Administration of China  
Document date: 2012-11-22  
Language: Chinese · Format: html  
Provenance: Original publisher

Original URL: <https://www.sca.gov.cn/sca/xxgk/2012-11/22/content_1002397.shtml>

[Preserved file](../sources/web/S072-sm2-application-standards-2012.html) · 14,017 bytes

Retrieved UTC: 2026-10-17T19:11:50.224563+00:00  
SHA-256: `2177d6207dc89b9a3259b6513af341073c10ae922e3acff37cc646bf481dbc44`

### S073 — Announcement No.45: 2023 cryptographic industry-standard revisions

Publisher: State Cryptography Administration of China  
Document date: 2023-12-23  
Language: Chinese · Format: html  
Provenance: Original publisher

Web announcement date is separate from individual standard issue dates and the stated 2024-06-01 implementation date.

Original URL: <https://oscca.gov.cn/sca/xxgk/2023-12/23/content_1061160.shtml>

[Preserved file](../sources/web/S073-china-standards-revisions-2023.html) · 15,769 bytes

Retrieved UTC: 2026-10-17T19:11:50.240764+00:00  
SHA-256: `1dd01569604b595616565886f8bb56be225df31faab45c4f645c2aa2a048845e`

### S074 — GM/T 0009-2012: SM2 application specification, three-page booklet scan

Publisher: State Cryptography Administration of China; preserved copy  
Document date: 2012-11-22  
Language: Chinese · Format: pdf  
Provenance: Original national-language standard scan preserved by Antpedia

Extent: Three PDF pages of imposed booklet images; incomplete body

Third-party three-page booklet scan. The images contain the covers, contents, foreword, and printed body pages 6 and 7; the earlier body pages are absent. This is not a complete copy of GM/T 0009-2012. The cover states issue and implementation on 2012-11-22; S073 records a later revision.

Original URL: <https://img.antpedia.com/standard/files/pdfs_ora/CN-GM/c8e/GM_T%200009-2012_5625.pdf>

[Preserved file](../sources/originals/S074-sm2-application-specification-2012.pdf) · 224,289 bytes · 3 PDF pages

Retrieved UTC: 2026-10-17T19:11:51.622298+00:00  
SHA-256: `572b0f9314e38c0f74f1bfdd562b8083fbef4e4cb1c334887021d1edea7cb9b9`

### S075 — ETSI TS 135 221 V19.0.0: EEA3 and EIA3 specifications, Release 19

Publisher: ETSI / 3GPP  
Document date: 2025-10  
Language: English · Format: pdf  
Provenance: Original publisher

Edition: 19.0.0 / Release 19

The ETSI wrapper and its normative references are distinguished from the separately preserved detailed ETSI/SAGE algorithm document.

Original URL: <https://www.etsi.org/deliver/etsi_ts/135200_135299/135221/19.00.00_60/ts_135221v190000p.pdf>

[Preserved file](../sources/originals/S075-etsi-ts135221-release19.pdf) · 86,592 bytes · 8 PDF pages

Retrieved UTC: 2026-10-17T19:11:52.123284+00:00  
SHA-256: `c5a9a292787d2e653beb711d4dd1ef0345707e81caf13740d3bbefb8a606523f`

### S076 — 128-EEA3 and 128-EIA3 Specification, Version 1.8

Publisher: ETSI/SAGE; hosted by GSMA  
Document date: 2019-01-24  
Language: English · Format: pdf  
Provenance: Original publisher

Edition: 1.8

Document 1 complements the ZUC core specification S037. The 2019 upload directory is not used as evidence for earlier revision dates.

Original URL: <https://www.gsma.com/solutions-and-impact/technologies/security/wp-content/uploads/2019/05/EEA3_EIA3_specification_v1_8.pdf>

[Preserved file](../sources/originals/S076-eea3-eia3-specification-v18.pdf) · 236,953 bytes · 16 PDF pages

Retrieved UTC: 2026-10-17T19:11:52.527124+00:00  
SHA-256: `b65d11ffa74c87ae6c898b48df5b36fe838297aede9c819bacb782c43695b974`

### S077 — CRYPTREC Ciphers List: current and historical edition index

Publisher: CRYPTREC / Japanese government agencies  
Document date: not printed / not verified  
Language: English · Format: html  
Provenance: Original publisher

Raw snapshot of the official index; revised and historical lists are preserved separately.

Original URL: <https://www.cryptrec.go.jp/en/list.html>

[Preserved file](../sources/web/S077-cryptrec-list-index.html) · 11,658 bytes

Retrieved UTC: 2026-10-17T19:11:52.563131+00:00  
SHA-256: `2d99652dcad14e3ac30f144425faf011466aa7ee4872cd2cd1cfe2223bfc2c9a`

### S078 — CRYPTREC Ciphers List, LS-0001-2022R2

Publisher: CRYPTREC  
Document date: 2026-03-30  
Language: Japanese · Format: pdf  
Provenance: Original publisher

Edition: LS-0001-2022R2 | Initial issue: 2023-03-30 | Revision: 2026-03-30

The identifier contains 2022. The cover dates the list family to 2023-03-30 and this revision to 2026-03-30. Preserve its three distinct list categories.

Original URL: <https://www.cryptrec.go.jp/list/cryptrec-ls-0001-2022r2.pdf>

[Preserved file](../sources/originals/S078-cryptrec-list-2026.pdf) · 239,893 bytes · 7 PDF pages

Retrieved UTC: 2026-10-17T19:11:52.739325+00:00  
SHA-256: `a492a5dce043b51cc0afd064a0bf7202518b31c65fb808bcc492f9cd4f0b32e3`

### S079 — CRYPTREC Ciphers List, LS-0001-2012, original 2013 edition

Publisher: CRYPTREC  
Document date: 2013-03-01  
Language: Japanese · Format: pdf  
Provenance: Original publisher

Edition: LS-0001-2012

Historical original list; recommendation categories and edition are kept separate from the later revised list.

Original URL: <https://www.cryptrec.go.jp/list/cryptrec-ls-0001-2012.pdf>

[Preserved file](../sources/originals/S079-cryptrec-list-2013.pdf) · 124,137 bytes · 4 PDF pages

Retrieved UTC: 2026-10-17T19:11:52.780752+00:00  
SHA-256: `b47b0f9477129812d6af321eed4bed99c0a66e988d8a8d50618fa76510cb0615`

### S080 — Standards for Cryptographic Strength Requirements, LS-0003-2022R1

Publisher: CRYPTREC  
Document date: 2023-03-30  
Language: Japanese · Format: pdf  
Provenance: Original publisher

Edition: LS-0003-2022R1 / Ver. 1.0 | Initial issue: 2022-07-01 | Revision: 2023-03-30

The revision table records first publication on 2022-07-01 and corrections on 2023-03-30, including correction of the publication month. The acquired cover still prints March 2022. These conflicting internal date fields are retained explicitly.

Original URL: <https://www.cryptrec.go.jp/list/cryptrec-ls-0003-2022r1.pdf>

[Preserved file](../sources/originals/S080-cryptrec-strength-requirements.pdf) · 1,424,925 bytes · 42 PDF pages

Retrieved UTC: 2026-10-17T19:11:53.774667+00:00  
SHA-256: `f249b7a5f880ce4bd239972de945bc8d5375912a98bf9d5e938e3293154cdced`

### S081 — TR-02102-1: Cryptographic Mechanisms, Recommendations and Key Lengths

Publisher: German Federal Office for Information Security (BSI)  
Document date: 2026-01-23  
Language: English · Format: pdf  
Provenance: Original publisher

Edition: 2026-01

Version 2026-01; cover states as of 2026-01-23. General recommendations do not constitute approval of a particular classified product.

Original URL: <https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TG02102/BSI-TR-02102-1.pdf?__blob=publicationFile&v=15>

[Preserved file](../sources/originals/S081-bsi-tr02102-1.pdf) · 568,388 bytes · 92 PDF pages

Retrieved UTC: 2026-10-17T19:11:53.879999+00:00  
SHA-256: `f601cdf25c000b431573a307a3c125f3c51d301897089e7e63dde0449367a62a`

### S082 — TR-02102-2: Use of Transport Layer Security (TLS)

Publisher: German Federal Office for Information Security (BSI)  
Document date: 2026-01-27  
Language: English · Format: pdf  
Provenance: Original publisher

Edition: 2026-01

Document history dates version 2026-01 to 2026-01-27.

Original URL: <https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TG02102/BSI-TR-02102-2.pdf?__blob=publicationFile&v=11>

[Preserved file](../sources/originals/S082-bsi-tr02102-2-tls.pdf) · 758,922 bytes · 18 PDF pages

Retrieved UTC: 2026-10-17T19:11:53.933737+00:00  
SHA-256: `a7f55c3403d45719287415d2698bf51e629aafe841e2e9867e8afe8749d238e5`

### S083 — TR-02102-3: Use of IPsec and IKEv2

Publisher: German Federal Office for Information Security (BSI)  
Document date: 2026-01-27  
Language: English · Format: pdf  
Provenance: Original publisher

Edition: 2026-01

Document history dates version 2026-01 to 2026-01-27.

Original URL: <https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TG02102/BSI-TR-02102-3.pdf?__blob=publicationFile&v=10>

[Preserved file](../sources/originals/S083-bsi-tr02102-3-ipsec.pdf) · 724,281 bytes · 18 PDF pages

Retrieved UTC: 2026-10-17T19:11:53.950547+00:00  
SHA-256: `ee6cf28a1b7fbc79b60dd2a913a905e99e3a246b0796cff894a41e22207d6bdc`

### S084 — KCMVP: algorithms subject to cryptographic module validation

Publisher: Korea Internet and Security Agency (KISA)  
Document date: not printed / not verified  
Language: Korean · Format: html  
Provenance: Original publisher

An eligibility/validation-reference page, not a certificate for a particular implementation. Acquisition may be unavailable; any failure remains explicit.

Original URL: <https://seed.kisa.or.kr/kisa/kcmvp/EgovVerification.do>

**Not preserved:** failed; HTTPError: HTTP Error 503: Service Unavailable  
Attempt UTC: 2026-10-20T15:36:04.711250+00:00

### S085 — KCMVP: cryptographic module testing and validation procedures

Publisher: Korea Internet and Security Agency (KISA)  
Document date: not printed / not verified  
Language: Korean · Format: html  
Provenance: Original publisher

Original URL: <https://seed.kisa.or.kr/kisa/kcmvp/reference.do>

**Not preserved:** failed; HTTPError: HTTP Error 503: Service Unavailable  
Attempt UTC: 2026-10-20T15:36:06.117019+00:00

### S086 — RFC 5932: Camellia Cipher Suites for TLS

Publisher: RFC Editor; named document authors  
Document date: 2010-06  
Language: English · Format: text  
Provenance: Original publisher

RFC category: Standards Track | RFC stream: IETF

Publication category and stream are recorded separately from national approval. The preserved edition may be updated by later RFCs; its header governs its publication status.

Original URL: <https://www.rfc-editor.org/rfc/rfc5932.txt>

[Preserved file](../sources/originals/S086-rfc5932.txt) · 11,949 bytes

Retrieved UTC: 2026-10-17T19:11:55.980731+00:00  
SHA-256: `4da0b39f346d7807a210a6c4b88ea5780a74267f256547cc5cd6b1f64976bb5d`

### S087 — RFC 4312: The Camellia Cipher Algorithm and Its Use With IPsec

Publisher: RFC Editor; named document authors  
Document date: 2005-12  
Language: English · Format: text  
Provenance: Original publisher

RFC category: Standards Track | RFC stream: IETF (pre-explicit-stream header)

Publication category and stream are recorded separately from national approval. The preserved edition may be updated by later RFCs; its header governs its publication status.

Original URL: <https://www.rfc-editor.org/rfc/rfc4312.txt>

[Preserved file](../sources/originals/S087-rfc4312.txt) · 15,980 bytes

Retrieved UTC: 2026-10-17T19:11:56.250552+00:00  
SHA-256: `3a1034a459d9be0b6195576b1171b413e8556967e7126b692a617a9b4fa38988`

### S088 — RFC 4162: Addition of SEED Cipher Suites to TLS

Publisher: RFC Editor; named document authors  
Document date: 2005-08  
Language: English · Format: text  
Provenance: Original publisher

RFC category: Standards Track | RFC stream: IETF (pre-explicit-stream header)

Publication category and stream are recorded separately from national approval. The preserved edition may be updated by later RFCs; its header governs its publication status.

Original URL: <https://www.rfc-editor.org/rfc/rfc4162.txt>

[Preserved file](../sources/originals/S088-rfc4162.txt) · 10,578 bytes

Retrieved UTC: 2026-10-17T19:11:56.447889+00:00  
SHA-256: `ae3456638cacf62adc60577867f3f13b0c33ecb02d70ac7ca83ccaa209b1b67e`

### S089 — RFC 4196: The SEED Cipher Algorithm and Its Use with IPsec

Publisher: RFC Editor; named document authors  
Document date: 2005-10  
Language: English · Format: text  
Provenance: Original publisher

RFC category: Standards Track | RFC stream: IETF (pre-explicit-stream header)

Publication category and stream are recorded separately from national approval. The preserved edition may be updated by later RFCs; its header governs its publication status.

Original URL: <https://www.rfc-editor.org/rfc/rfc4196.txt>

[Preserved file](../sources/originals/S089-rfc4196.txt) · 22,587 bytes

Retrieved UTC: 2026-10-17T19:11:56.634517+00:00  
SHA-256: `fcd316975dc1abe1c9fdcfc48d0d29f9caca5858075ef4882a99d40abbd97d9a`

### S090 — RFC 6209: Addition of the ARIA Cipher Suites to TLS

Publisher: RFC Editor; named document authors  
Document date: 2011-04  
Language: English · Format: text  
Provenance: Original publisher

RFC category: Informational | RFC stream: IETF

Publication category and stream are recorded separately from national approval. The preserved edition may be updated by later RFCs; its header governs its publication status.

Original URL: <https://www.rfc-editor.org/rfc/rfc6209.txt>

[Preserved file](../sources/originals/S090-rfc6209.txt) · 19,501 bytes

Retrieved UTC: 2026-10-17T19:11:56.645443+00:00  
SHA-256: `bec379ec5fe8df5faa17315146c2208bdf901f0cbfdad0a2f5010243d813deeb`

### S091 — RFC 8269: The ARIA Algorithm and Its Use with SRTP

Publisher: RFC Editor; named document authors  
Document date: 2017-10  
Language: English · Format: text  
Provenance: Original publisher

RFC category: Informational | RFC stream: IETF

Publication category and stream are recorded separately from national approval. The preserved edition may be updated by later RFCs; its header governs its publication status.

Original URL: <https://www.rfc-editor.org/rfc/rfc8269.txt>

[Preserved file](../sources/originals/S091-rfc8269.txt) · 39,285 bytes

Retrieved UTC: 2026-10-17T19:13:43.412389+00:00  
SHA-256: `f2a4fa93fc63c6e94a1a9df148970b9759cdee770f98cb38cc706dee650e921d`

### S092 — 128-EEA3 and 128-EIA3 Implementer Test Data, Version 1.1

Publisher: ETSI/SAGE; hosted by GSMA  
Document date: 2011-01-04  
Language: English · Format: pdf  
Provenance: Original publisher

Edition: 1.1

Cover date is 2011-01-04; the 2019 hosting directory is not the document publication date. The preface expressly says that passing these tests does not guarantee a correct implementation.

Original URL: <https://www.gsma.com/solutions-and-impact/technologies/security/wp-content/uploads/2019/05/eea3eia3testdatav11.pdf>

[Preserved file](../sources/originals/S092-eea3-eia3-implementer-tests.pdf) · 227,188 bytes · 21 PDF pages

Retrieved UTC: 2026-10-17T19:11:56.830113+00:00  
SHA-256: `65b461c84daac4f9c7e831b739ca33792e25fdcbcf67e2e6befa60e4a58eea82`

### S093 — Design and Evaluation Report: 128-EEA3, 128-EIA3 and ZUC, Version 2.0

Publisher: ETSI/SAGE; hosted by GSMA  
Document date: 2011-09-09  
Language: English · Format: pdf  
Provenance: Original publisher

Edition: 2.0

Final-deliverable edition dated 2011-09-09. Its history records a first public release on 2010-08-11 and subsequent algorithm revisions.

Original URL: <https://www.gsma.com/solutions-and-impact/technologies/security/wp-content/uploads/2019/05/EEA3_EIA3_Design_Evaluation_v2_0.pdf>

[Preserved file](../sources/originals/S093-zuc-design-evaluation.pdf) · 1,027,545 bytes · 43 PDF pages

Retrieved UTC: 2026-10-17T19:11:56.988033+00:00  
SHA-256: `f31c51cad773fff898d3fd6c6246629eca73cba8c0d9b893b451eca9d99165ee`

### S094 — CRYPTREC e-Government Recommended Ciphers List, LS-0001-2002R1

Publisher: CRYPTREC  
Document date: 2005-10-12  
Language: Japanese · Format: pdf  
Provenance: Original publisher

Edition: LS-0001-2002R1 | Initial issue: 2003-02-20 | Revision: 2005-10-12

List cover: 2003-02-20. Appended correction record: 2005-10-12, changing a Triple-DES specification reference from FIPS 46-3 to SP 800-67. This is the historical list with that correction, not a fresh 2005 selection.

Original URL: <https://www.cryptrec.go.jp/list/cryptrec-ls-0001-2002r1.pdf>

[Preserved file](../sources/originals/S094-cryptrec-legacy-list.pdf) · 153,555 bytes · 3 PDF pages

Retrieved UTC: 2026-10-17T19:11:57.044703+00:00  
SHA-256: `953e17ad183ea28e21052ec106eea85703bb0381ee1e2af7d8aee401828c0dca`

### S095 — TR-02102-4: Use of Secure Shell (SSH)

Publisher: German Federal Office for Information Security (BSI)  
Document date: 2026-01-27  
Language: English · Format: pdf  
Provenance: Original publisher

Edition: 2026-01

Document history dates version 2026-01 to 2026-01-27.

Original URL: <https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TG02102/BSI-TR-02102-4.pdf?__blob=publicationFile&v=11>

[Preserved file](../sources/originals/S095-bsi-tr02102-4-ssh.pdf) · 639,452 bytes · 12 PDF pages

Retrieved UTC: 2026-10-17T19:11:57.110794+00:00  
SHA-256: `9338643a2c5019bf1c819c759b9c1e903203f0db79e5ecb087b0ace0613f4de8`

### S096 — SM2 elliptic-curve public-key cryptographic algorithm: original release, Parts 1–4

Publisher: State Cryptography Administration of China  
Document date: 2010-12  
Language: Chinese · Format: pdf  
Provenance: Original publisher

Extent: 93 PDF pages; four separately titled parts combined

Official attachment to the release announcement of 2010-12-17 (S070). The four part covers are dated December 2010: general, signature, key exchange, and public-key encryption. These are the original release texts, not the later GB/T editions.

Original URL: <https://www.sca.gov.cn/sca/xwdt/2010-12/17/1002386/files/b791a9f908bb4803875ab6aeeb7b4e03.pdf>

[Preserved file](../sources/originals/S096-sm2-official-release-a.pdf) · 945,731 bytes · 93 PDF pages

Retrieved UTC: 2026-10-17T19:14:35.055523+00:00  
SHA-256: `727ad5611ccc6efeef9b184b39687a5ce72540eea5a9a58bf99685d881a9962a`

### S097 — SM2 recommended elliptic-curve parameters: original release attachment

Publisher: State Cryptography Administration of China  
Document date: not printed / not verified  
Language: Chinese · Format: pdf  
Provenance: Original publisher

Extent: One PDF page

Undated one-page parameter sheet directly linked by the official 2010-12-17 announcement (S070). The announcement supplies the dated release evidence; the sheet itself has no printed date.

Original URL: <https://www.sca.gov.cn/sca/xwdt/2010-12/17/1002386/files/b965ce832cc34bc191cb1cde446b860d.pdf>

[Preserved file](../sources/originals/S097-sm2-official-release-b.pdf) · 22,552 bytes · 1 PDF pages

Retrieved UTC: 2026-10-17T19:14:35.057158+00:00  
SHA-256: `a2b7aa352aa218f46116879748e87596ce45a5a80aef8036fc6e3ab151d2b90c`

### S098 — SM3 Cryptographic Hash Algorithm: original official release

Publisher: State Cryptography Administration of China  
Document date: 2010-12  
Language: Chinese · Format: pdf  
Provenance: Original publisher

Extent: 13 PDF pages

Cover dated December 2010; official attachment to the 2010-12-17 announcement (S071). This is the original release specification, not a later GM/T or GB/T edition.

Original URL: <https://www.oscca.gov.cn/sca/xxgk/2010-12/17/1002389/files/302a3ada057c4a73830536d03e683110.pdf>

[Preserved file](../sources/originals/S098-sm3-official-release.pdf) · 103,677 bytes · 13 PDF pages

Retrieved UTC: 2026-10-17T19:14:35.056622+00:00  
SHA-256: `6f35d1870b8b137f70f309270d7c60c830a20a678f6bdedf33cb6008d00ab38e`

### S099 — Cryptographic module validation programme overview

Publisher: Korea Internet and Security Agency (KISA)  
Document date: not printed / not verified  
Language: Korean · Format: html  
Provenance: Original publisher

Official programme overview on KISA's main host, distinct from the unavailable seed.kisa.or.kr detail pages.

Original URL: <https://www.kisa.or.kr/1040209>

**Not preserved:** failed; HTTPError: HTTP Error 503: Service Unavailable  
Attempt UTC: 2026-10-20T15:36:07.447820+00:00

### S100 — RFC Series index: publisher XML metadata snapshot

Publisher: RFC Editor  
Document date: not printed / not verified  
Language: English · Format: xml  
Provenance: Original publisher XML; dated acquisition snapshot

Extent: Publisher XML index snapshot

Mutable publisher index acquired on 2026-10-20. Stream and current-status fields are observations at retrieval; they do not alter the category printed in an original RFC.

Original URL: <https://www.rfc-editor.org/rfc/rfc-index.xml>

[Preserved file](../sources/originals/S100-rfc-index.xml) · 13,732,842 bytes

Retrieved UTC: 2026-10-20T15:42:47.878865+00:00  
SHA-256: `ab81329d975096f37b9a8a85cfb8b593e5c249b65f7a9707cd1ec45d3edf4099`

### S101 — GOST R 34.13-2015: Modes of operation for block ciphers, Russian official-edition scan

Publisher: Rosstandart; Standartinform  
Document date: 2016-03-28  
Language: Russian · Format: pdf  
Provenance: Primary Russian standard reproduced by the Meganorm mirror; host-added advertising text remains unchanged

Edition: GOST R 34.13-2015 / Standartinform 2016 printing | Initial issue: 2015-06-19 | Effective: 2016-01-01 | Printing: 2016-03-28 | Extent: 29 PDF pages: cover, preliminaries, printed body pages 1–23 and imprint

Foreword cites approval order 750-st of 2015-06-19; body states effective 2016-01-01. Imprint says signed for printing 2016-03-28. Meganorm mirror contains added advertising/link text; it is a reproduced standard, not an authenticated publisher download. The separate 2018 erratum is not silently applied.

Original URL: <https://meganorm.ru/Data2/1/4293762/4293762703.pdf>

[Preserved file](../sources/originals/S101-gost-modes-ru.pdf) · 606,856 bytes · 29 PDF pages

Retrieved UTC: 2026-10-20T15:41:13.464877+00:00  
SHA-256: `de71f9360586a492986bb5f984950b57805febc31accc0894174cce7f57e7d0f`

### S102 — Correction to GOST R 34.13-2015, IUS No. 6/2018

Publisher: Rosstandart / national standards information bulletin  
Document date: 2018-06  
Language: Russian · Format: pdf  
Provenance: Primary correction notice reproduced by the Meganorm mirror

Edition: IUS No. 6/2018 | Revision: 2018-06 | Extent: 1 PDF pages

One-page correction to Section 5.3.2, rule (7). Month comes from IUS No. 6/2018; no exact issue day is asserted. Mirror contains added advertising/link text.

Original URL: <https://meganorm.ru/Data2/0/4294800/4294800102.pdf>

[Preserved file](../sources/originals/S102-gost-modes-erratum.pdf) · 18,242 bytes · 1 PDF pages

Retrieved UTC: 2026-10-20T15:41:13.465939+00:00  
SHA-256: `d8e9e45e18d8675dddf05d120cf18fa88887255cfc29815aad7e3d006c9938b9`

### S103 — Official Rosstandart record for GOST R 34.13-2015 and its correction

Publisher: Rosstandart / Institute of Standardization  
Document date: not printed / not verified  
Language: Russian · Format: html  
Provenance: Original publisher

Effective: 2016-01-01 | Extent: Raw HTML snapshot; linked assets not bundled

Live catalogue metadata, not a dated copy of the standard itself. Lists order 750-st dated 2015-06-19, effective 2016-01-01 and IUS 6-2018 correction.

Original URL: <https://protect.gost.ru/gost/details/ed723f12-1f11-4bbb-b09b-86c455a393db>

[Preserved file](../sources/web/S103-gost-modes-official-record.html) · 87,658 bytes

Retrieved UTC: 2026-10-20T15:41:13.467034+00:00  
SHA-256: `353af593617336f82de902d2b9be2183d010757082e0fd67e5a6e00cc345b6e7`

### S104 — R 1323565.1.005-2017: Permissible data volumes under one key for GOST block-cipher modes

Publisher: Rosstandart; Standartinform  
Document date: 2017  
Language: Russian · Format: pdf  
Provenance: Primary Russian recommendation reproduced by the Meganorm mirror

Edition: R 1323565.1.005-2017 | Initial issue: 2017-10-25 | Effective: 2018-04-01 | Extent: 8 PDF pages

Cover printing year 2017; foreword cites order 1518-st of 2017-10-25; body states effective 2018-04-01. A standardization recommendation, distinct from a product certificate. Mirror-added advertising text remains in the acquired PDF.

Original URL: <https://meganorm.ru/Data2/1/4293741/4293741713.pdf>

[Preserved file](../sources/originals/S104-gost-key-volume.pdf) · 126,643 bytes · 8 PDF pages

Retrieved UTC: 2026-10-20T15:41:15.621639+00:00  
SHA-256: `3afe34287fca0c08812ceff61e22a9a1aaa03675e520ed333993a4bc9555a989`

### S105 — RFC 4490: Using the GOST 28147-89, GOST R 34.11-94, GOST R 34.10-94, and GOST R 34.10-2001 Algorithms with Cryptographic Message Syntax (CMS)

Publisher: RFC Editor; named document authors  
Document date: 2006-05  
Language: English · Format: text  
Provenance: Original publisher

Edition: RFC 4490 | RFC category: Standards Track | RFC stream: IETF | RFC status at issue: PROPOSED STANDARD | Status in acquired index: PROPOSED STANDARD | Extent: 29 publisher-index pages; original RFC text

Category is transcribed from the preserved original header. Stream and publisher status fields are cross-checked against the separately preserved RFC index (S100), entry RFC4490. They establish RFC publication provenance, not national approval or implementation certification.

Original URL: <https://www.rfc-editor.org/rfc/rfc4490.txt>

[Preserved file](../sources/originals/S105-rfc4490.txt) · 54,912 bytes

Retrieved UTC: 2026-10-20T15:37:46.105890+00:00  
SHA-256: `c1391aca412ec468dd584196f0ba8e7f0ccdbaf49e3a83b7d76ebd304f5c8f45`

### S106 — RFC 4491: Using the GOST R 34.10-94, GOST R 34.10-2001, and GOST R 34.11-94 Algorithms with the Internet X.509 Public Key Infrastructure Certificate and CRL Profile

Publisher: RFC Editor; named document authors  
Document date: 2006-05  
Language: English · Format: text  
Provenance: Original publisher

Edition: RFC 4491 | RFC category: Standards Track | RFC stream: IETF | RFC status at issue: PROPOSED STANDARD | Status in acquired index: PROPOSED STANDARD | Extent: 20 publisher-index pages; original RFC text

Category is transcribed from the preserved original header. Stream and publisher status fields are cross-checked against the separately preserved RFC index (S100), entry RFC4491. They establish RFC publication provenance, not national approval or implementation certification. The index snapshot does not mark this RFC obsoleted; RFC 9215 separately addresses the 2012 GOST algorithms. The two profiles must not be silently merged.

Original URL: <https://www.rfc-editor.org/rfc/rfc4491.txt>

[Preserved file](../sources/originals/S106-rfc4491.txt) · 39,095 bytes

Retrieved UTC: 2026-10-20T15:37:46.107768+00:00  
SHA-256: `39f1d26e869fb99e4615c0bc4cfe6a8b44aaca0b28f7f99f45d28658da89eb6e`

### S107 — RFC 9337: Generating Password-Based Keys Using the GOST Algorithms

Publisher: RFC Editor; named document authors  
Document date: 2022-12  
Language: English · Format: text  
Provenance: Original publisher

Edition: RFC 9337 | RFC category: Informational | RFC stream: Independent Submission | RFC status at issue: INFORMATIONAL | Status in acquired index: INFORMATIONAL | Extent: 14 publisher-index pages; original RFC text

Category is transcribed from the preserved original header. Stream and publisher status fields are cross-checked against the separately preserved RFC index (S100), entry RFC9337. They establish RFC publication provenance, not national approval or implementation certification.

Original URL: <https://www.rfc-editor.org/rfc/rfc9337.txt>

[Preserved file](../sources/originals/S107-rfc9337.txt) · 28,990 bytes

Retrieved UTC: 2026-10-20T15:37:46.103313+00:00  
SHA-256: `4af753ad9ca1056af97d7a011f8874b435b62bc42d004f063b79259c858253c1`

### S108 — RFC 9548: Generating Transport Key Containers (PFX) Using the GOST Algorithms

Publisher: RFC Editor; named document authors  
Document date: 2024-05  
Language: English · Format: text  
Provenance: Original publisher

Edition: RFC 9548 | RFC category: Informational | RFC stream: Independent Submission | RFC status at issue: INFORMATIONAL | Status in acquired index: INFORMATIONAL | Extent: 24 publisher-index pages; original RFC text

Category is transcribed from the preserved original header. Stream and publisher status fields are cross-checked against the separately preserved RFC index (S100), entry RFC9548. They establish RFC publication provenance, not national approval or implementation certification.

Original URL: <https://www.rfc-editor.org/rfc/rfc9548.txt>

[Preserved file](../sources/originals/S108-rfc9548.txt) · 52,834 bytes

Retrieved UTC: 2026-10-20T15:38:40.965686+00:00  
SHA-256: `43a2fac0561542aaa2d743a8897dc99c1b10413ddfedaa2f36d265a501d09e55`

### S109 — GM/T 0009-2012: SM2 cryptography algorithm application specification (Chinese scan)

Publisher: State Cryptography Administration of China; Standards Press of China  
Document date: 2012-11-22  
Language: Chinese · Format: pdf  
Provenance: Primary Chinese standard reproduced by the guanzhi/GM-Standards mirror; not a publisher-hosted or translated edition

Edition: GM/T 0009-2012 | Initial issue: 2012-11-22 | Effective: 2012-11-22 | Printing: 2013-01 | Extent: 12 PDF pages

Chinese national-language standard scan hosted by guanzhi/GM-Standards on GitHub, pinned to commit 402e57ed1c4002e3262978061b4f490b5e9ffc65. Cover identifies GM/T 0009-2012 and prints issue/effective dates 2012-11-22. Host filenames and mirror commit dates are not issue or approval dates. Final imprint identifies the first edition and first printing as January 2013, distinct from the 2012 standard issue date. This 12-page scan includes covers, contents, foreword, introduction and all printed body pages 1–7; it fills the omissions in S074. S074 remains preserved as the earlier incomplete acquisition.

Original URL: <https://raw.githubusercontent.com/guanzhi/GM-Standards/402e57ed1c4002e3262978061b4f490b5e9ffc65/GMT%E5%AF%86%E7%A0%81%E8%A1%8C%E6%A0%87/GMT%200009-2012%20SM2%E5%AF%86%E7%A0%81%E7%AE%97%E6%B3%95%E4%BD%BF%E7%94%A8%E8%A7%84%E8%8C%83%20.pdf>

[Preserved file](../sources/originals/S109-gmt0009-mirror.pdf) · 4,128,321 bytes · 12 PDF pages

Retrieved UTC: 2026-10-20T15:38:38.797048+00:00  
SHA-256: `281abef0ae055ef3f40aa28b3e63daf9d1d6b209125fe2ecd321311582ffd029`

### S110 — GM/T 0010-2012: SM2 cryptography message syntax specification (Chinese scan)

Publisher: State Cryptography Administration of China; Standards Press of China  
Document date: 2012-11-22  
Language: Chinese · Format: pdf  
Provenance: Primary Chinese standard reproduced by the guanzhi/GM-Standards mirror; not a publisher-hosted or translated edition

Edition: GM/T 0010-2012 | Initial issue: 2012-11-22 | Effective: 2012-11-22 | Printing: 2013-01 | Extent: 14 PDF pages

Chinese national-language standard scan hosted by guanzhi/GM-Standards on GitHub, pinned to commit 402e57ed1c4002e3262978061b4f490b5e9ffc65. Cover identifies GM/T 0010-2012 and prints issue/effective dates 2012-11-22. Host filenames and mirror commit dates are not issue or approval dates. Final imprint identifies the first edition and first printing as January 2013, distinct from the 2012 standard issue date.

Original URL: <https://raw.githubusercontent.com/guanzhi/GM-Standards/402e57ed1c4002e3262978061b4f490b5e9ffc65/GMT%E5%AF%86%E7%A0%81%E8%A1%8C%E6%A0%87/GMT%200010-2012%20SM2%E5%AF%86%E7%A0%81%E7%AE%97%E6%B3%95%E5%8A%A0%E5%AF%86%E7%AD%BE%E5%90%8D%E6%B6%88%E6%81%AF%E8%AF%AD%E6%B3%95%E8%A7%84%E8%8C%83.pdf>

[Preserved file](../sources/originals/S110-gmt0010-mirror.pdf) · 5,170,500 bytes · 14 PDF pages

Retrieved UTC: 2026-10-20T15:38:38.796117+00:00  
SHA-256: `34acf1e833f4a03b66ff1fa27c6081533f2120d22931b613d04ef9255886429b`

### S111 — GM/T 0014-2012: Digital certificate authentication system cryptography protocol specification (Chinese scan)

Publisher: State Cryptography Administration of China; Standards Press of China  
Document date: 2012-11-22  
Language: Chinese · Format: pdf  
Provenance: Primary Chinese standard reproduced by the guanzhi/GM-Standards mirror; not a publisher-hosted or translated edition

Edition: GM/T 0014-2012 | Initial issue: 2012-11-22 | Effective: 2012-11-22 | Printing: 2013-01 | Extent: 58 PDF pages

Chinese national-language standard scan hosted by guanzhi/GM-Standards on GitHub, pinned to commit 402e57ed1c4002e3262978061b4f490b5e9ffc65. Cover identifies GM/T 0014-2012 and prints issue/effective dates 2012-11-22. Host filenames and mirror commit dates are not issue or approval dates. Final imprint identifies the first edition and first printing as January 2013, distinct from the 2012 standard issue date.

Original URL: <https://raw.githubusercontent.com/guanzhi/GM-Standards/402e57ed1c4002e3262978061b4f490b5e9ffc65/GMT%E5%AF%86%E7%A0%81%E8%A1%8C%E6%A0%87/GMT%200014-2012%20%E6%95%B0%E5%AD%97%E8%AF%81%E4%B9%A6%E8%AE%A4%E8%AF%81%E7%B3%BB%E7%BB%9F%E5%AF%86%E7%A0%81%E5%8D%8F%E8%AE%AE%E8%A7%84%E8%8C%83.pdf>

[Preserved file](../sources/originals/S111-gmt0014-mirror.pdf) · 30,400,068 bytes · 58 PDF pages

Retrieved UTC: 2026-10-20T15:38:38.798362+00:00  
SHA-256: `2bb1aa39225d13d036d1cee761a4da12b5a49e0a31e296cddba83037c362ae1a`

### S112 — GM/T 0015-2012: Digital certificate format based on SM2 algorithm (Chinese scan)

Publisher: State Cryptography Administration of China; Standards Press of China  
Document date: 2012-11-22  
Language: Chinese · Format: pdf  
Provenance: Primary Chinese standard reproduced by the guanzhi/GM-Standards mirror; not a publisher-hosted or translated edition

Edition: GM/T 0015-2012 | Initial issue: 2012-11-22 | Effective: 2012-11-22 | Printing: 2013-01 | Extent: 61 PDF pages

Chinese national-language standard scan hosted by guanzhi/GM-Standards on GitHub, pinned to commit 402e57ed1c4002e3262978061b4f490b5e9ffc65. Cover identifies GM/T 0015-2012 and prints issue/effective dates 2012-11-22. Host filenames and mirror commit dates are not issue or approval dates. Final imprint identifies the first edition and first printing as January 2013, distinct from the 2012 standard issue date.

Original URL: <https://raw.githubusercontent.com/guanzhi/GM-Standards/402e57ed1c4002e3262978061b4f490b5e9ffc65/GMT%E5%AF%86%E7%A0%81%E8%A1%8C%E6%A0%87/GMT%200015-2012%20%E5%9F%BA%E4%BA%8ESM2%E5%AF%86%E7%A0%81%E7%AE%97%E6%B3%95%E7%9A%84%E6%95%B0%E5%AD%97%E8%AF%81%E4%B9%A6%E6%A0%BC%E5%BC%8F.pdf>

[Preserved file](../sources/originals/S112-gmt0015-mirror.pdf) · 35,429,684 bytes · 61 PDF pages

Retrieved UTC: 2026-10-20T15:38:39.639274+00:00  
SHA-256: `d5e574253005472654039118133ec921060c8cc500648fc7ee859e8c27fed8fa`

### S113 — GM/T 0017-2012: Smart token cryptography application interface data format specification (Chinese scan)

Publisher: State Cryptography Administration of China; Standards Press of China  
Document date: 2012-11-22  
Language: Chinese · Format: pdf  
Provenance: Primary Chinese standard reproduced by the guanzhi/GM-Standards mirror; not a publisher-hosted or translated edition

Edition: GM/T 0017-2012 | Initial issue: 2012-11-22 | Effective: 2012-11-22 | Extent: 155 PDF pages

Chinese national-language standard scan hosted by guanzhi/GM-Standards on GitHub, pinned to commit 402e57ed1c4002e3262978061b4f490b5e9ffc65. Cover identifies GM/T 0017-2012 and prints issue/effective dates 2012-11-22. Host filenames and mirror commit dates are not issue or approval dates.

Original URL: <https://raw.githubusercontent.com/guanzhi/GM-Standards/402e57ed1c4002e3262978061b4f490b5e9ffc65/GMT%E5%AF%86%E7%A0%81%E8%A1%8C%E6%A0%87/GMT%200017-2012%20%E6%99%BA%E8%83%BD%E5%AF%86%E7%A0%81%E9%92%A5%E5%8C%99%E5%AF%86%E7%A0%81%E5%BA%94%E7%94%A8%E6%8E%A5%E5%8F%A3%E6%95%B0%E6%8D%AE%E6%A0%BC%E5%BC%8F%E8%A7%84%E8%8C%83.PDF>

[Preserved file](../sources/originals/S113-gmt0017-mirror.pdf) · 4,335,518 bytes · 155 PDF pages

Retrieved UTC: 2026-10-20T15:38:39.644895+00:00  
SHA-256: `53ec505191d603ebf95c60978404d25c60cd53b9672ac45096606897c65a3dce`

### S114 — GM/T 0024-2014: SSL VPN specification (Chinese scan)

Publisher: State Cryptography Administration of China; Standards Press of China  
Document date: 2014-02-13  
Language: Chinese · Format: pdf  
Provenance: Primary Chinese standard reproduced by the guanzhi/GM-Standards mirror; not a publisher-hosted or translated edition

Edition: GM/T 0024-2014 | Initial issue: 2014-02-13 | Effective: 2014-02-13 | Extent: 36 PDF pages

Chinese national-language standard scan hosted by guanzhi/GM-Standards on GitHub, pinned to commit 402e57ed1c4002e3262978061b4f490b5e9ffc65. Cover identifies GM/T 0024-2014 and prints issue/effective dates 2014-02-13. Host filenames and mirror commit dates are not issue or approval dates.

Original URL: <https://raw.githubusercontent.com/guanzhi/GM-Standards/402e57ed1c4002e3262978061b4f490b5e9ffc65/GMT%E5%AF%86%E7%A0%81%E8%A1%8C%E6%A0%87/GMT%200024-2014%20SSL%20VPN%20%E6%8A%80%E6%9C%AF%E8%A7%84%E8%8C%83.PDF>

[Preserved file](../sources/originals/S114-gmt0024-mirror.pdf) · 4,302,806 bytes · 36 PDF pages

Retrieved UTC: 2026-10-20T15:38:40.552273+00:00  
SHA-256: `20787a423e00dcaa4935f78e628b35234cb5a588679ba4e3122d4ae0d59a51d2`

### S115 — RFC 5528: Camellia Counter Mode and Camellia Counter with CBC-MAC Mode Algorithms

Publisher: RFC Editor; named document authors  
Document date: 2009-04  
Language: English · Format: text  
Provenance: Original publisher

Edition: RFC 5528 | RFC category: Informational | RFC stream: IETF | RFC status at issue: INFORMATIONAL | Status in acquired index: INFORMATIONAL | Extent: 22 publisher-index pages; original RFC text

Category is transcribed from the preserved original header. Stream and publisher status fields are cross-checked against the separately preserved RFC index (S100), entry RFC5528. They establish RFC publication provenance, not national approval or implementation certification.

Original URL: <https://www.rfc-editor.org/rfc/rfc5528.txt>

[Preserved file](../sources/originals/S115-rfc5528.txt) · 56,134 bytes

Retrieved UTC: 2026-10-20T15:37:46.578342+00:00  
SHA-256: `3477959e97dcadfdd78abfd106f3e9bd94dd4a40bdec279b77d84e89e83760b9`

### S116 — RFC 5529: Modes of Operation for Camellia for Use with IPsec

Publisher: RFC Editor; named document authors  
Document date: 2009-04  
Language: English · Format: text  
Provenance: Original publisher

Edition: RFC 5529 | RFC category: Standards Track | RFC stream: IETF | RFC status at issue: PROPOSED STANDARD | Status in acquired index: PROPOSED STANDARD | Extent: 7 publisher-index pages; original RFC text

Category is transcribed from the preserved original header. Stream and publisher status fields are cross-checked against the separately preserved RFC index (S100), entry RFC5529. They establish RFC publication provenance, not national approval or implementation certification.

Original URL: <https://www.rfc-editor.org/rfc/rfc5529.txt>

[Preserved file](../sources/originals/S116-rfc5529.txt) · 13,030 bytes

Retrieved UTC: 2026-10-20T15:37:46.765850+00:00  
SHA-256: `6a8e197a19c385161a20f113f8c0d2b26984968e6f3a9e023dfd02c9545d66d7`

### S117 — RFC 6367: Addition of the Camellia Cipher Suites to Transport Layer Security (TLS)

Publisher: RFC Editor; named document authors  
Document date: 2011-09  
Language: English · Format: text  
Provenance: Original publisher

Edition: RFC 6367 | RFC category: Informational | RFC stream: IETF | RFC status at issue: INFORMATIONAL | Status in acquired index: INFORMATIONAL | Extent: 8 publisher-index pages; original RFC text

Category is transcribed from the preserved original header. Stream and publisher status fields are cross-checked against the separately preserved RFC index (S100), entry RFC6367. They establish RFC publication provenance, not national approval or implementation certification.

Original URL: <https://www.rfc-editor.org/rfc/rfc6367.txt>

[Preserved file](../sources/originals/S117-rfc6367.txt) · 17,613 bytes

Retrieved UTC: 2026-10-20T15:37:46.774000+00:00  
SHA-256: `7343444b83b9d7c264cf80a940665b94181011be741b80a260500d939c421ab2`

### S118 — RFC 2994: A Description of the MISTY1 Encryption Algorithm

Publisher: RFC Editor; named document authors  
Document date: 2000-11  
Language: English · Format: text  
Provenance: Original publisher

Edition: RFC 2994 | RFC category: Informational | RFC stream: Legacy (publisher index; original header predates stream labels) | RFC status at issue: INFORMATIONAL | Status in acquired index: INFORMATIONAL | Extent: 10 publisher-index pages; original RFC text

Category is transcribed from the preserved original header. Stream and publisher status fields are cross-checked against the separately preserved RFC index (S100), entry RFC2994. They establish RFC publication provenance, not national approval or implementation certification.

Original URL: <https://www.rfc-editor.org/rfc/rfc2994.txt>

[Preserved file](../sources/originals/S118-rfc2994.txt) · 17,803 bytes

Retrieved UTC: 2026-10-20T15:37:47.443597+00:00  
SHA-256: `a1ba5947ca793c55b2653f449fe19d0f972683a19c0bbb717a90ce6e98020756`

### S119 — RFC 7008: A Description of the KCipher-2 Encryption Algorithm

Publisher: RFC Editor; named document authors  
Document date: 2013-08  
Language: English · Format: text  
Provenance: Original publisher

Edition: RFC 7008 | RFC category: Informational | RFC stream: Independent Submission | RFC status at issue: INFORMATIONAL | Status in acquired index: INFORMATIONAL | Extent: 37 publisher-index pages; original RFC text

Category is transcribed from the preserved original header. Stream and publisher status fields are cross-checked against the separately preserved RFC index (S100), entry RFC7008. They establish RFC publication provenance, not national approval or implementation certification.

Original URL: <https://www.rfc-editor.org/rfc/rfc7008.txt>

[Preserved file](../sources/originals/S119-rfc7008.txt) · 71,051 bytes

Retrieved UTC: 2026-10-20T15:37:47.149022+00:00  
SHA-256: `5a5074fb4655296fa5fa0d274191a48f87e14ac66573eb21c79c3788870d6e23`

### S120 — ETSI TS 135 202 V17.0.0: KASUMI specification, Release 17

Publisher: ETSI / 3GPP  
Document date: 2022-04  
Language: English · Format: pdf  
Provenance: Original publisher

Edition: ETSI TS 135 202 V17.0.0 / 3GPP TS 35.202 Release 17 | Extent: 26 PDF pages

The April 2022 edition is the preserved standards wrapper, not a claim that the primitive was invented or first approved in 2022. Its annex includes an older dated sample implementation.

Original URL: <https://www.etsi.org/deliver/etsi_ts/135200_135299/135202/17.00.00_60/ts_135202v170000p.pdf>

[Preserved file](../sources/originals/S120-kasumi-17.pdf) · 147,275 bytes · 26 PDF pages

Retrieved UTC: 2026-10-20T15:38:41.558310+00:00  
SHA-256: `73f26476db04881d7bc2395ca623aa6d8e81ce38e163fd10a1da3593f263326d`

### S121 — RFC 5669: The SEED Cipher Algorithm and Its Use with the Secure Real-Time Transport Protocol (SRTP)

Publisher: RFC Editor; named document authors  
Document date: 2010-08  
Language: English · Format: text  
Provenance: Original publisher

Edition: RFC 5669 | RFC category: Standards Track | RFC stream: IETF | RFC status at issue: PROPOSED STANDARD | Status in acquired index: PROPOSED STANDARD | Extent: 13 publisher-index pages; original RFC text

Category is transcribed from the preserved original header. Stream and publisher status fields are cross-checked against the separately preserved RFC index (S100), entry RFC5669. They establish RFC publication provenance, not national approval or implementation certification.

Original URL: <https://www.rfc-editor.org/rfc/rfc5669.txt>

[Preserved file](../sources/originals/S121-rfc5669.txt) · 24,918 bytes

Retrieved UTC: 2026-10-20T15:37:47.216827+00:00  
SHA-256: `2fc14db340ecf3aed3b80c8c4b2a11c109967586f0b0b03d4e54ab63f6c48d89`

### S122 — RFC 4010: Use of the SEED Encryption Algorithm in Cryptographic Message Syntax (CMS)

Publisher: RFC Editor; named document authors  
Document date: 2005-02  
Language: English · Format: text  
Provenance: Original publisher

Edition: RFC 4010 | RFC category: Standards Track | RFC stream: IETF | RFC status at issue: PROPOSED STANDARD | Status in acquired index: PROPOSED STANDARD | Extent: 13 publisher-index pages; original RFC text

Category is transcribed from the preserved original header. Stream and publisher status fields are cross-checked against the separately preserved RFC index (S100), entry RFC4010. They establish RFC publication provenance, not national approval or implementation certification.

Original URL: <https://www.rfc-editor.org/rfc/rfc4010.txt>

[Preserved file](../sources/originals/S122-rfc4010.txt) · 22,403 bytes

Retrieved UTC: 2026-10-20T15:38:41.333764+00:00  
SHA-256: `13e00750f938bdbd21bb938010505288908e84610aa419079584d13ac3a66545`

### S123 — RFC 5639: Elliptic Curve Cryptography (ECC) Brainpool Standard Curves and Curve Generation

Publisher: RFC Editor; named document authors  
Document date: 2010-03  
Language: English · Format: text  
Provenance: Original publisher

Edition: RFC 5639 | RFC category: Informational | RFC stream: Independent Submission | RFC status at issue: INFORMATIONAL | Status in acquired index: INFORMATIONAL | Extent: 27 publisher-index pages; original RFC text

Category is transcribed from the preserved original header. Stream and publisher status fields are cross-checked against the separately preserved RFC index (S100), entry RFC5639. They establish RFC publication provenance, not national approval or implementation certification.

Original URL: <https://www.rfc-editor.org/rfc/rfc5639.txt>

[Preserved file](../sources/originals/S123-rfc5639.txt) · 50,566 bytes

Retrieved UTC: 2026-10-20T15:37:46.458842+00:00  
SHA-256: `d19949766009ac82b69e46b09f3a08d712908381300a340d3fa3b1478f4b215e`

### S124 — RFC 8734: Elliptic Curve Cryptography (ECC) Brainpool Curves for Transport Layer Security (TLS) Version 1.3

Publisher: RFC Editor; named document authors  
Document date: 2020-02  
Language: English · Format: text  
Provenance: Original publisher

Edition: RFC 8734 | RFC category: Informational | RFC stream: Independent Submission | RFC status at issue: INFORMATIONAL | Status in acquired index: INFORMATIONAL | Extent: 11 publisher-index pages; original RFC text

Category is transcribed from the preserved original header. Stream and publisher status fields are cross-checked against the separately preserved RFC index (S100), entry RFC8734. They establish RFC publication provenance, not national approval or implementation certification.

Original URL: <https://www.rfc-editor.org/rfc/rfc8734.txt>

[Preserved file](../sources/originals/S124-rfc8734.txt) · 18,297 bytes

Retrieved UTC: 2026-10-20T15:37:46.496541+00:00  
SHA-256: `47d4e076ec158107aceb2415a3f417eb30e034bcee99c91ab1f64656a5879075`

### S125 — BSI TR-03111: Elliptic Curve Cryptography, Version 2.10

Publisher: German Federal Office for Information Security (BSI)  
Document date: 2018-06-01  
Language: English · Format: pdf  
Provenance: Original publisher

Edition: 2.10 | Initial issue: 2007-02-14 | Revision: 2018-06-01 | Extent: 43 PDF pages

Cover and revision history identify version 2.10 dated 2018-06-01. The URL filename contains V-2-1, which must not be silently substituted for the printed version. History dates the first public version to 2007-02-14.

Original URL: <https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TR03111/BSI-TR-03111_V-2-1_pdf.pdf?__blob=publicationFile&v=1>

[Preserved file](../sources/originals/S125-bsi-tr03111.pdf) · 813,167 bytes · 43 PDF pages

Retrieved UTC: 2026-10-20T15:37:47.528572+00:00  
SHA-256: `51ee5d0fab150c42d8b446bd48dc7bb7be987278507a0bd96619b50eb127c440`

### S126 — RFC 5869: HMAC-based Extract-and-Expand Key Derivation Function (HKDF)

Publisher: RFC Editor; named document authors  
Document date: 2010-05  
Language: English · Format: text  
Provenance: Original publisher

Edition: RFC 5869 | RFC category: Informational | RFC stream: IETF | RFC status at issue: INFORMATIONAL | Status in acquired index: INFORMATIONAL | Extent: 14 publisher-index pages; original RFC text

Category is transcribed from the preserved original header. Stream and publisher status fields are cross-checked against the separately preserved RFC index (S100), entry RFC5869. They establish RFC publication provenance, not national approval or implementation certification.

Original URL: <https://www.rfc-editor.org/rfc/rfc5869.txt>

[Preserved file](../sources/originals/S126-rfc5869.txt) · 25,854 bytes

Retrieved UTC: 2026-10-20T15:37:47.425544+00:00  
SHA-256: `7a40eb3835b35fc947eb12a2ed614db079d43b26e50dbc537c31fba16397089c`

### S127 — RFC 8018: PKCS #5: Password-Based Cryptography Specification Version 2.1

Publisher: RFC Editor; named document authors  
Document date: 2017-01  
Language: English · Format: text  
Provenance: Original publisher

Edition: RFC 8018 | RFC category: Informational | RFC stream: IETF | RFC status at issue: INFORMATIONAL | Status in acquired index: INFORMATIONAL | Extent: 40 publisher-index pages; original RFC text

Category is transcribed from the preserved original header. Stream and publisher status fields are cross-checked against the separately preserved RFC index (S100), entry RFC8018. They establish RFC publication provenance, not national approval or implementation certification.

Original URL: <https://www.rfc-editor.org/rfc/rfc8018.txt>

[Preserved file](../sources/originals/S127-rfc8018.txt) · 80,887 bytes

Retrieved UTC: 2026-10-20T15:37:47.221891+00:00  
SHA-256: `cf96b02e68216f618ea33b20b49d476edba9d70f2333597ec516629d22971cda`

### S128 — ANSSI cryptographic mechanisms: current guide distribution page

Publisher: ANSSI / MesServicesCyber  
Document date: 2026-03-20  
Language: French · Format: html  
Provenance: Original government distribution page; raw HTML snapshot

Extent: Raw HTML snapshot; linked assets not bundled

Page says published 2026-03-20 and links a v3.00 rules guide together with a v1.0 selection guide. The latter PDF remains dated 2021-03-08. An older v2.04 PDF URL redirects here; it does not return the historical PDF.

Original URL: <https://messervices.cyber.gouv.fr/guides/mecanismes-cryptographiques>

[Preserved file](../sources/web/S128-anssi-current-index.html) · 33,212 bytes

Retrieved UTC: 2026-10-20T15:39:18.239432+00:00  
SHA-256: `0fb9d35a8a31eeeebc4d08069b1cddcd06b8c2dc1168f7afa8df5b1169e206ae`

### S129 — ANSSI-PG-083: Rules and recommendations for choosing and sizing cryptographic mechanisms

Publisher: ANSSI  
Document date: 2026-03-20  
Language: French · Format: pdf  
Provenance: Original publisher

Edition: 3.00 | Initial issue: 2004-11-19 | Revision: 2026-03-20 | Extent: 81 PDF pages

Cover and revision table identify 2026-03-20 / v3.00. The table records v2.04 on 2020-01-01 and a first applicable version on 2004-11-19. The 2026 edition explicitly adds quantum-threat treatment. These are guide milestones, not first approval dates for every algorithm.

Original URL: <https://messervices.cyber.gouv.fr/documents-guides/anssi-guide-mecanismes-crypto-3.00.pdf>

[Preserved file](../sources/originals/S129-anssi-mechanisms-300.pdf) · 1,365,473 bytes · 81 PDF pages

Retrieved UTC: 2026-10-20T15:39:51.588090+00:00  
SHA-256: `1baf13e8ae81bd476f09aed12885587850429a6925a182b6b8d5c76b31b288ec`

### S130 — ANSSI-PA-079: Guide to selecting cryptographic algorithms

Publisher: ANSSI  
Document date: 2021-03-08  
Language: French · Format: pdf  
Provenance: Original publisher

Edition: 1.0 | Initial issue: 2021-03-08 | Extent: 58 PDF pages

Cover prints 8/3/2021; the revision table calls this the initial v1.0 edition. It is linked from a page dated March 2026 but remains a 2021 document. Recommendations retain their original scope and date.

Original URL: <https://messervices.cyber.gouv.fr/documents-guides/anssi-guide-selection_crypto-1.0.pdf>

[Preserved file](../sources/originals/S130-anssi-selection-10.pdf) · 428,530 bytes · 58 PDF pages

Retrieved UTC: 2026-10-20T15:39:51.587281+00:00  
SHA-256: `5b48eb227d57be08c7d0365b39e3168be7580222f8c0cf69e044fb9265950281`

### S131 — Document 2: SNOW 3G Algorithm Specification

Publisher: ETSI/SAGE; distributed by GSMA  
Document date: 2006-09-06  
Language: English · Format: pdf  
Provenance: Original publisher

Edition: 1.1 | Initial issue: 2006-01-10 | Revision: 2006-09-06 | Extent: 37 PDF pages

Edition and date transcribed from this document’s cover. The 2019 hosting directory does not date the specification. Companion documents have different version/date histories and are not treated as a synchronized release.

Original URL: <https://www.gsma.com/solutions-and-impact/technologies/security/wp-content/uploads/2019/05/snow3gspec.pdf>

[Preserved file](../sources/originals/S131-snow3g.pdf) · 355,133 bytes · 37 PDF pages

Retrieved UTC: 2026-10-20T15:39:51.588712+00:00  
SHA-256: `a4dc79f2dcf3a1d91a0c5efbae317ffc50cbf90a9bb53da0edb52b4e86b989b5`

### S132 — Document 1: UEA2 and UIA2 Specification

Publisher: ETSI/SAGE; distributed by GSMA  
Document date: 2009-03-16  
Language: English · Format: pdf  
Provenance: Original publisher

Edition: 2.1 | Revision: 2009-03-16 | Extent: 27 PDF pages

Edition and date transcribed from this document’s cover. The 2019 hosting directory does not date the specification. Companion documents have different version/date histories and are not treated as a synchronized release.

Original URL: <https://www.gsma.com/solutions-and-impact/technologies/security/wp-content/uploads/2019/05/uea2uia2d1v21.pdf>

[Preserved file](../sources/originals/S132-uea2-uia2.pdf) · 102,689 bytes · 27 PDF pages

Retrieved UTC: 2026-10-20T15:39:52.526883+00:00  
SHA-256: `d2671f7821e8971e8bf4245ff50f28fa7a1ec71be29927f60ef2f436b8edf438`

### S133 — Document 3: UEA2/UIA2 Implementors’ Test Data

Publisher: ETSI/SAGE; distributed by GSMA  
Document date: 2012-10-25  
Language: English · Format: pdf  
Provenance: Original publisher

Edition: 1.1 | Revision: 2012-10-25 | Extent: 20 PDF pages

Edition and date transcribed from this document’s cover. The 2019 hosting directory does not date the specification. Companion documents have different version/date histories and are not treated as a synchronized release.

Original URL: <https://www.gsma.com/solutions-and-impact/technologies/security/wp-content/uploads/2019/05/Doc3-UEA2-UIA2-Spec-Implementors-Test-Data.pdf>

[Preserved file](../sources/originals/S133-snow-tests.pdf) · 335,256 bytes · 20 PDF pages

Retrieved UTC: 2026-10-20T15:39:53.089544+00:00  
SHA-256: `fdf3281aacb8098f7cee4461851910aeff84f8c6cbdaadca95ee9a5d63d1c677`

### S134 — Document 5: UEA2/UIA2 Design and Evaluation Report

Publisher: ETSI/SAGE; distributed by GSMA  
Document date: 2006-09-06  
Language: English · Format: pdf  
Provenance: Original publisher

Edition: 1.1 | Initial issue: 2006-02-06 | Revision: 2006-09-06 | Extent: 40 PDF pages

Edition and date transcribed from this document’s cover. The 2019 hosting directory does not date the specification. Companion documents have different version/date histories and are not treated as a synchronized release.

Original URL: <https://www.gsma.com/solutions-and-impact/technologies/security/wp-content/uploads/2019/05/uea2designevaluation.pdf>

[Preserved file](../sources/originals/S134-snow-evaluation.pdf) · 506,305 bytes · 40 PDF pages

Retrieved UTC: 2026-10-20T15:39:53.437096+00:00  
SHA-256: `0c5640830b9d2f9d63f26181cf13a52400516035846d36548878b8feee4e321a`

### S135 — GSMA security algorithms: specifications and distribution provenance

Publisher: GSMA  
Document date: not printed / not verified  
Language: English · Format: html  
Provenance: Original publisher

Extent: Raw HTML snapshot; linked assets not bundled

Live distribution index. Its UEA2/UIA2 section states distribution rights and links Documents 1–5; raw HTML is not a complete offline rendering of linked files.

Original URL: <https://www.gsma.com/solutions-and-impact/technologies/security/security-algorithms/>

[Preserved file](../sources/web/S135-gsma-algorithm-index.html) · 98,554 bytes

Retrieved UTC: 2026-10-20T15:39:18.241072+00:00  
SHA-256: `316da170e7fd880ae82c7dccbb7c4c42540a6c72db69a9c9ea685f845951dff6`

### S136 — NEMA operating instructions / Instruction de service de la machine à chiffrer

Publisher: Historical Swiss NEMA operating manual; issuing office not named on the scanned cover  
Document date: not printed / not verified  
Language: German / French · Format: pdf  
Provenance: Primary historical operating manual reproduced as a Crypto Museum scan

Declassification annotation: 1992-07-09 | Extent: 18 PDF pages of scanned booklet spreads, including covers and German/French instructions

Original booklet scan hosted by Crypto Museum, copy number 717. Cover is stamped declassified 1992-07-09. No original issue date has been verified; the declassification date is not its publication, design or first approval date.

Original URL: <https://www.cryptomuseum.com/crypto/nema/files/nema_manual.pdf>

[Preserved file](../sources/originals/S136-nema-manual.pdf) · 10,468,622 bytes · 18 PDF pages

Retrieved UTC: 2026-10-20T15:37:47.625724+00:00  
SHA-256: `303b7e2e90235d8add3ff4eab207bf4e13e8eb056f4624134aaad62dfbc8eb03`

### S137 — FRA’s history in brief: From Morse telegraphy to cyber defence

Publisher: Swedish National Defence Radio Establishment (FRA); Fredrik Wallin  
Document date: not printed / not verified  
Language: Swedish · Format: pdf  
Provenance: Original agency historical publication

Extent: 15 PDF pages containing booklet spreads and covers; printed history through page 26

Official retrospective history. No publication date is printed in the inspected cover or final page; the 2022 download-path timestamp and PDF metadata are not asserted as the original issue date.

Original URL: <https://fra.se/download/18.55af049f184e92956c43f20/1658314605605/FRAs-historia-i-korthet.pdf>

[Preserved file](../sources/originals/S137-fra-history.pdf) · 1,660,464 bytes · 15 PDF pages

Retrieved UTC: 2026-10-20T15:36:49.379785+00:00  
SHA-256: `26c6d5c18a28d3dccb8cf353a75a855b86bb49e31427e718902c0e30ecb459a4`

### S138 — How Arne Beurling may have broken the G-schreiber: Carl-Gösta Borelius account

Publisher: FRA; Carl-Gösta Borelius  
Document date: not printed / not verified  
Language: Swedish · Format: html  
Provenance: Participant’s archival retrospective account published by the original agency; raw HTML snapshot

Extent: Raw HTML snapshot; linked assets not bundled

FRA describes the account as written in the 1980s and published here from its archive; exact composition and web-publication dates are not established. Borelius participated in G-schreiber cryptanalysis from 1941. His account reconstructs how Beurling may have worked; it is not Beurling’s contemporaneous explanation.

Original URL: <https://www.fra.se/omfra/frashistoria/forceringenavgskrivaren.4.55af049f184e92956c42acb.html>

[Preserved file](../sources/web/S138-fra-g-schreiber.html) · 87,300 bytes

Retrieved UTC: 2026-10-20T15:36:48.879831+00:00  
SHA-256: `5ca0e426a721b80caef827494be1afb4529e874750ae32559a79ebd4f726b202`

### S139 — 3GPP TR 55.919 V6.1.0: A5/3 and GEA3 design and evaluation report (development copy)

Publisher: 3GPP / ETSI SAGE; distributed by GSMA  
Document date: 2002-12  
Language: English · Format: pdf  
Provenance: Original standards-project technical report, distributed by GSMA; cover status warning retained

Edition: 3GPP TR 55.919 V6.1.0 / Release 6 | Revision: 2002-12 | Extent: 26 PDF pages

Cover identifies Release 6 / V6.1.0 (2002-12) and explicitly says the document has not been subject to approval by the Organizational Partners and shall not be implemented. Preserved as a historical design/evaluation account, not an approval or implementation instruction. The 2019 hosting directory is not the report date.

Original URL: <https://www.gsma.com/solutions-and-impact/technologies/security/wp-content/uploads/2019/05/designevaluationreport.pdf>

[Preserved file](../sources/originals/S139-kasumi-evaluation.pdf) · 165,984 bytes · 26 PDF pages

Retrieved UTC: 2026-10-20T15:52:09.510652+00:00  
SHA-256: `7372e93973ced4088d904bec185bb78567e7529f56aaac5f60c69343f9899f97`
