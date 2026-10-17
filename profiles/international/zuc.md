# ZUC / Zu Chongzhi

A public word-oriented stream cipher used as a building block for mobile confidentiality and integrity algorithms.

Region: China / international mobile standards  
Role: Keystream generation  
Construction: LFSR plus nonlinear state machine  
Parameters: 128-bit key; 128-bit IV; 32-bit output words in version 1.6

### Documented statements

- **INTL-ZUC-F1** — Version 1.6 takes a 128-bit key and 128-bit IV and produces 32-bit keystream words. The design combines a 16-cell, 31-bit LFSR, bit reorganization and a nonlinear function. ([S037](../../sources/README.md#s037), Sections 1, 2.1-2.4)
- **INTL-ZUC-F2** — The preserved specification is dated 28 June 2011 and identifies ZUC as the core for 128-EEA3 and 128-EIA3. ([S037](../../sources/README.md#s037), Cover and Section 1)
- **INTL-ZUC-F3** — OSCCA included the Zu Chongzhi industry standard in its 21 March 2012 announcement. ([S034](../../sources/README.md#s034), Announcement list, GM/T0001-2012)

### Technical inferences

- **INTL-ZUC-I1 · strong** — The keystream generator, the confidentiality algorithm and the integrity algorithm occupy different interfaces; the name ZUC alone does not specify the full mobile packet-protection procedure. Basis: INTL-ZUC-F1, INTL-ZUC-F2.

### Unresolved details

- Parameters in this profile apply to the preserved 128-bit version, not automatically to later ZUC-256 variants.

[Companion standards: China and 3GPP: ZUC, EEA3 and EIA3](../../docs/companion-standards.md#zuc)
