# Suite A: a public-source technical and historical record

Research snapshot: 2026-10-17

This first collection translates codeword names into technical roles and bounded inferences. It preserves a distinction between what a source states, what follows under stated assumptions, and what remains unknown. It is a research record rather than an official inventory or current deployment guide.

Suite A names a family of classified cryptographic algorithms. The historical NIST glossary describes its purpose as protecting certain restricted, mission-critical information (S019, printed p.190; PDF p.195). Individual names cover several different cryptographic functions. Product support lists can also contain published algorithms such as AES and equipment compatibility entries.

The evidence spans tactical secure voice, block-cipher interfaces, key establishment, key protection and software distribution. A name in a catalogue may designate an algorithm, a mode, a protocol or an equipment personality.

## From names to primitives

| Function | Examples in this collection | What the evidence exposes |
|---|---|---|
| Symmetric traffic or storage encryption | BATON, JUNIPER, MEDLEY | Block-oriented interfaces, key encodings, mode names and deployment roles; the round functions remain unspecified. |
| Key establishment | FIREFLY, SPONDULIX-S | A public-key description or a key-agreement role; exact mathematical groups and authentication details remain open. |
| Key protection | ACCORDION | Versioned key-wrapping roles; the protected-object format and internal construction remain open. |
| Software confidentiality | JOSEKI, WATARI | Tools and requirements for encrypted software loading; the underlying primitive remains open. |
| Software authenticity | KM-TG schemes, SILVER LINING | Signing and validation roles; the mathematical signature construction remains open. |
| Legacy secure voice | SAVILLE | Program history and an implementation throughput measurement; detailed internal structure needs separate evidence. |

The strongest deductions concern interfaces and roles. An advertised standard mode can constrain a primitive's block size, while a product's support list alone rarely establishes its internal design or cryptanalytic strength.

## How to read the record

Documented statements are source-reported facts, with locators. Inferences identify their premise claim IDs and any conditions. Dates distinguish development, specifications, public acknowledgment, requirements and implementation certification. A later public catalogue does not establish the public availability of the older records it lists.

See [the research method](methodology.md), [the timeline](timeline.md), the [additional-name index](name-index.md), and the [source catalogue](../sources/README.md). Source documents retain their original notices and have not been modified.

## MEDLEY

A symmetric encryption primitive exposed through familiar block-cipher modes.

### Documented statements

