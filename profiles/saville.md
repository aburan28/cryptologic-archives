# SAVILLE

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
