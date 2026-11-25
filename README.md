# Operation Phantom Swipe
### Investigating a Cross-Border ATM & Credit Card Fraud Ring
**Assignment 1 — Unit 1: Foundations of Digital Forensics**

> ⚠️ All evidence, names, devices, card numbers, and communications in this
> repository are **synthetic/simulated** for academic purposes only. No real
> individuals, devices, or financial data are involved.

## 1. Repository Structure

```
.
├── README.md                          # this file
├── taxonomy/
│   └── cybercrime_taxonomy.md         # Sub-Problem 1: classification + legal mapping
├── evidence/
│   ├── skimmer_device/                # simulated skimmer data dump
│   └── phone_device/                  # simulated phone data (apps, comms, txns)
├── chain_of_custody/
│   └── chain_of_custody_form.md       # Sub-Problem 2: custody form + handling SOP
├── hashes/
│   └── hash_values.txt                # SHA-256 hashes of all acquired files
├── artifacts/
│   ├── search_log.txt                 # Sub-Problem 3: automated search output
│   └── evidence_log.md                # search strategy + key findings write-up
├── crypto/
│   ├── protected_batch.zip            # Sub-Problem 4: password-protected archive
│   ├── wordlist.txt                   # dictionary used for the cracking simulation
│   ├── cracking_log.txt               # output of the cracking attempt
│   └── cryptography_discussion.md     # ethical/legal discussion
├── report/
│   └── Legal-Technical-Report.docx    # Sub-Problem 5: 4-6 page report
├── scripts/
│   ├── generate_hashes.py
│   ├── search_artifacts.py
│   └── crack_password.py
└── .github/workflows/
    └── validate-structure.yml         # CI: validates repo structure + reruns scripts
```

## 2. Execution Guide

Requires Python 3.9+ and `pyzipper` (`pip install pyzipper`).

```bash
git clone <your-repo-url>
cd phantom-swipe
pip install pyzipper

# 1. Generate/verify SHA-256 hashes of all acquired evidence
python3 scripts/generate_hashes.py

# 2. Run the forensic string/metadata search over evidence files
python3 scripts/search_artifacts.py

# 3. Run the dictionary-attack simulation against the protected archive
python3 scripts/crack_password.py
```

Each script writes its output to the relevant folder (`hashes/`,
`artifacts/`, `crypto/`) so results are reproducible and match what's
already committed in the repo.

### Real-tool equivalents (documented in `crypto/cryptography_discussion.md`)
The Python simulation stands in for `John the Ripper` / `hashcat`, whose
equivalent commands are:
```bash
zip2john crypto/protected_batch.zip > protected_batch.hash
john --wordlist=crypto/wordlist.txt protected_batch.hash
# or
hashcat -m 13600 protected_batch.hash crypto/wordlist.txt
```

## 3. Tools Used

| Tool | Purpose |
|---|---|
| Python 3 (`hashlib`, `re`) | Hashing, string/pattern search |
| `pyzipper` | AES ZIP creation/decryption for the crypto simulation |
| Markdown | Taxonomy, chain-of-custody, and log documentation |
| GitHub Actions | CI validation of repo structure and script reproducibility |
| (Documented, not executed) John the Ripper / hashcat | Real-world password-cracking tool commands, referenced for equivalence |

## 4. Deliverables Checklist

- [x] Simulated media files (skimmer + phone) — `evidence/`
- [x] Extracted artefacts — `artifacts/search_log.txt`, `artifacts/evidence_log.md`
- [x] Password-protected folder + cracking simulation — `crypto/`
- [x] Legal-technical report (DOCX) — `report/Legal-Technical-Report.docx`
- [x] Cracking/analysis tools/scripts — `scripts/`
- [x] Tool usage screenshots — script-run screenshots included in `screenshots/`;
      **you still need to add** the GitHub Actions green-check and repo-tree
      screenshots after you push (see Section 5 below)
- [x] Chain of custody form — `chain_of_custody/chain_of_custody_form.md`
- [x] Hash values of collected artefacts — `hashes/hash_values.txt`
- [x] Execution guide, tools used, authorship declaration — this file
- [x] GitHub Action for validating repo structure — `.github/workflows/validate-structure.yml`

## 5. Screenshots

Screenshots of the three scripts running are already in `screenshots/`.
Two more can only be taken from your own GitHub account after you push:
1. The GitHub Actions run passing (green check) — Actions tab
2. The repo file tree on GitHub

Add those two to `screenshots/` and reference all five in the report's
appendix if your instructor wants them inline.

## 6. Authorship Declaration

I declare that the analysis, scripts, and report in this repository were
prepared by me for this assignment, using simulated/synthetic data only.
Where tools or techniques are referenced (e.g. John the Ripper, hashcat),
they are documented for methodological completeness but were not run
against any real device or real personal data.

**Name:** _[your name]_
**Student ID:** _[your ID]_
**Course/Section:** _[fill in]_
**Date:** _[fill in]_
