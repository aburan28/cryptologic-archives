# International cryptography: constructions and historical records

Research snapshot: 2026-10-17

This collection extends the archive across Soviet/Russian, Chinese, German, Japanese and Korean cryptography. It records public national standards, historical military machines and government systems for which only limited architectural information is public.

Regional labels describe design or historical context. They are not assertions of exclusive use, present-day approval or equivalence to NSA Suite A. Hashes, signatures, key-establishment protocols and encryption ciphers have distinct roles.

Every profile separates source-reported statements, deductions and unresolved details. A patent application, standard issue, implementation date, procurement contract, RFC publication and approval withdrawal are different event types. A public standards document does not identify a country's entire classified cryptographic inventory.

## Comparison

| Region | Scheme | Role / construction | Parameters |
|---|---|---|---|
| Soviet Union / Russia | [GOST 28147-89](../profiles/international/gost-28147.md) | Symmetric encryption and MAC; Feistel block cipher | 64-bit block; 256-bit key; 32 encryption rounds |
| Russia | [Magma](../profiles/international/magma.md) | Symmetric encryption; Feistel block cipher | 64-bit block; 256-bit key; 32 round keys |
| Russia | [Kuznyechik](../profiles/international/kuznyechik.md) | Symmetric encryption; Substitution and linear-diffusion network | 128-bit block; 256-bit key; ten round keys |
| Russia | [Streebog / GOST R 34.11-2012](../profiles/international/streebog.md) | Cryptographic hashing; Iterated compression with substitution, permutation and linear transforms | 256- or 512-bit digest; 512-bit chaining state |
| Russia | [GOST R 34.10-2012](../profiles/international/gost-signatures.md) | Digital signatures; Elliptic-curve discrete-logarithm scheme | Prime-field elliptic curves; 512- or 1024-bit encoded signatures |
| Soviet Union | [FIALKA / M-125 family](../profiles/international/fialka.md) | Historical machine encryption; Electromechanical rotor substitution | Ten rotors; 30 contacts per rotor on examined M-125 specimens |
| China | [SM4 / SMS4](../profiles/international/sm4.md) | Symmetric encryption; Unbalanced Feistel-style word transformation | 128-bit block; 128-bit key; 32 rounds |
| China | [SM3](../profiles/international/sm3.md) | Cryptographic hashing; Iterated word-oriented compression | 256-bit digest; 512-bit message blocks; 64 compression steps |
| China | [SM2 family](../profiles/international/sm2.md) | Signatures, key exchange and public-key encryption; Elliptic-curve cryptography | TLS profile uses a 256-bit prime-field curve |
| China / international mobile standards | [ZUC / Zu Chongzhi](../profiles/international/zuc.md) | Keystream generation; LFSR plus nonlinear state machine | 128-bit key; 128-bit IV; 32-bit output words in version 1.6 |
| Germany | [Enigma](../profiles/international/enigma.md) | Historical machine encryption; Stepped rotor permutations with a reflector | 26-symbol service-machine description; model-dependent rotor/plugboard settings |
| Germany | [Lorenz SZ / Tunny](../profiles/international/lorenz.md) | Historical teleprinter encryption; Additive keystream cipher with wheel-controlled state | Five teleprinter bits; five chi wheels, five psi wheels and motor control |
| Germany | [CHIASMUS](../profiles/international/chiasmus.md) | Government file encryption and historical SINA use; Proprietary symmetric-encryption system; internal construction unresolved here | Key material and format are product-specific in the cited agency account |
| Germany | [LIBELLE in SINA](../profiles/international/libelle.md) | Government network protection; Algorithm implemented inside a hardware security module | Internal primitive parameters not established by the cited BSI records |
| Japan | [Camellia](../profiles/international/camellia.md) | Symmetric encryption; Feistel network with FL/FLINV layers | 128-bit block; 128/192/256-bit keys; 18 or 24 rounds |
| Japan | [CLEFIA](../profiles/international/clefia.md) | Symmetric encryption; Four-branch generalized Feistel network | 128-bit block; 128/192/256-bit keys; 18/22/26 rounds |
| Republic of Korea | [SEED](../profiles/international/seed.md) | Symmetric encryption; 16-round Feistel network | 128-bit block; 128-bit key |
| Republic of Korea | [ARIA](../profiles/international/aria.md) | Symmetric encryption; Substitution and involutive linear-diffusion layers | 128-bit block; 128/192/256-bit keys; 12/14/16 rounds |

