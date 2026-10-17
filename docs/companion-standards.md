# Companion standards: from primitives to implementations

Research snapshot: 2026-10-17

This collection links the archive’s algorithm profiles to the surrounding specifications: modes, parameters, key formats, protocol profiles, selection lists and validation records. It preserves particular editions and their dates rather than claiming to hold every standard or the latest version of every document.

An algorithm release, a national-standard issue, an effective date, an RFC publication and a product certificate describe different events. A protocol profile can expose exact mathematical and wire-format choices while leaving deployment and implementation approval unresolved.

The original files remain unchanged. Documented statements have source locators; deductions identify their premises and assumptions. Acquisition failures and incomplete copies are listed alongside successful preservation.

This guide maps **7 families**, **36 claims** and **27 dated milestones** to 52 source records. 49 copies are preserved, including 40 newly added documents and snapshots. Three KISA pages remain acquisition gaps.

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
| [Common modes, formats and Suite A interfaces](#interfaces) | [S001](../sources/README.md#s001), [S003](../sources/README.md#s003), [S004](../sources/README.md#s004), [S064](../sources/README.md#s064), [S065](../sources/README.md#s065), [S066](../sources/README.md#s066), [S067](../sources/README.md#s067), [S068](../sources/README.md#s068), [S069](../sources/README.md#s069) | Read the primitive or mechanism interface, then the mode definition, then the protocol that uses it. The PKCS #11 Base and Historical Mechanisms copies deliberately share the v3.0 publication date. |
| [Russia: GOST parameters, modes and protocol bindings](#gost) | [S050](../sources/README.md#s050), [S057](../sources/README.md#s057), [S058](../sources/README.md#s058), [S059](../sources/README.md#s059), [S060](../sources/README.md#s060), [S061](../sources/README.md#s061), [S062](../sources/README.md#s062), [S063](../sources/README.md#s063), [S064](../sources/README.md#s064), [S065](../sources/README.md#s065) | Start with the existing primitive profiles. Use RFC 4357 for older GOST companion choices; RFC 7836 for newer auxiliary algorithms and curves; RFC 9058 for MGM; then choose the certificate, TLS or IPsec binding. |
| [China: original releases, parameters and successive standards](#shangmi) | [S026](../sources/README.md#s026), [S034](../sources/README.md#s034), [S035](../sources/README.md#s035), [S036](../sources/README.md#s036), [S070](../sources/README.md#s070), [S071](../sources/README.md#s071), [S072](../sources/README.md#s072), [S073](../sources/README.md#s073), [S074](../sources/README.md#s074), [S096](../sources/README.md#s096), [S097](../sources/README.md#s097), [S098](../sources/README.md#s098) | Pair the dated 2010 announcements with their official attachments. Read the one-page SM2 curve parameters separately from the general algorithm. Follow the 2012 industry standards, later GB/T records, revised application standards, and the TLS 1.3 profile. |
| [China and 3GPP: ZUC, EEA3 and EIA3](#zuc) | [S037](../sources/README.md#s037), [S075](../sources/README.md#s075), [S076](../sources/README.md#s076), [S092](../sources/README.md#s092), [S093](../sources/README.md#s093) | Read ZUC Document 2 for the keystream generator, Document 1 for the EEA3/EIA3 packet algorithms, Document 3 for implementer test data and Document 4 for design/evaluation history. The Release 19 ETSI wrapper records the later standards context. |
| [Japan: CRYPTREC selections and Camellia protocol profiles](#japan) | [S077](../sources/README.md#s077), [S078](../sources/README.md#s078), [S079](../sources/README.md#s079), [S080](../sources/README.md#s080), [S086](../sources/README.md#s086), [S087](../sources/README.md#s087), [S094](../sources/README.md#s094) | Compare the historical 2003 list (with its 2005 correction), the original 2013 list, and the preserved March 2026 revision. Use the strength-requirements document to interpret key-length and lifetime choices. Camellia TLS and IPsec bindings are separate protocol records. |
| [Republic of Korea: SEED and ARIA protocol profiles](#korea) | [S084](../sources/README.md#s084), [S085](../sources/README.md#s085), [S088](../sources/README.md#s088), [S089](../sources/README.md#s089), [S090](../sources/README.md#s090), [S091](../sources/README.md#s091), [S099](../sources/README.md#s099) | Use the existing SEED and ARIA primitive specifications, then the TLS and IPsec/SRTP bindings as relevant. The KCMVP programme pages are acquisition leads only until their original bytes can be preserved. |
| [Germany: general recommendations and protocol guidance](#germany) | [S081](../sources/README.md#s081), [S082](../sources/README.md#s082), [S083](../sources/README.md#s083), [S095](../sources/README.md#s095) | TR-02102-1 gives general cryptographic mechanism and key-length recommendations; Parts 2, 3 and 4 specialize guidance for TLS, IPsec/IKEv2 and SSH. Read these separately from the existing historical product and approval records. |

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

### Inference

- **STD-COM-I1 · conditional** — If a product uses MEDLEY with GCM exactly as defined in SP 800-38D, the block cipher supplied to that mode has 128-bit blocks. This deduction supplies neither its key length nor its round construction. Basis: MEDLEY-F1, STD-COM-F1.
  Assumption: The manufacturer’s GCM label refers to the standard mode without a proprietary change in its block interface.

<a id="gost"></a>

## Russia: GOST parameters, modes and protocol bindings

Existing profiles: [GOST 28147-89](../profiles/international/gost-28147.md), [Magma](../profiles/international/magma.md), [Kuznyechik](../profiles/international/kuznyechik.md), [Streebog](../profiles/international/streebog.md), [GOST signatures](../profiles/international/gost-signatures.md).

Start with the existing primitive profiles. Use RFC 4357 for older GOST companion choices; RFC 7836 for newer auxiliary algorithms and curves; RFC 9058 for MGM; then choose the certificate, TLS or IPsec binding.

**Scope limit:** The preserved GOST binding RFCs are Informational Independent Submissions. RFC 8645 is an IRTF Informational document. These distinct streams do not imply IETF standards-track endorsement or establish the original Russian approval dates.

### Documented statements

- **STD-GOST-F1** — RFC 4357 provides additional modes, key meshing, wrapping, parameter sets and identifiers for the older GOST algorithm family. RFC 7836 adds HMAC, VKO key agreement, KDF and wrapping constructions and elliptic-curve parameters for the 2012 family. ([S050](../sources/README.md#s050), Abstract; Sections 2–8; [S057](../sources/README.md#s057), Sections 4 and 5; Appendix A)
- **STD-GOST-F2** — MGM is an authenticated-encryption mode defined for both 64-bit and 128-bit block ciphers. RFC 9058 supplies test vectors for Kuznyechik and Magma. ([S059](../sources/README.md#s059), Abstract; Section 4; Appendices A.1 and A.2)
- **STD-GOST-F3** — RFC 9227 binds Magma and Kuznyechik in MGM, with external rekeying, to ESP and IKEv2. RFC 9189 profiles GOST for TLS 1.2; RFC 9367 separately defines cipher suites, signature schemes and key exchange for TLS 1.3. ([S060](../sources/README.md#s060), Abstract; Section 1; [S062](../sources/README.md#s062), Abstract; [S063](../sources/README.md#s063), Abstract; Sections 4–6)
- **STD-GOST-F4** — RFC 9215 specifies GOST signature/hash identifiers, parameters and encodings for the Internet X.509 PKI, including public-key encoding and signature representation. ([S061](../sources/README.md#s061), Abstract; Sections 2–4)
- **STD-GOST-F5** — RFCs 7836, 9058, 9189, 9215, 9227 and 9367 are Informational Independent Submissions. RFC 8645 is Informational in the IRTF stream and describes symmetric rekeying mechanisms. ([S057](../sources/README.md#s057), Header; Status of This Memo; [S058](../sources/README.md#s058), Header; Abstract; Status of This Memo; [S059](../sources/README.md#s059), Header; [S060](../sources/README.md#s060), Header; [S061](../sources/README.md#s061), Header; [S062](../sources/README.md#s062), Header; [S063](../sources/README.md#s063), Header)

### Inference

- **STD-GOST-I1 · conditional** — An implementation described only as supporting GOST is underspecified: interoperation also requires agreement on the primitive generation, curve or parameter set, mode, rekeying rules, encoding and protocol profile. Basis: STD-GOST-F1, STD-GOST-F2, STD-GOST-F3, STD-GOST-F4.
  Assumption: The parties exchange keys, signatures or protected messages using the cited protocol families.

<a id="shangmi"></a>

## China: original releases, parameters and successive standards

Existing profiles: [SM2](../profiles/international/sm2.md), [SM3](../profiles/international/sm3.md), [SM4](../profiles/international/sm4.md).

Pair the dated 2010 announcements with their official attachments. Read the one-page SM2 curve parameters separately from the general algorithm. Follow the 2012 industry standards, later GB/T records, revised application standards, and the TLS 1.3 profile.

**Scope limit:** The 2010 release texts, later industry/national standards and hosted English translations are different editions. The archive has official revision announcements, but not complete copies of every announced 2023 standard. S074 is an incomplete booklet scan.

### Documented statements

- **STD-SM-F1** — The Chinese authority’s announcements No.21 and No.22 are dated 2010-12-17 and release SM2 and SM3 respectively. Their attached official algorithm PDFs carry December 2010 covers. ([S070](../sources/README.md#s070), Release date and announcement text; attachment links; [S071](../sources/README.md#s071), Release date and announcement text; attachment link; [S096](../sources/README.md#s096), Covers at PDF pages 1, 47, 61 and 80; [S098](../sources/README.md#s098), Cover)
- **STD-SM-F2** — The 93-page SM2 release combines Parts 1–4: general elliptic-curve rules, signatures, key exchange and public-key encryption. A separate one-page official attachment recommends a 256-bit prime-field curve and gives p, a, b, n, Gx and Gy. ([S096](../sources/README.md#s096), Part covers at PDF pages 1, 47, 61 and 80; [S097](../sources/README.md#s097), Entire one-page parameter sheet)
- **STD-SM-F3** — The recommended SM2 curve has p = FFFFFFFE FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF 00000000 FFFFFFFF FFFFFFFF and a = p − 3. Its equation is y² = x³ + ax + b over that prime field. This parameter choice is more specific than the general label elliptic-curve cryptography. ([S097](../sources/README.md#s097), Curve equation and parameter lines p and a)
- **STD-SM-F4** — The original SM3 specification uses 512-bit message blocks, 32-bit words, 64 compression rounds, modular addition, XOR, rotations and Boolean functions, and outputs 256 bits. ([S098](../sources/README.md#s098), Sections 2–5, especially 4.3–4.4 and 5.2–5.4)
- **STD-SM-F5** — The 2012-11-22 announcement lists GM/T 0009-2012 for SM2 applications, GM/T 0010-2012 for signed/enveloped message syntax, GM/T 0014-2012 for certificate-authentication protocols and GM/T 0015-2012 for certificate format. ([S072](../sources/README.md#s072), Announcement No.24; numbered standards list)
- **STD-SM-F6** — Announcement No.45, posted 2023-12-23, lists 2023 revisions of GM/T 0009, 0010, 0014 and 0015 among other standards and states an effective date of 2024-06-01. The web posting date is recorded separately from each standard’s issue date. ([S073](../sources/README.md#s073), Posting date; announcement; attached standards list)
- **STD-SM-F7** — The official GB/T records for SM2 Part 1 and SM4 record issue on 2016-08-29 and implementation on 2017-03-01. These are later national-standard milestones, separate from the 2010 SM2 release and 2012 industry-standard announcements. ([S035](../sources/README.md#s035), Issue and implementation metadata; [S036](../sources/README.md#s036), Issue and implementation metadata; [S070](../sources/README.md#s070), Release date; [S034](../sources/README.md#s034), Announcement No.23 and standards list)
- **STD-SM-F8** — RFC 8998 profiles SM2, SM3 and SM4 for TLS 1.3, including SM4-GCM and SM4-CCM cipher suites. It is an Informational Independent Submission, while the underlying TLS 1.3 specification RFC 8446 is Standards Track. ([S026](../sources/README.md#s026), Header; Sections 2 and 3; [S065](../sources/README.md#s065), Header)

### Inference

- **STD-SM-I1 · conditional** — The curve sheet and SM3 text allow concrete descriptions of arithmetic, parameters and hashing without inferring those choices from a codeword. The published record does not, by itself, identify the original classified design date or every government use. Basis: STD-SM-F1, STD-SM-F2, STD-SM-F3, STD-SM-F4.
  Assumption: The question concerns the preserved public specifications and their dated releases, rather than an undocumented earlier variant.

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

## Japan: CRYPTREC selections and Camellia protocol profiles

Existing profiles: [Camellia](../profiles/international/camellia.md), [CLEFIA](../profiles/international/clefia.md).

Compare the historical 2003 list (with its 2005 correction), the original 2013 list, and the preserved March 2026 revision. Use the strength-requirements document to interpret key-length and lifetime choices. Camellia TLS and IPsec bindings are separate protocol records.

**Scope limit:** CRYPTREC list membership and category are dated policy evidence. They do not establish first invention, implementation certification or universal government approval.

### Documented statements

- **STD-JP-F1** — The preserved legacy CRYPTREC list is dated 2003-02-20 and includes a 2005-10-12 correction appendix. The archive also holds the 2013-03-01 list and the list revised 2026-03-30, whose family cover date is 2023-03-30. ([S094](../sources/README.md#s094), Cover and correction appendix; [S079](../sources/README.md#s079), Cover; [S078](../sources/README.md#s078), Cover)
- **STD-JP-F2** — The March 2026 list places Camellia among e-Government Recommended Ciphers and CLEFIA among Candidate Recommended Ciphers. A separate Monitored Ciphers category also exists. ([S078](../sources/README.md#s078), e-Government Recommended, Candidate Recommended and Monitored tables; PDF pages 1, 4 and 5)
- **STD-JP-F3** — The strength-requirements PDF’s revision table records first publication on 2022-07-01 and corrections on 2023-03-30. Its cover still states March 2022; the archive retains that internal date discrepancy. ([S080](../sources/README.md#s080), Cover; revision table in introductory pages)
- **STD-JP-F4** — RFC 5932 specifies Camellia cipher suites for TLS (June 2010), and RFC 4312 specifies Camellia for IPsec (December 2005). Both were published with the Standards Track category. ([S086](../sources/README.md#s086), Header; Abstract; [S087](../sources/README.md#s087), Header; Abstract)

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

### Inference

- **STD-KR-I1 · conditional** — The protocol records establish specified interoperability choices, but they do not by themselves show that a named product passed Korean module validation. Such a claim needs a product-specific validation record and its scope. Basis: STD-KR-F1, STD-KR-F2.
  Assumption: The proposed claim concerns implementation validation rather than publication of a protocol profile.

<a id="germany"></a>

## Germany: general recommendations and protocol guidance

Existing profiles: [CHIASMUS](../profiles/international/chiasmus.md), [LIBELLE / SINA](../profiles/international/libelle.md).

TR-02102-1 gives general cryptographic mechanism and key-length recommendations; Parts 2, 3 and 4 specialize guidance for TLS, IPsec/IKEv2 and SSH. Read these separately from the existing historical product and approval records.

**Scope limit:** General BSI technical guidance is not a public specification of LIBELLE or proof that a particular SINA product is approved for a classification level. It also does not establish CHIASMUS’s internal construction.

### Documented statements

- **STD-DE-F1** — The archived TR-02102-1 is version 2026-01, as of 2026-01-23. It provides general cryptographic mechanism and key-length recommendations. ([S081](../sources/README.md#s081), Cover; Section 1)
- **STD-DE-F2** — TR-02102 Parts 2, 3 and 4 address TLS, IPsec/IKEv2 and SSH respectively. Each preserved edition’s history dates version 2026-01 to 2026-01-27. ([S082](../sources/README.md#s082), Cover; Document history; Section 1; [S083](../sources/README.md#s083), Cover; Document history; Section 1; [S095](../sources/README.md#s095), Cover; Document history; Section 1)

### Inference

- **STD-DE-I1 · conditional** — The TR series supplies a public policy and protocol context for German deployments; identifying the mathematics or approval scope of an opaque product still requires a record that names that product and its algorithm or certification boundary. Basis: STD-DE-F1, STD-DE-F2.
  Assumption: No additional product-specific approval or algorithm specification is supplied by the generic guidance citation.

## Publication and effective dates

These events distinguish releases, revisions, list selections and publication categories. None is automatically an invention date or first classified approval.

| Date | Subject | Event type | Interpretation | Evidence |
|---|---|---|---|---|
| 2003-02-20 | CRYPTREC legacy list | list issue | Original list date; the preserved R1 copy also has a 2005 correction. | [S094](../sources/README.md#s094), Cover; correction appendix |
| 2005-08 | SEED / TLS | RFC publication | RFC 4162 Standards Track profile; not an invention date. | [S088](../sources/README.md#s088), Header |
| 2005-10-12 | CRYPTREC legacy list | correction | Specification-reference correction; not a new cipher design. | [S094](../sources/README.md#s094), Correction appendix |
| 2005-12 | Camellia / IPsec | RFC publication | RFC 4312 Standards Track profile. | [S087](../sources/README.md#s087), Header |
| 2010-06-18 | EEA3/EIA3 | specification publication | Document 1 history records v1.0 publication. | [S076](../sources/README.md#s076), Document History, PDF page 2 |
| 2010-12-17 | SM2 and SM3 | public release announcements | Official releases; attached PDFs have December 2010 covers. | [S070](../sources/README.md#s070), Announcement; compare S071 |
| 2011-01-04 | ZUC/EEA3/EIA3 | algorithm revision and test edition | EIA3 modification and v1.1 implementer-test edition; see design report for ZUC change. | [S076](../sources/README.md#s076), Document History; compare S092 and S093 |
| 2011-09-09 | ZUC design evaluation | report edition | Version 2.0 final deliverable. | [S093](../sources/README.md#s093), Cover; Document History |
| 2012-03-21 | Chinese industry standards | standards announcement | No.23 lists six standards including SM3 and SM4 industry standards. | [S034](../sources/README.md#s034), Announcement; standards list |
| 2012-11-22 | SM2 application ecosystem | standards announcement | No.24 lists applications, message syntax, certificate protocols and formats. | [S072](../sources/README.md#s072), Announcement; standards list |
| 2013-03-01 | CRYPTREC list | list issue | Original 2013 list retained as a historical edition. | [S079](../sources/README.md#s079), Cover |
| 2016-08-29 | SM2 Part 1 and SM4 | national-standard issue | GB/T issue date; later implementation date is 2017-03-01. | [S036](../sources/README.md#s036), Official metadata; compare S035 |
| 2017-03-01 | SM2 Part 1 and SM4 | national-standard implementation | Implementation date distinct from public release and issue. | [S036](../sources/README.md#s036), Official metadata; compare S035 |
| 2017-10 | ARIA / SRTP | RFC publication | RFC 8269 IETF Informational profile. | [S091](../sources/README.md#s091), Header |
| 2019-01-24 | EEA3/EIA3 | specification revision | Document 1 v1.8 increases maximum integrity-message length. | [S076](../sources/README.md#s076), Cover; Document History |
| 2020-06-15 | PKCS #11 v3.0 | OASIS standard edition | Matched Base and Historical Mechanisms editions. | [S066](../sources/README.md#s066), Cover; compare S001 |
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
| 2026-03-30 | CRYPTREC list | list revision | LS-0001-2022R2, with distinct recommended, candidate and monitored lists. | [S078](../sources/README.md#s078), Cover; list tables |

## Preservation and coverage limits

### Incomplete application-standard scan

S074 is preserved exactly as acquired: three PDF pages containing imposed booklet images of covers, contents, foreword and printed body pages 6–7. Earlier body pages are absent. It must not be cited as a complete GM/T 0009-2012 text. ([S074](../sources/README.md#s074))

### Korean validation acquisition gaps

S084, S085 and S099 returned HTTP 503. The catalogue retains the attempted URLs and retrieval errors, but no original copy is claimed. Programme names and acquisition leads are not substitutes for a preserved current eligibility list or product certificate. ([S084](../sources/README.md#s084), [S085](../sources/README.md#s085), [S099](../sources/README.md#s099))

### Revised standards announced but not fully acquired

S073 preserves the official announcement and list of 2023 industry-standard revisions. The archive does not claim to contain the full text of every listed revision. Historical 2012 material cannot silently substitute for a 2023 edition. ([S072](../sources/README.md#s072), [S073](../sources/README.md#s073), [S074](../sources/README.md#s074))

### Translations and mutable publisher URLs

The earlier Alipay-hosted English SM2/SM3/SM4 files remain separately labeled translations with edition uncertainties. The newly acquired official Chinese release files supply independent 2010 evidence. BSI and CRYPTREC URLs may later change their contents; SHA-256 and acquisition times identify the copies used here. ([S070](../sources/README.md#s070), [S071](../sources/README.md#s071), [S078](../sources/README.md#s078), [S081](../sources/README.md#s081), [S096](../sources/README.md#s096), [S097](../sources/README.md#s097), [S098](../sources/README.md#s098))

### Status and coverage limits

RFC categories and streams describe publication status at issue. This guide does not perform a complete present-day obsolescence, errata or approval audit. Full ISO/IEC standards and every national standard cited by the profiles are not all preserved. Historical rotor-machine records remain in their existing profiles; modern companion standards are not retroactively applied to Enigma, Lorenz or Fialka.

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
Attempt UTC: 2026-10-17T19:11:54.380270+00:00

### S085 — KCMVP: cryptographic module testing and validation procedures

Publisher: Korea Internet and Security Agency (KISA)  
Document date: not printed / not verified  
Language: Korean · Format: html  
Provenance: Original publisher

Original URL: <https://seed.kisa.or.kr/kisa/kcmvp/reference.do>

**Not preserved:** failed; HTTPError: HTTP Error 503: Service Unavailable  
Attempt UTC: 2026-10-17T19:11:55.326633+00:00

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
Attempt UTC: 2026-10-17T19:14:35.057635+00:00