- **MEDLEY-F1** — Viasat advertises MEDLEY-256 with GCM, CTR, OFB and CFB. ([S005](../sources/README.md#s005), Multiple-mission capable > KG-42 ECM)
- **MEDLEY-F2** — Standard GCM uses a 128-bit block cipher and does not use its inverse function. ([S003](../sources/README.md#s003), Section 5.1)
- **MEDLEY-F3** — The NGLD-M requirements list MEDLEY for data-at-rest and non-security software confidentiality. ([S010](../sources/README.md#s010), Table 9, printed p.42; PDF p.48)

### Technical inferences

- **MEDLEY-I1 · conditional** — The advertised GCM profile implies a keyed 128-bit block permutation interface. Basis: MEDLEY-F1, MEDLEY-F2.
  Assumption: GCM denotes the standard NIST mode.
- **MEDLEY-I2 · conditional** — The advertised modes can process message encryption and decryption using only the forward block-cipher function. Basis: MEDLEY-F1, MEDLEY-F2.
  Assumption: The modes follow their standard definitions; see S004 sections 6.3-6.5.
- **MEDLEY-I3 · moderate** — The -256 designation suggests a 256-bit key variant, but does not by itself establish entropy or attack cost. Basis: MEDLEY-F1.

### Unresolved details

- Round function, key schedule and relationship to AES are not established by these records.
- The original 2001 mode set need not equal the later advertised mode set.

## BATON

A block-oriented cipher with structured key representation and token-controlled initialization.

### Documented statements

- **BATON-F1** — PKCS #11 encodes a BATON key value in 40 bytes and identifies 160 bits as checksum material. ([S001](../sources/README.md#s001), Section 2.9.2)
- **BATON-F2** — Named mechanisms include ECB128, ECB96, CBC128, COUNTER, SHUFFLE and WRAP; encryption-mode IV parameters are 24 bytes and token-selected. ([S001](../sources/README.md#s001), Sections 2.9.4-2.9.9)
- **BATON-F3** — NSA described BATON as supporting higher throughput than SKIPJACK with then-current microelectronics. ([S015](../sources/README.md#s015), Written question 6)

### Technical inferences

- **BATON-I1 · conditional** — If the checksum bits are determined by the remaining bits, this encoding contains at most 160 independent key bits: 320 minus 160. Basis: BATON-F1.
  Assumption: The checksum is deterministic from the remaining encoded key material.
- **BATON-I2 · strong** — The interface places encryption initialization policy inside the device. Basis: BATON-F2.

### Unresolved details

- The entropy bound is not a demonstrated cryptanalytic attack cost.
- The 192-bit IV parameter does not establish a 192-bit block size or internal state size.

## JUNIPER

A historical block-cipher interface closely resembling BATON at the API boundary.

### Documented statements

- **JUNIPER-F1** — JUNIPER has a 40-byte key representation containing 160 checksum bits, with ECB128, CBC128, counter, shuffle and wrapping mechanisms. ([S001](../sources/README.md#s001), Section 2.10)
- **JUNIPER-F2** — A public JUNIPER mechanism description appears in the December 1999 PKCS #11 standard. ([S002](../sources/README.md#s002), Section 12.23)

### Technical inferences

- **JUNIPER-I1 · moderate** — Shared key-format and mechanism conventions support reuse of integration infrastructure. Basis: JUNIPER-F1.

### Unresolved details

- A common API does not establish a common round function, key schedule or design ancestry.

## ACCORDION

A versioned key-protection mechanism in the key-management path.

### Documented statements

- **ACCORDION-F1** — ACCORDION 1.3 is assigned transfer-key protection and acceptable internal key wrapping. ([S010](../sources/README.md#s010), Table 9, printed p.42)
- **ACCORDION-F2** — ACCORDION 3.0 is an internal wrapping option and appears as a future KMI black-key wrapping option in the 2019 table. ([S010](../sources/README.md#s010), Table 9, printed p.42)
- **ACCORDION-F3** — A 2002 reference is titled NSA MEDLEY Implementation Standard: An ACCORDION MEDLEY. ([S010](../sources/README.md#s010), Bibliography, printed p.4; PDF p.10)

### Technical inferences

- **ACCORDION-I1 · strong** — A useful abstract interface is a wrapping key plus key material producing a protected key object. Basis: ACCORDION-F1, ACCORDION-F2.
- **ACCORDION-I2 · moderate** — The MEDLEY-related title is evidence of a documented relationship, whose construction remains unspecified. Basis: ACCORDION-F3.

### Unresolved details

- The cited roles do not expose a complete primitive or wrapping encoding.
- A future requirement is not evidence that a feature shipped.

## JOSEKI

Confidentiality for loadable algorithm software in a protected execution environment.

### Documented statements

- **JOSEKI-F1** — AIM tooling includes a JOSEKI encryptor for preparing program code and a JOSEKI decryption service. ([S006](../sources/README.md#s006), p.2, software environment and SOS services)
- **JOSEKI-F2** — AIM requires properly digitally signed software. ([S006](../sources/README.md#s006), p.2, Signed Software)
- **JOSEKI-F3** — Harris lists JOSEKI Decrypt among Sierra II capabilities. ([S007](../sources/README.md#s007), p.2, Type 1 algorithms)

### Technical inferences

- **JOSEKI-I1 · strong** — The documented tools support protected software preparation, distribution and device-side loading. Basis: JOSEKI-F1, JOSEKI-F2.
- **JOSEKI-I2 · strong** — A decrypt-only product entry describes its role as a recipient; it does not identify the cipher as asymmetric. Basis: JOSEKI-F1, JOSEKI-F3.

### Unresolved details

- Package format, key schedule and the ordering of decryption and signature checks are not specified here.

## WATARI

A confidentiality mechanism for security-software delivery.

### Documented statements

- **WATARI-F1** — NGLD-M assigns WATARI to security-software confidentiality and includes it among non-security software options. ([S010](../sources/README.md#s010), Table 9, printed p.42)

### Technical inferences

- **WATARI-I1 · strong** — WATARI protects the contents of software packages in this deployment model. Basis: WATARI-F1.

### Unresolved details

- A related purpose does not establish that WATARI derives from JOSEKI.
- Its internal mathematical construction is not established by the role assignment.

## FIREFLY / Enhanced FIREFLY

Endpoint key establishment rather than the bulk data-processing stage.

### Documented statements

- **FIREFLY-F1** — The KIV-19M brochure describes establishing a unique encryption key over full-duplex channels without an online third party. ([S009](../sources/README.md#s009), p.2, Operational Modes)
- **FIREFLY-F2** — Diffie discussed FIREFLY in 1988 and considered an exponentiation-based construction plausible from contemporary descriptions and testimony. ([S013](../sources/README.md#s013), p.571, STU-III/FIREFLY discussion)
- **FIREFLY-F3** — NSA history identifies FIREFLY as a public-key algorithm underpinning STU-III. ([S012](../sources/README.md#s012), Printed p.297; PDF p.40, STU-III discussion)

### Technical inferences

- **FIREFLY-I1 · strong** — The scheme belongs in the stage that establishes shared key material for later traffic protection. Basis: FIREFLY-F1, FIREFLY-F3.
- **FIREFLY-I2 · moderate** — Classical exponentiation-based public-key mathematics is a historically grounded hypothesis, not a released specification. Basis: FIREFLY-F2.

### Unresolved details

- An exact identification with Diffie-Hellman, RSA or a particular authenticated variant is not established.
- No online third party does not imply no provisioning, certificates or prior trust.

## SPONDULIX-S

A named KMI key-agreement option.

### Documented statements

- **SPONDULIX-S-F1** — NGLD-M lists SPONDULIX-S alongside ECDH-384 under KMI key agreement. ([S010](../sources/README.md#s010), Table 9, printed p.42)

### Technical inferences

- **SPONDULIX-S-I1 · strong** — It occupies a key-establishment role in KMI. Basis: SPONDULIX-S-F1.

### Unresolved details

- Being listed beside ECDH-384 does not establish identical mathematics, curve parameters or strength.
- First development and first approval dates have not been verified.

## KM-TG signing schemes / SILVER LINING

Authorization and authenticity checks for software updates.

### Documented statements

- **SOFTWARE-SIGNATURES-F1** — NGLD-M describes NSA-signed security-software updates and device-side validation using KM-TG schemes, with an upgrade path to SILVER LINING. ([S010](../sources/README.md#s010), Table 9, printed p.42)

### Technical inferences

- **SOFTWARE-SIGNATURES-I1 · strong** — These schemes establish whether software is accepted as authorized; confidentiality is a separate function in the same update process. Basis: SOFTWARE-SIGNATURES-F1.

### Unresolved details

- The record does not identify SILVER LINING as RSA, elliptic-curve or hash-based signatures.
- The planned transition is not a verified first operational approval date.

## SAVILLE

An older secure-voice lineage with a measurable implementation cost on AIM.

### Documented statements

- **SAVILLE-F1** — NSA history dates the SAVILLE tactical secure-voice program to the late 1960s and associates VINSON with the family. ([S011](../sources/README.md#s011), Printed p.143; PDF p.154, tactical secure-voice discussion)
- **SAVILLE-F2** — Motorola advertises SAVILLE at 0.04 bits per input clock and BATON at 1.29 bits per input clock on AIM. ([S006](../sources/README.md#s006), p.1, Performance)

### Technical inferences

- **SAVILLE-I1 · strong** — Applying the advertised rates at a hypothetical 10 MHz input clock gives 0.4 Mbps for SAVILLE and 12.9 Mbps for BATON, a 32.25-fold throughput ratio. Basis: SAVILLE-F2.
- **SAVILLE-I2 · strong** — The ratio measures implementation cost on that platform, combining algorithm, mode and implementation choices. Basis: SAVILLE-F2.

### Unresolved details

- These performance figures do not identify the internal feedback structure, round count or security margin.
- Detailed online reconstructions require separate evidence from an original design record.

## Additional names and catalogue boundaries

Manufacturer records also attest PADSTONE, CRAYON, KEESEE, GOODSPEED, PHALANX, SHILLELAGH, VALLOR, WALBURN, WEASEL, ACME, JACKKNIFE and Mark XII (CADMUS). Viasat lists CAROUSEL, CARDHOLDER and BELSHAZZAR together with equipment compatibility entries. The [additional-name index](name-index.md) records each name's actual evidence, including several names known only from specification titles. Their presence is not a complete design specification or uniform proof of Suite A membership. See S006, S007, S008, S010 and S018.

## Implementation approval

Harris reports that Sierra II received NSA certification in Harris fiscal 2005 (S016). This is a platform milestone, distinct from the development or first approval of every algorithm it can execute. Original first-approval dates for the individual schemes remain open research questions.
