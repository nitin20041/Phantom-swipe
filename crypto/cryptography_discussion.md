# Cryptography Component — Discussion
## Operation Phantom Swipe

## 1. What Was Done

One extracted archive (`crypto/protected_batch.zip`, referenced in the
email at `evidence/phone_device/email_extract.eml`) was found to be
AES-encrypted and password-protected. A **dictionary attack** was simulated
using `scripts/crack_password.py` against a 15-entry common-password
wordlist (`crypto/wordlist.txt`). The password `password1` was recovered in
6 attempts (0.0155s), revealing a second batch of cloned Track2 data.

The equivalent commands using standard forensic tools would be:

```bash
# John the Ripper
zip2john crypto/protected_batch.zip > protected_batch.hash
john --wordlist=crypto/wordlist.txt protected_batch.hash
john --show protected_batch.hash

# hashcat (mode 13600 = WinZip/PKZIP AES)
hashcat -m 13600 protected_batch.hash crypto/wordlist.txt
```

## 2. Why a Dictionary Attack Succeeded So Quickly

The password `password1` appears in virtually every breach-derived
wordlist (e.g. RockYou) because it satisfies naive complexity rules
(letters + a digit) while remaining highly predictable. This reflects a
common pattern in real cybercrime cases: operational-security discipline
around *technical* infrastructure (skimmer firmware, sideloaded apps) is
often far higher than discipline around *password hygiene*, because
password choice is a human/behavioural weak point rather than a technical
one.

## 3. Brute Force vs. Dictionary vs. Lawful Decryption Requests

| Approach | Description | When Used |
|---|---|---|
| **Dictionary attack** | Tries known/likely passwords (breach lists, common words) | Fast, effective against weak/reused passwords — used here |
| **Brute force** | Tries every possible character combination | Used when dictionary attacks fail; time cost grows exponentially with password length/complexity |
| **Lawful decryption request** | Formal legal order (e.g. under Sec. 69 IT Act, 2000 in India) compelling a suspect or service provider to provide a password or decryption key | Used when technical cracking is infeasible (strong password, hardware-backed encryption) |

## 4. Ethical and Legal Implications

- **Proportionality:** Brute-forcing is technically unauthorised access to
  a device unless conducted under a valid warrant/search authorisation.
  Even in a genuine investigation, cracking should be documented as part of
  the chain of custody and only performed on a **working copy**, never the
  sealed master evidence.
- **Self-incrimination tension:** Compelling a suspect to reveal a password
  (as opposed to a biometric) raises constitutional questions in several
  jurisdictions (analogous to protections against self-incrimination). India's
  IT Act Sec. 69 empowers government-authorised interception/decryption, but
  its use must be necessity- and proportionality-tested and is subject to
  the safeguards read into Sec. 69 by courts.
- **Chain of custody for cracked evidence:** Once decrypted, the *plaintext*
  content becomes new evidence and must itself be hashed and logged (see
  `hashes/hash_values.txt`) to preserve integrity for court production.
- **Cross-border complication:** If the archive had instead been secured
  with a strong, unique passphrase, lawful access may have required a
  Mutual Legal Assistance Treaty (MLAT) request if the device or cloud
  backup was hosted abroad — a major source of delay in transnational
  cybercrime cases (see Sec. 5 of the main report).

## 5. Reflection on Password Strength in Criminal Scenarios

This case illustrates a recurring investigative advantage: criminal actors
frequently reuse weak, memorable passwords across both legitimate and
illicit accounts for convenience, which is precisely what makes dictionary
attacks with breach-derived wordlists so effective in practice. This is a
double-edged finding for policy: it means poor password hygiene by
criminals aids investigators, but it also means legitimate users and
organisations remain vulnerable to the *same* attack technique, reinforcing
the case for mandatory strong-password policies and multi-factor
authentication as a general defensive control — not just a forensic
footnote.
