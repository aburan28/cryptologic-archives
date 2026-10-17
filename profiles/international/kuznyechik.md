# Kuznyechik

The 128-bit cipher standardized alongside Magma in GOST R 34.12-2015.

Region: Russia  
Role: Symmetric encryption  
Construction: Substitution and linear-diffusion network  
Parameters: 128-bit block; 256-bit key; ten round keys

### Documented statements

- **INTL-KUZNYECHIK-F1** — The standard specifies a 128-bit block and 256-bit key. Ten round keys are derived, and encryption applies nine keyed substitution/linear-transform layers followed by a final key XOR. ([S022](../../sources/README.md#s022), Abstract; Sections 4.4 and 4.5.1)
- **INTL-KUZNYECHIK-F2** — Its nonlinear byte substitution, linear transformation and key schedule are explicitly specified with worked examples. ([S022](../../sources/README.md#s022), Sections 4.1-4.4 and 5)
- **INTL-KUZNYECHIK-F3** — The Russian standard is the 2015 edition; the English RFC dates to March 2016. ([S022](../../sources/README.md#s022), Header and normative reference GOSTR3412-2015)

### Technical inferences

- **INTL-KUZNYECHIK-I1 · strong** — The published transformations and vectors permit independent implementations; implementation agreement can be checked without knowing unpublished round details. Basis: INTL-KUZNYECHIK-F1, INTL-KUZNYECHIK-F2.

### Unresolved details

- Sharing a standard with Magma does not make the two ciphers mathematically interchangeable.
