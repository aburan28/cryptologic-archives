# ARIA

A Korean cipher with public development and standardization milestones.

Region: Republic of Korea  
Role: Symmetric encryption  
Construction: Substitution and involutive linear-diffusion layers  
Parameters: 128-bit block; 128/192/256-bit keys; 12/14/16 rounds

### Documented statements

- **INTL-ARIA-F1** — RFC 5794 dates development by Korean cryptographers to 2003 and Korean standardization to 2004. It specifies 128-bit blocks with 12, 14 or 16 rounds depending on key size. ([S046](../../sources/README.md#s046), Section 1)
- **INTL-ARIA-F2** — The round transformations alternate substitution layers, use XOR key addition and a diffusion map A satisfying A(A(x))=x. ([S046](../../sources/README.md#s046), Sections 2.4.1-2.4.3)
- **INTL-ARIA-F3** — The preserved English RFC was published in March 2010. ([S046](../../sources/README.md#s046), Header)

### Technical inferences

- **INTL-ARIA-I1 · strong** — The diffusion map's involution is a specific algebraic property. It does not mean encryption is self-inverse without the specified key-schedule and round transformations. Basis: INTL-ARIA-F1, INTL-ARIA-F2.

### Unresolved details

- The 2004 national-standard milestone is not proof of universal approval for all Korean government information.
