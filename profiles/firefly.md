# FIREFLY / Enhanced FIREFLY

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
