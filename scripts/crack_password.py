#!/usr/bin/env python3
"""
crack_password.py
Simulates a DICTIONARY ATTACK against a password-protected evidence archive
(Assignment Sub-Problem 4).

This is a pure-Python demonstration equivalent to what a tool like
`John the Ripper` (with `zip2john` + a wordlist) or `hashcat` (mode 13600 for
PKZIP/WinZip AES) would do — attempt to open the archive using each
candidate password from a wordlist until one succeeds.

Real-tool equivalent commands (documented, not required to run this script):
    zip2john crypto/protected_batch.zip > protected_batch.hash
    john --wordlist=crypto/wordlist.txt protected_batch.hash

    # or with hashcat:
    hashcat -m 13600 protected_batch.hash crypto/wordlist.txt

Usage:
    python3 scripts/crack_password.py
Writes a log to crypto/cracking_log.txt
"""

import time
from pathlib import Path

import pyzipper

ROOT = Path(__file__).resolve().parent.parent
ARCHIVE = ROOT / "crypto" / "protected_batch.zip"
WORDLIST = ROOT / "crypto" / "wordlist.txt"
LOG_FILE = ROOT / "crypto" / "cracking_log.txt"


def try_password(pwd: str) -> bool:
    try:
        with pyzipper.AESZipFile(ARCHIVE) as zf:
            zf.setpassword(pwd.encode())
            zf.testzip()
        return True
    except (RuntimeError, Exception):
        return False


def main():
    lines = [
        "# Password Cracking Simulation Log — Operation Phantom Swipe",
        f"# Target archive: {ARCHIVE.relative_to(ROOT)}",
        f"# Method: Dictionary attack using {WORDLIST.relative_to(ROOT)}",
        "",
    ]
    candidates = WORDLIST.read_text().splitlines()
    start = time.time()
    found = None
    attempts = 0
    for pwd in candidates:
        attempts += 1
        ok = try_password(pwd)
        lines.append(f"Attempt {attempts}: '{pwd}' -> {'SUCCESS' if ok else 'failed'}")
        if ok:
            found = pwd
            break
    elapsed = time.time() - start

    lines.append("")
    if found:
        lines.append(f"RESULT: Password recovered = '{found}' after {attempts} attempts in {elapsed:.4f}s")
    else:
        lines.append(f"RESULT: Password NOT found in wordlist after {attempts} attempts")

    LOG_FILE.write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
