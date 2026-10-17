# ACCORDION

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
