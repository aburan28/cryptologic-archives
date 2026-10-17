# Lorenz SZ / Tunny

Tunny is the British cryptanalytic name used in the preserved wartime record.

Region: Germany  
Role: Historical teleprinter encryption  
Construction: Additive keystream cipher with wheel-controlled state  
Parameters: Five teleprinter bits; five chi wheels, five psi wheels and motor control

### Documented statements

- **INTL-LORENZ-F1** — The wartime dictionary describes five regularly moving chi wheels, five psi wheels with controlled movement, and motor-wheel control of the psi movement. ([S055](../../sources/README.md#s055), Entries CHI, PSI, MOTOR-WHEELS and TUNNY)
- **INTL-LORENZ-F2** — The Newmanry report describes machine-based setting work beginning in December 1942 and pilot Robinson and Tunny machines arriving in April 1943. ([S040](../../sources/README.md#s040), Section 31A, original p.276)
- **INTL-LORENZ-F3** — The report treats five-impulse teleprinter characters, chi/psi components and addition modulo 2 in its account of Tunny and decoding machines. ([S040](../../sources/README.md#s040), Section 56J, original pp.376-378)

### Technical inferences

- **INTL-LORENZ-I1 · strong** — At the additive interface C=P XOR K, reuse of the same keystream yields C1 XOR C2=P1 XOR P2. This is a property of keystream reuse, independent of the number of wheels. Basis: INTL-LORENZ-F1, INTL-LORENZ-F3.
  Assumption: The two messages use the same keystream at aligned bit positions.

### Unresolved details

- The preserved 1942-1945 British milestones do not date the original German invention or every SZ40/SZ42 deployment.
- The Newmanry PDF is a transcription of part of the report, not the complete wartime original.
