# LIBELLE in SINA

A named government cipher with public architectural and migration evidence.

Region: Germany  
Role: Government network protection  
Construction: Algorithm implemented inside a hardware security module  
Parameters: Internal primitive parameters not established by the cited BSI records

### Documented statements

- **INTL-LIBELLE-F1** — BSI's SINA history says development was commissioned from secunet in 1999. It identifies LIBELLE as an HSM-implemented algorithm used at higher classification levels and describes gradual replacement by a newly approved algorithm. ([S041](../../sources/README.md#s041), SINA im Wandel der Zeit, development and cryptographic migration paragraphs)
- **INTL-LIBELLE-F2** — The preserved SINA brochure is a January 2016 system description covering protected network communication, storage and separation of functions. ([S048](../../sources/README.md#s048), Sections 1 and 4; imprint, January 2016)

### Technical inferences

- **INTL-LIBELLE-I1 · strong** — A stable product-family name such as SINA can span changes in cipher and security hardware. The algorithm, hardware module and product version must be identified separately. Basis: INTL-LIBELLE-F1, INTL-LIBELLE-F2.

### Unresolved details

- The cited sources do not identify the replacement cipher or provide LIBELLE's round function.
- The 1999 SINA contract is a system-development milestone, not a verified first approval of LIBELLE.

[Companion standards: Germany: general recommendations and protocol guidance](../../docs/companion-standards.md#germany)
