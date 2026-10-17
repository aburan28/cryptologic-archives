# JOSEKI

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