See the [international timeline](international-timeline.md), [profile index](../profiles/international/README.md), [companion standards](companion-standards.md), and [source catalogue](../sources/README.md).

## GOST 28147-89

A Soviet standard whose public description exposes the round function, key schedule and modes.

Region: Soviet Union / Russia  
Role: Symmetric encryption and MAC  
Construction: Feistel block cipher  
Parameters: 64-bit block; 256-bit key; 32 encryption rounds

### Documented statements

- **INTL-GOST-28147-F1** — The encryption core processes 64-bit blocks using a 256-bit key and 32 rounds. Its round transformation combines addition modulo 2^32, eight 4-bit substitutions, an 11-bit cyclic rotation and XOR. ([S020](../sources/README.md#s020), Sections 4 and 5.1)
- **INTL-GOST-28147-F2** — The 1989 standard leaves substitution tables to a parameter set; RFC 4357 supplies named parameter sets and identifiers. ([S020](../sources/README.md#s020), Section 4, S-box remark and long-term parameter discussion)
- **INTL-GOST-28147-F3** — RFC 4357 gives concrete encryption parameter-set encodings and S-box tables. ([S050](../sources/README.md#s050), Sections 8.1, 11.1 and 11.2)
- **INTL-GOST-28147-F4** — The reference standard is dated 1989; the preserved English RFC was published in March 2010. ([S020](../sources/README.md#s020), Header and Section 10, GOST28147-89 reference)

### Technical inferences

- **INTL-GOST-28147-I1 · strong** — The label GOST 28147-89 is insufficient for interoperable encryption: the S-box parameter set and mode must also be specified. Basis: INTL-GOST-28147-F1, INTL-GOST-28147-F2, INTL-GOST-28147-F3.

### Unresolved details

- The 1989 standard date does not establish the original internal design date or approval for every later product.

[Companion standards: Russia: GOST parameters, modes and protocol bindings](../docs/companion-standards.md#gost)

## Magma

The updated 64-bit cipher in GOST R 34.12-2015, with important compatibility details.

Region: Russia  
Role: Symmetric encryption  
Construction: Feistel block cipher  
Parameters: 64-bit block; 256-bit key; 32 round keys

### Documented statements

- **INTL-MAGMA-F1** — Magma uses a 64-bit block and 256-bit key; its specified encryption composition uses 32 round keys. ([S021](../sources/README.md#s021), Abstract; Sections 4.2, 4.3 and 5.1)
- **INTL-MAGMA-F2** — Relative to GOST 28147-89, the RFC fixes the S-box set and changes key/block parsing conventions, including big-endian key parsing. ([S021](../sources/README.md#s021), Appendix B, Background)
- **INTL-MAGMA-F3** — Its national-standard edition is 2015; RFC 8891 was published in September 2020. ([S021](../sources/README.md#s021), Header, Introduction and normative reference GOSTR3412-2015)

### Technical inferences

- **INTL-MAGMA-I1 · strong** — Replacing a legacy GOST implementation by changing its displayed algorithm name is insufficient: representation and parameter choices can change ciphertext. Basis: INTL-MAGMA-F1, INTL-MAGMA-F2.

### Unresolved details

- The 2020 RFC date is an English-publication milestone, not the cipher invention date.

[Companion standards: Russia: GOST parameters, modes and protocol bindings](../docs/companion-standards.md#gost)

## Kuznyechik

The 128-bit cipher standardized alongside Magma in GOST R 34.12-2015.

Region: Russia  
Role: Symmetric encryption  
Construction: Substitution and linear-diffusion network  
Parameters: 128-bit block; 256-bit key; ten round keys

### Documented statements

- **INTL-KUZNYECHIK-F1** — The standard specifies a 128-bit block and 256-bit key. Ten round keys are derived, and encryption applies nine keyed substitution/linear-transform layers followed by a final key XOR. ([S022](../sources/README.md#s022), Abstract; Sections 4.4 and 4.5.1)
- **INTL-KUZNYECHIK-F2** — Its nonlinear byte substitution, linear transformation and key schedule are explicitly specified with worked examples. ([S022](../sources/README.md#s022), Sections 4.1-4.4 and 5)
- **INTL-KUZNYECHIK-F3** — The Russian standard is the 2015 edition; the English RFC dates to March 2016. ([S022](../sources/README.md#s022), Header and normative reference GOSTR3412-2015)

### Technical inferences

- **INTL-KUZNYECHIK-I1 · strong** — The published transformations and vectors permit independent implementations; implementation agreement can be checked without knowing unpublished round details. Basis: INTL-KUZNYECHIK-F1, INTL-KUZNYECHIK-F2.

### Unresolved details

- Sharing a standard with Magma does not make the two ciphers mathematically interchangeable.

[Companion standards: Russia: GOST parameters, modes and protocol bindings](../docs/companion-standards.md#gost)

## Streebog / GOST R 34.11-2012

A hash-function standard, with a fully specified compression construction.

Region: Russia  
Role: Cryptographic hashing  
Construction: Iterated compression with substitution, permutation and linear transforms  
Parameters: 256- or 512-bit digest; 512-bit chaining state

### Documented statements

- **INTL-STREEBOG-F1** — GOST R 34.11-2012 defines 256-bit and 512-bit digest variants. Both use a 512-bit chaining state and specified S, P and L transformations. ([S023](../sources/README.md#s023), Sections 5-9)
- **INTL-STREEBOG-F2** — The compression function combines a keyed internal transformation with the previous chaining value and message block by XOR; finalization also processes message length and a block sum. ([S023](../sources/README.md#s023), Sections 8 and 9)
- **INTL-STREEBOG-F3** — The standard edition is 2012; the preserved English publication is RFC 6986 of August 2013. ([S023](../sources/README.md#s023), Header and normative reference GOST3411-2012)

### Technical inferences

- **INTL-STREEBOG-I1 · strong** — A 256-bit digest is an output length. It is not a 256-bit encryption key, and a hash interface does not provide a decryption operation. Basis: INTL-STREEBOG-F1, INTL-STREEBOG-F2.

### Unresolved details

- This profile records the specified construction, not a complete survey of subsequent cryptanalysis.

[Companion standards: Russia: GOST parameters, modes and protocol bindings](../docs/companion-standards.md#gost)

## GOST R 34.10-2012

The GOST signature standard is a separate mathematical object from GOST block ciphers.

Region: Russia  
Role: Digital signatures  
Construction: Elliptic-curve discrete-logarithm scheme  
Parameters: Prime-field elliptic curves; 512- or 1024-bit encoded signatures

### Documented statements

- **INTL-GOST-SIGNATURES-F1** — The standard defines signing and verification using an elliptic-curve point group over a prime finite field. It specifies signature encodings of 512 or 1024 bits. ([S024](../sources/README.md#s024), Sections 1.2, 4 and 5)
- **INTL-GOST-SIGNATURES-F2** — The signing rule uses an ephemeral scalar k, point C=kP, r=x_C mod q, and s=(r*d+k*e) mod q, with the specified hash-to-integer and retry rules. ([S024](../sources/README.md#s024), Section 6.1)
- **INTL-GOST-SIGNATURES-F3** — The standard edition is 2012 and the English RFC is dated December 2013. ([S024](../sources/README.md#s024), Header and Section 1.1)

### Technical inferences

- **INTL-GOST-SIGNATURES-I1 · strong** — GOST can name an ecosystem containing signatures, hashes and ciphers. A signature length alone cannot identify the block cipher used by a product. Basis: INTL-GOST-SIGNATURES-F1, INTL-GOST-SIGNATURES-F2.

### Unresolved details

- A product profile must additionally identify curve parameters, hash function and encoding conventions.

[Companion standards: Russia: GOST parameters, modes and protocol bindings](../docs/companion-standards.md#gost)

## FIALKA / M-125 family

A Cold War cipher-machine family documented through surviving artifacts and a German-language manual.

Region: Soviet Union  
Role: Historical machine encryption  
Construction: Electromechanical rotor substitution  
Parameters: Ten rotors; 30 contacts per rotor on examined M-125 specimens

### Documented statements

- **INTL-FIALKA-F1** — The examined M-125 machines have ten 30-contact rotors; adjacent rotors move in opposite directions. A punched card sets internal connections, and the machine prints and punches paper tape. ([S051](../sources/README.md#s051), General Description; Input and Output; Card Reader; Direction of Rotor Rotation)
- **INTL-FIALKA-F2** — The preserved manual covers M-125-MN and M-125-3MN. Its digitizer introduction is dated 24 March 2005 and explicitly notes missing original pages 2, 4 and 60. ([S025](../sources/README.md#s025), PDF pp.1-2, digitizer cover and introduction)

### Technical inferences

- **INTL-FIALKA-I1 · strong** — These are changing symbol permutations implemented with physical contacts and stepping mechanics. A modern fixed-width block-cipher API would omit important machine-state and operating-procedure details. Basis: INTL-FIALKA-F1.

### Unresolved details

- The original manual date and first service-approval date are not verified here.
- Variant-specific reflector connections and rotor sets require examination of the particular model.

## SM4 / SMS4

A public block cipher whose earlier name SMS4 and later standard numbers describe different historical milestones.

Region: China  
Role: Symmetric encryption  
Construction: Unbalanced Feistel-style word transformation  
Parameters: 128-bit block; 128-bit key; 32 rounds

### Documented statements

- **INTL-SM4-F1** — The published transformation uses four 32-bit state words, 32 rounds, byte S-box substitution and a linear layer built from XOR and rotations. Both block and key are 128 bits. ([S027](../sources/README.md#s027), Sections 4, 6 and 7)
- **INTL-SM4-F2** — In compact notation, the update is X[i+4]=X[i] XOR T(X[i+1] XOR X[i+2] XOR X[i+3] XOR rk[i]); output reverses the final four words. ([S027](../sources/README.md#s027), Sections 6.1 and 7.1)
- **INTL-SM4-F3** — Diffie and Ledin's dated May 2008 translation reports that SMS4 was issued in January 2006. OSCCA explicitly identified SM4 as formerly SMS4 in its March 2012 announcement. ([S053](../sources/README.md#s053), Cover and introductory paragraph; [S034](../sources/README.md#s034), Announcement list, GM/T0002-2012)
- **INTL-SM4-F4** — The official national record gives GB/T 32907-2016 an issue date of 29 August 2016 and an implementation date of 1 March 2017. ([S035](../sources/README.md#s035), Publication and implementation metadata)

### Technical inferences

- **INTL-SM4-I1 · strong** — A protocol entry such as SM4-GCM identifies a block cipher plus a mode. Its authentication and nonce rules belong to the full protocol profile, rather than to the SM4 round function alone. Basis: INTL-SM4-F1, INTL-SM4-F2.

### Unresolved details

- The hosted English translation lacks an official dated Chinese cover; its edition is not established by its filename.

[Companion standards: China: original releases, parameters and successive standards](../docs/companion-standards.md#shangmi)

## SM3

A public hash specification built from Boolean functions, word additions, rotations and message expansion.

Region: China  
Role: Cryptographic hashing  
Construction: Iterated word-oriented compression  
Parameters: 256-bit digest; 512-bit message blocks; 64 compression steps

### Documented statements

- **INTL-SM3-F1** — SM3 pads messages into 512-bit blocks and updates a 256-bit chaining value with a compression function. That function iterates j from 0 to 63. ([S028](../sources/README.md#s028), Sections 5.1-5.3.3)
- **INTL-SM3-F2** — The compression state comprises eight 32-bit words, using specified Boolean functions, rotations, additions and permutations P0/P1. ([S028](../sources/README.md#s028), Sections 3, 4 and 5.3.3)
- **INTL-SM3-F3** — OSCCA announced GM/T 0004-2012 for SM3 on 21 March 2012. RFC 8998 later specifies SM3 in its SM TLS 1.3 profile. ([S034](../sources/README.md#s034), Announcement list, GM/T0004-2012; [S026](../sources/README.md#s026), Sections 1.1 and 3.4)
- **INTL-SM3-F4** — The official announcement of 2010-12-17 released SM3 with an attached algorithm specification whose cover is dated December 2010, preceding the 2012 industry-standard announcement. ([S071](../sources/README.md#s071), Announcement date and attachment link; [S098](../sources/README.md#s098), Cover and Sections 4–5)

### Technical inferences

- **INTL-SM3-I1 · strong** — The concrete object is a digest computation, with message expansion and compression, rather than a bulk-encryption key schedule. Basis: INTL-SM3-F1, INTL-SM3-F2.

### Unresolved details

- A 256-bit digest length alone does not establish every security property or interoperability with other 256-bit hashes.

[Companion standards: China: original releases, parameters and successive standards](../docs/companion-standards.md#shangmi)

## SM2 family

SM2 names several related algorithms; the operation and protocol must be identified.

Region: China  
Role: Signatures, key exchange and public-key encryption  
Construction: Elliptic-curve cryptography  
Parameters: TLS profile uses a 256-bit prime-field curve

### Documented statements

- **INTL-SM2-F1** — The preserved parts separately describe general elliptic-curve operations, signatures, key exchange, public-key encryption and parameter definition. ([S029](../sources/README.md#s029), Title and Scope; companion parts S030-S033; [S030](../sources/README.md#s030), Title and Scope; companion parts S031-S033)
- **INTL-SM2-F2** — The signature algorithm hashes an identity-bound value with the message; its signing equations include r=(e+x1) mod n and s=(1+d)^(-1)*(k-r*d) mod n, with required retry conditions. ([S030](../sources/README.md#s030), Sections 5.5 and 6.1)
- **INTL-SM2-F3** — RFC 8998 specifies a 256-bit prime-field curve and uses SM2 signatures with SM3. Its TLS key exchange is ECDHE over that curve. ([S026](../sources/README.md#s026), Sections 1, 3.2.1 and 3.3)
- **INTL-SM2-F4** — OSCCA announced the GM/T SM2 family in March 2012. The official GB/T Part 1 record was issued in August 2016 and implemented in March 2017. ([S036](../sources/README.md#s036), Publication and implementation metadata; [S034](../sources/README.md#s034), Announcement list, GM/T0003-2012)
- **INTL-SM2-F5** — Before the later GM/T and GB/T standards, the official announcement of 2010-12-17 released SM2 with a four-part algorithm PDF dated December 2010 and a separate recommended-curve parameter sheet. ([S070](../sources/README.md#s070), Announcement date and attachment links; [S096](../sources/README.md#s096), Part covers at PDF pages 1, 47, 61 and 80; [S097](../sources/README.md#s097), One-page parameter sheet)

### Technical inferences

- **INTL-SM2-I1 · strong** — Using the SM2 curve for ECDHE in TLS does not by itself mean that the native SM2 Part 3 key-exchange protocol is being executed. Basis: INTL-SM2-F1, INTL-SM2-F3.

### Unresolved details

- The English Part 5 filename says 2016, whereas RFC 8998 cites GB/T 32918.5-2017. The filename must not be treated as authoritative edition metadata.

[Companion standards: China: original releases, parameters and successive standards](../docs/companion-standards.md#shangmi)

## ZUC / Zu Chongzhi

A public word-oriented stream cipher used as a building block for mobile confidentiality and integrity algorithms.

Region: China / international mobile standards  
Role: Keystream generation  
Construction: LFSR plus nonlinear state machine  
Parameters: 128-bit key; 128-bit IV; 32-bit output words in version 1.6

### Documented statements

- **INTL-ZUC-F1** — Version 1.6 takes a 128-bit key and 128-bit IV and produces 32-bit keystream words. The design combines a 16-cell, 31-bit LFSR, bit reorganization and a nonlinear function. ([S037](../sources/README.md#s037), Sections 1, 2.1-2.4)
- **INTL-ZUC-F2** — The preserved specification is dated 28 June 2011 and identifies ZUC as the core for 128-EEA3 and 128-EIA3. ([S037](../sources/README.md#s037), Cover and Section 1)
- **INTL-ZUC-F3** — OSCCA included the Zu Chongzhi industry standard in its 21 March 2012 announcement. ([S034](../sources/README.md#s034), Announcement list, GM/T0001-2012)

### Technical inferences

- **INTL-ZUC-I1 · strong** — The keystream generator, the confidentiality algorithm and the integrity algorithm occupy different interfaces; the name ZUC alone does not specify the full mobile packet-protection procedure. Basis: INTL-ZUC-F1, INTL-ZUC-F2.

### Unresolved details

- Parameters in this profile apply to the preserved 128-bit version, not automatically to later ZUC-256 variants.

[Companion standards: China and 3GPP: ZUC, EEA3 and EIA3](../docs/companion-standards.md#zuc)

## Enigma

A machine family whose operating procedures and reflector structure are documented in wartime sources.

Region: Germany  
Role: Historical machine encryption  
Construction: Stepped rotor permutations with a reflector  
Parameters: 26-symbol service-machine description; model-dependent rotor/plugboard settings

### Documented statements

- **INTL-ENIGMA-F1** — Turing describes 26-contact rotors, paired reflector contacts, turnover mechanics and plugboard changes. At a fixed machine position, encryption is reciprocal and no letter maps to itself. ([S039](../sources/README.md#s039), Chapter 1, printed pp.1-4, especially p.2)
- **INTL-ENIGMA-F2** — The 1940 naval manual records a contemporary operational procedure; it is a separate kind of evidence from a patent or a later cryptanalytic account. ([S038](../sources/README.md#s038), Title page and operational instructions)
- **INTL-ENIGMA-F3** — Scherbius's patent record distinguishes its 23 February 1918 application/priority date from publication on 8 July 1925. ([S054](../sources/README.md#s054), Patent front page; [S056](../sources/README.md#s056), Opening paragraph, Scherbius patent application)

### Technical inferences

- **INTL-ENIGMA-I1 · strong** — Writing the fixed-position wiring as E=T^(-1)*R*T shows why E is its own inverse when the reflector R is an involution. A reflector without fixed points also makes E fixed-point-free. Basis: INTL-ENIGMA-F1.
  Assumption: T includes all forward wiring and the reflector pairs distinct contacts; composition is evaluated at one fixed stepping state.

### Unresolved details

- The 1918 patent milestone does not establish the service-approval date of every later Enigma model.
- Different Enigma variants and operating procedures require separate profiles.

## Lorenz SZ / Tunny

Tunny is the British cryptanalytic name used in the preserved wartime record.

Region: Germany  
Role: Historical teleprinter encryption  
Construction: Additive keystream cipher with wheel-controlled state  
Parameters: Five teleprinter bits; five chi wheels, five psi wheels and motor control

### Documented statements

- **INTL-LORENZ-F1** — The wartime dictionary describes five regularly moving chi wheels, five psi wheels with controlled movement, and motor-wheel control of the psi movement. ([S055](../sources/README.md#s055), Entries CHI, PSI, MOTOR-WHEELS and TUNNY)
- **INTL-LORENZ-F2** — The Newmanry report describes machine-based setting work beginning in December 1942 and pilot Robinson and Tunny machines arriving in April 1943. ([S040](../sources/README.md#s040), Section 31A, original p.276)
- **INTL-LORENZ-F3** — The report treats five-impulse teleprinter characters, chi/psi components and addition modulo 2 in its account of Tunny and decoding machines. ([S040](../sources/README.md#s040), Section 56J, original pp.376-378)

### Technical inferences

- **INTL-LORENZ-I1 · strong** — At the additive interface C=P XOR K, reuse of the same keystream yields C1 XOR C2=P1 XOR P2. This is a property of keystream reuse, independent of the number of wheels. Basis: INTL-LORENZ-F1, INTL-LORENZ-F3.
  Assumption: The two messages use the same keystream at aligned bit positions.

### Unresolved details

- The preserved 1942-1945 British milestones do not date the original German invention or every SZ40/SZ42 deployment.
- The Newmanry PDF is a transcription of part of the report, not the complete wartime original.

## CHIASMUS

A German government example where public lifecycle evidence is clearer than the primitive's internals.

Region: Germany  
Role: Government file encryption and historical SINA use  
Construction: Proprietary symmetric-encryption system; internal construction unresolved here  
Parameters: Key material and format are product-specific in the cited agency account

### Documented statements

- **INTL-CHIASMUS-F1** — BSI dates the Windows Chiasmus file-encryption program to 2001, followed by a Linux command-line version. Partners had to exchange secret key material beforehand. ([S042](../sources/README.md#s042), Section 1, printed p.4)
- **INTL-CHIASMUS-F2** — BSI describes non-open algorithms and standards and proprietary software; it says Chiasmus key material is incompatible with replacement products. ([S042](../sources/README.md#s042), Section 1, printed p.4)
- **INTL-CHIASMUS-F3** — BSI states that the VS-NfD approval was withdrawn on 30 June 2022. Its SINA history separately records replacing CHIASMUS by AES at lower classification levels. ([S042](../sources/README.md#s042), Section 1, printed p.4; [S041](../sources/README.md#s041), Cryptographic migration paragraph)

### Technical inferences

- **INTL-CHIASMUS-I1 · strong** — A file archive or migration tool needs the actual container, key format and implementation behavior; merely selecting another symmetric cipher cannot make a Chiasmus file readable. Basis: INTL-CHIASMUS-F1, INTL-CHIASMUS-F2.

### Unresolved details

- The cited agency records do not expose a complete round function or establish the cipher's original design date.
- Independent reverse engineering should be catalogued separately from an official design release.

[Companion standards: Germany: general recommendations and protocol guidance](../docs/companion-standards.md#germany)

## LIBELLE in SINA

A named government cipher with public architectural and migration evidence.

Region: Germany  
Role: Government network protection  
Construction: Algorithm implemented inside a hardware security module  
Parameters: Internal primitive parameters not established by the cited BSI records

### Documented statements

- **INTL-LIBELLE-F1** — BSI's SINA history says development was commissioned from secunet in 1999. It identifies LIBELLE as an HSM-implemented algorithm used at higher classification levels and describes gradual replacement by a newly approved algorithm. ([S041](../sources/README.md#s041), SINA im Wandel der Zeit, development and cryptographic migration paragraphs)
- **INTL-LIBELLE-F2** — The preserved SINA brochure is a January 2016 system description covering protected network communication, storage and separation of functions. ([S048](../sources/README.md#s048), Sections 1 and 4; imprint, January 2016)

### Technical inferences

- **INTL-LIBELLE-I1 · strong** — A stable product-family name such as SINA can span changes in cipher and security hardware. The algorithm, hardware module and product version must be identified separately. Basis: INTL-LIBELLE-F1, INTL-LIBELLE-F2.

### Unresolved details

- The cited sources do not identify the replacement cipher or provide LIBELLE's round function.
- The 1999 SINA contract is a system-development milestone, not a verified first approval of LIBELLE.

[Companion standards: Germany: general recommendations and protocol guidance](../docs/companion-standards.md#germany)

## Camellia

A designer-published cipher from NTT and Mitsubishi Electric with early CRYPTREC records.

Region: Japan  
Role: Symmetric encryption  
Construction: Feistel network with FL/FLINV layers  
Parameters: 128-bit block; 128/192/256-bit keys; 18 or 24 rounds

### Documented statements

- **INTL-CAMELLIA-F1** — Camellia was jointly developed by NTT and Mitsubishi Electric. It has a 128-bit block and 128-, 192- and 256-bit key options. ([S043](../sources/README.md#s043), Abstract and Section 1.1)
- **INTL-CAMELLIA-F2** — The data path has 18 rounds for 128-bit keys and 24 rounds for the larger keys, with FL and FLINV functions inserted every six rounds. ([S043](../sources/README.md#s043), Sections 2.3 and 2.4)
- **INTL-CAMELLIA-F3** — The designer archive identifies a 12 July 2000 CRYPTREC specification and a 26 September 2001 version 2.0. The English RFC followed in April 2004. ([S047](../sources/README.md#s047), Version 2.0 title and revision record; companion 2000 submission S052; [S052](../sources/README.md#s052), 2000 designer submission; [S043](../sources/README.md#s043), Header)

### Technical inferences

- **INTL-CAMELLIA-I1 · strong** — A 128-bit block interface with several key sizes does not imply AES internals: Camellia's specified data path is a Feistel construction with additional keyed layers. Basis: INTL-CAMELLIA-F1, INTL-CAMELLIA-F2.

### Unresolved details

- A submission, an algorithm publication and a national procurement approval are separate historical milestones.

[Companion standards: Japan: CRYPTREC selections and Camellia protocol profiles](../docs/companion-standards.md#japan)

## CLEFIA

Sony's published cipher gives an explicit alternative to a two-branch Feistel network.

Region: Japan  
Role: Symmetric encryption  
Construction: Four-branch generalized Feistel network  
Parameters: 128-bit block; 128/192/256-bit keys; 18/22/26 rounds

### Documented statements

- **INTL-CLEFIA-F1** — Sony's version 1.0 specification is dated 1 June 2007. It uses four 32-bit data branches and 18, 22 or 26 rounds for the three key sizes. ([S049](../sources/README.md#s049), Cover; Sections 1 and 4.2)
- **INTL-CLEFIA-F2** — The data-processing part uses a four-branch generalized Feistel network; an eight-branch construction also appears in scheduling larger keys. ([S044](../sources/README.md#s044), Section 4)
- **INTL-CLEFIA-F3** — The English RFC specification was published in March 2011 and dates the algorithm's public publication to 2007. ([S044](../sources/README.md#s044), Header and Introduction)

### Technical inferences

- **INTL-CLEFIA-I1 · strong** — The four-branch structure is a concrete design distinction, despite sharing a 128-bit block interface and key-size choices with several other ciphers. Basis: INTL-CLEFIA-F1, INTL-CLEFIA-F2.

### Unresolved details

- The preserved design dates do not establish when every Sony product first deployed CLEFIA.

[Companion standards: Japan: CRYPTREC selections and Camellia protocol profiles](../docs/companion-standards.md#japan)

## SEED

A Korean national cipher with a public description of its round structure.

Region: Republic of Korea  
Role: Symmetric encryption  
Construction: 16-round Feistel network  
Parameters: 128-bit block; 128-bit key

### Documented statements

- **INTL-SEED-F1** — RFC 4269 describes SEED as developed by KISA since 1998 and as a Korean national standard. It specifies a 128-bit block, a 128-bit key and 16 Feistel rounds. ([S045](../sources/README.md#s045), Section 1.2)
- **INTL-SEED-F2** — The public round description includes S-box transformations, permutations, XOR and addition, with an explicit key schedule and test data. ([S045](../sources/README.md#s045), Sections 2 and 3; appendices)
- **INTL-SEED-F3** — The preserved RFC is dated December 2005 and replaces the earlier RFC 4009 description. ([S045](../sources/README.md#s045), Header and Abstract)

### Technical inferences

- **INTL-SEED-I1 · strong** — SEED provides an example where both the primitive's structure and development period can be stated from a published specification, while product certification remains a separate question. Basis: INTL-SEED-F1, INTL-SEED-F2.

### Unresolved details

- This profile concerns the 128-bit SEED specification in RFC 4269, not every later similarly named variant.

[Companion standards: Republic of Korea: SEED and ARIA protocol profiles](../docs/companion-standards.md#korea)

## ARIA

A Korean cipher with public development and standardization milestones.

Region: Republic of Korea  
Role: Symmetric encryption  
Construction: Substitution and involutive linear-diffusion layers  
Parameters: 128-bit block; 128/192/256-bit keys; 12/14/16 rounds

### Documented statements

- **INTL-ARIA-F1** — RFC 5794 dates development by Korean cryptographers to 2003 and Korean standardization to 2004. It specifies 128-bit blocks with 12, 14 or 16 rounds depending on key size. ([S046](../sources/README.md#s046), Section 1)
- **INTL-ARIA-F2** — The round transformations alternate substitution layers, use XOR key addition and a diffusion map A satisfying A(A(x))=x. ([S046](../sources/README.md#s046), Sections 2.4.1-2.4.3)
- **INTL-ARIA-F3** — The preserved English RFC was published in March 2010. ([S046](../sources/README.md#s046), Header)

### Technical inferences

- **INTL-ARIA-I1 · strong** — The diffusion map's involution is a specific algebraic property. It does not mean encryption is self-inverse without the specified key-schedule and round transformations. Basis: INTL-ARIA-F1, INTL-ARIA-F2.

### Unresolved details

- The 2004 national-standard milestone is not proof of universal approval for all Korean government information.

[Companion standards: Republic of Korea: SEED and ARIA protocol profiles](../docs/companion-standards.md#korea)

## Translation and preservation notes

The seven English SM2/SM3/SM4 files are preserved as hosted by Alipay. Their covers lack official dated Chinese standard identifiers; the filenames alone do not verify an edition or an authorized translation. In particular, the SM2 Part 5 filename contains 2016 while RFC 8998 cites a 2017 standard. The catalogue keeps this discrepancy visible. Official Chinese records and the contemporary OSCCA announcement provide separate date evidence.

Official 2010 SM2 Parts 1–4, the recommended-curve sheet, and the original SM3 release are now preserved separately (S096–S098), together with the 2010-12-17 announcements (S070–S071). These earlier release texts are distinct from the hosted English translations and later GM/T/GB/T editions.

The Fialka manual copy explicitly lacks original pages 2, 4 and 60. Turing Chapter 1, the Newmanry report portion and the Bletchley dictionary are edited transcriptions. They are labeled as such. Original RFC text is preserved when that is the publisher's available source format.

## Further acquisitions

The archive can be extended with independently sourced French, Swiss, Swedish, Israeli, Indian and other collections; earlier Chinese cryptologic history; and public records of additional Soviet equipment. Record a concrete source and its provenance before adding a design or approval claim. This edition does not claim worldwide completeness.
