# Cybercrime Classification & Legal Mapping
## Operation Phantom Swipe — Cross-Border ATM & Credit Card Fraud Ring

## 1. Scenario Summary

The case involves a suspected organised group operating a **cross-border ATM
skimming and online credit-card fraud ring**. Two devices were seized during
the simulated raid:

1. A physical **ATM skimmer** (card-reader overlay + micro-camera unit)
2. A **smartphone** containing fraudulent payment apps, cloned card data,
   and communication logs with suspected co-conspirators abroad

## 2. Cybercrime Taxonomy

| # | Crime Observed | Category | Description |
|---|---|---|---|
| 1 | ATM Skimming | Hardware-based financial fraud | Covert device fitted to an ATM card slot to copy magnetic-stripe data, paired with a pinhole camera or thermal overlay to capture PINs |
| 2 | Credit/Debit Card Cloning | Identity/financial fraud | Skimmed track data written to a blank magnetic-stripe card to create a counterfeit card |
| 3 | Online Card-Not-Present (CNP) Fraud | Cyber-enabled financial fraud | Use of stolen card numbers, CVV, and expiry data for unauthorised e-commerce transactions |
| 4 | Unauthorised Access to Computer/Payment Systems | Cyber-dependent crime | Use of fraudulent mobile apps to access or simulate payment gateway sessions |
| 5 | Cross-Border Data Transfer of Stolen Financial Data | Transnational cybercrime | Card data and proceeds moved across jurisdictions, complicating attribution and evidence-sharing |
| 6 | Criminal Conspiracy | Ancillary offence | Coordination between skimming operatives, cloning technicians, and online fraud actors |

## 3. Mapping to Indian Law

### Information Technology Act, 2000 (as amended)

| Section | Offence | Relevance to Case |
|---|---|---|
| **Sec. 43** | Unauthorised access/damage to computer systems, data theft | Covers unauthorised extraction of card data via skimmer firmware and phone apps |
| **Sec. 66** | Computer-related offences (dishonestly/fraudulently doing acts under Sec. 43) | Applies to fraudulent use of skimmed data |
| **Sec. 66C** | Identity theft (fraudulent use of electronic signature, password, or unique identification feature) | Directly applicable — card numbers/PINs are a "unique identification feature" |
| **Sec. 66D** | Cheating by personation using computer resource | Applies to online CNP fraud using cloned card identities |
| **Sec. 43A / 72A** | Data protection / disclosure of information in breach of contract | Relevant if a payment processor's data was mishandled |

### Indian Penal Code, 1860 (now referenced alongside Bharatiya Nyaya Sanhita, 2023)

| Section | Offence | Relevance to Case |
|---|---|---|
| **Sec. 379** | Theft | Physical theft of card data via skimmer |
| **Sec. 420** | Cheating and dishonestly inducing delivery of property | Core offence for fraudulent transactions |
| **Sec. 465 / 468 / 471** | Forgery, forgery for cheating, using forged document as genuine | Cloned card = forged "document"/electronic record |
| **Sec. 120B** | Criminal conspiracy | Multiple actors (skimmer planter, cloner, online fraudster) acting in concert |
| **Sec. 34** | Common intention | Joint liability for coordinated acts |

### International Framework

| Instrument | Relevance |
|---|---|
| **Budapest Convention on Cybercrime (2001)** | Art. 2 (illegal access), Art. 8 (computer-related fraud), Art. 25 (mutual legal assistance) — relevant since the ring is cross-border; India is not a signatory but the Convention is the reference framework for MLAT (Mutual Legal Assistance Treaty) cooperation |
| **UN Convention against Transnational Organized Crime (2000)** | Applicable given the organised, multi-jurisdiction nature of the ring |
| **PCI-DSS (industry standard, not law)** | Relevant to how the breached payment data should have been protected upstream |

## 4. Taxonomy Justification

The classification separates **acquisition** (skimming — a hardware/physical
crime under Sec. 379 IPC and Sec. 66C IT Act), **fabrication** (cloning —
forgery under Sec. 465/468 IPC), and **monetisation** (CNP fraud — cheating
under Sec. 420 IPC and Sec. 66D IT Act). This acquisition→fabrication→
monetisation chain is the standard model used in financial cybercrime
investigations because each stage typically involves a different actor and
different digital evidence, which is why the investigation must treat the
skimmer and the phone as two separate but linked evidence sources.
