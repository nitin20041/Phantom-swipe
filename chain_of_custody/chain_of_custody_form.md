# Chain of Custody Form — Operation Phantom Swipe

**Case Reference:** OPS-2026-CC-0091 (Simulated)
**Investigating Unit:** Cyber Forensics Lab (Simulated Exercise)

---

## Section A — Item Details

| Item # | Description | Serial/ID | Seizure Location | Date/Time Seized |
|---|---|---|---|---|
| E-01 | ATM Skimmer Device (card-reader overlay + camera) | SK-DUMMY-77821 | Gurgaon Branch ATM, near sector 44 | 2026-08-05, 22:14 IST |
| E-02 | Android Smartphone (fraudulent apps + comms) | IMEI-DUMMY-000112233 | Suspect residence, Gurgaon | 2026-08-06, 06:40 IST |

## Section B — Seizing Officer Declaration

I, the seizing officer, confirm the above items were seized in the presence
of an independent witness and photographed *in situ* prior to handling.
Both devices were placed in anti-static, tamper-evident evidence bags
(seal numbers **TE-4471** and **TE-4472**) immediately upon seizure.

## Section C — Evidence Handling / Write-Blocker Protocol

1. Devices transported to the lab in sealed bags; seals verified unbroken on arrival.
2. All storage media imaged using a **hardware write-blocker** to prevent
   modification of source data (no direct read/write access to original media).
3. Forensic image acquired as a bit-for-bit copy; **SHA-256 hash** computed
   on both the source (where feasible) and the resulting image immediately
   after acquisition — see `hashes/hash_values.txt`.
4. Two copies of each image made: one **working copy** for analysis, one
   **sealed master copy** kept unopened for court production.
5. All access to the working copy logged in Section D below.

## Section D — Custody Log

| # | Date/Time | Released By | Received By | Purpose | Item(s) |
|---|---|---|---|---|---|
| 1 | 2026-08-06 07:10 | Seizing Officer (S. Rao) | Evidence Custodian (A. Mehta) | Intake & bagging | E-01, E-02 |
| 2 | 2026-08-06 09:30 | Evidence Custodian (A. Mehta) | Forensic Examiner (P. Iyer) | Imaging via write-blocker | E-01, E-02 |
| 3 | 2026-08-06 14:00 | Forensic Examiner (P. Iyer) | Evidence Custodian (A. Mehta) | Return after imaging; master copy sealed | E-01, E-02 |
| 4 | 2026-08-07 10:00 | Evidence Custodian (A. Mehta) | Forensic Examiner (P. Iyer) | Working-copy analysis (this assignment) | Working images only |

## Section E — Integrity Verification

Hash of each acquired file/image is recorded at intake and re-verified
before and after every analysis session (see `hashes/hash_values.txt` and
`scripts/generate_hashes.py`). Any mismatch triggers immediate escalation
and suspension of analysis pending review.

## Section F — Signatures (Simulated)

| Role | Name (Simulated) | Signature | Date |
|---|---|---|---|
| Seizing Officer | S. Rao | *[signed]* | 2026-08-06 |
| Evidence Custodian | A. Mehta | *[signed]* | 2026-08-06 |
| Forensic Examiner | P. Iyer | *[signed]* | 2026-08-07 |
| Independent Witness | R. Nair | *[signed]* | 2026-08-06 |

---
*This is a simulated academic exercise. All names, IDs, and evidence are synthetic.*
