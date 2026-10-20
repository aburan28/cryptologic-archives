# Siemens T52 / G-schreiber

FRA preserves an institutional history and a participant’s explicitly reconstructed account of the Swedish cryptanalysis.

Region: Germany / Swedish cryptanalytic records  
Role: Historical teleprinter encryption  
Construction: Five-impulse masking and transposition, as described in the published reconstruction  
Parameters: Five teleprinter bit positions; aligned parallel traffic is central to Borelius’s account

### Documented statements

- **INTL-T52-F1** — FRA’s history identifies the G-schreiber as Siemens und Halske T52. It dates the first interception of this teleprinter traffic to 19 May 1940 and describes Beurling’s solution and subsequent logical replicas. ([S137](../../sources/README.md#s137), G-skrivaren, printed pp.8–9 / PDF p.5)
- **INTL-T52-F2** — Borelius’s published account describes five-bit teleprinter symbols subjected to common masking and transposition in aligned parallel messages. Its introduction says the account was written in the 1980s and reconstructs how Beurling may have worked. ([S138](../../sources/README.md#s138), Introduction; passage beginning Dessa tecken har utsatts för samma överlagring och samma transposition; following comparison and transposition discussion)

### Technical inferences

- **INTL-T52-I1 · conditional** — For a fixed mask K and bit permutation pi, the map C=pi(P XOR K) preserves pairwise Hamming distances between aligned plaintext symbols. This explains the kind of comparison described in the account without proving Beurling’s actual sequence of discoveries. Basis: INTL-T52-F2.
  Assumption: The compared messages use the same mask and permutation at the aligned position; no claim is made about all T52 models or operating states.

### Unresolved details

- The retrospective account is not a contemporaneous explanation by Beurling. Exact model variants, full wiring and original German approval dates are outside these sources.

[Companion standards: Swiss and Swedish historical machine records](../../docs/companion-standards.md#historical-archives)
