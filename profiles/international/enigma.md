# Enigma

A machine family whose operating procedures and reflector structure are documented in wartime sources.

Region: Germany  
Role: Historical machine encryption  
Construction: Stepped rotor permutations with a reflector  
Parameters: 26-symbol service-machine description; model-dependent rotor/plugboard settings

### Documented statements

- **INTL-ENIGMA-F1** — Turing describes 26-contact rotors, paired reflector contacts, turnover mechanics and plugboard changes. At a fixed machine position, encryption is reciprocal and no letter maps to itself. ([S039](../../sources/README.md#s039), Chapter 1, printed pp.1-4, especially p.2)
- **INTL-ENIGMA-F2** — The 1940 naval manual records a contemporary operational procedure; it is a separate kind of evidence from a patent or a later cryptanalytic account. ([S038](../../sources/README.md#s038), Title page and operational instructions)
- **INTL-ENIGMA-F3** — Scherbius's patent record distinguishes its 23 February 1918 application/priority date from publication on 8 July 1925. ([S054](../../sources/README.md#s054), Patent front page; [S056](../../sources/README.md#s056), Opening paragraph, Scherbius patent application)

### Technical inferences

- **INTL-ENIGMA-I1 · strong** — Writing the fixed-position wiring as E=T^(-1)*R*T shows why E is its own inverse when the reflector R is an involution. A reflector without fixed points also makes E fixed-point-free. Basis: INTL-ENIGMA-F1.
  Assumption: T includes all forward wiring and the reflector pairs distinct contacts; composition is evaluated at one fixed stepping state.

### Unresolved details

- The 1918 patent milestone does not establish the service-approval date of every later Enigma model.
- Different Enigma variants and operating procedures require separate profiles.
