<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">


## 📖 Overview

This repository documents the solutions for the **Krypton** wargame hosted by [OverTheWire](https://overthewire.org/wargames/krypton/). 

Unlike other wargames that focus on web or system exploitation, Krypton is dedicated to the study of **Cryptography** and **Cryptanalysis**. The challenges require analyzing encrypted data (ciphertexts) to recover the plaintext passwords, moving from classical ciphers to modern encryption concepts.

## 🎯 Objective

The objective of this documentation is to demonstrate the methodology used to break various encryption schemes. It serves as a reference for:
* **Classical Ciphers:** Understanding substitution and transposition ciphers (ROT13, Caesar, Vigenère).
* **Frequency Analysis:** Using statistical language properties to break monoalphabetic substitution ciphers.
* **Key Analysis:** Determining key lengths and recovering keys from polyalphabetic ciphers.
* **Modern Crypto:** Working with stream ciphers and hashing.

## 📂 Repository Structure

The solutions are categorized by the type of cryptographic challenge encountered:

| Level | concept |
| :--- | :--- |
| **Level 0** | Encoding vs. Encryption (Base64). |
| **Level 1** | Rotation Ciphers (ROT13). |
| **Level 2** | Caesar Ciphers (Shift Ciphers). |
| **Level 3** | Frequency Analysis (Monoalphabetic Substitution). |
| **Level 4** | Vigenère Cipher (Key Length & Frequency Analysis). |
| **Level 5** | Vigenère Cipher (Key Recovery). |
| **Level 6** | Stream Ciphers / Randomness Analysis. |

## 🛠️ Tools Used

The following tools and techniques were utilized to solve these challenges:
* **Unix Text Utilities:** `tr`, `grep`, `wc`, `sort`, `uniq` for statistical analysis.
* **Python:** For scripting custom decoders and frequency analysis tools.
* **Online Solvers:** Tools like CyberChef (for verification).
* **Cryptanalysis:** Manual analysis of letter frequency distributions.

## ⚠️ Disclaimer

**Educational Purposes Only**

This repository contains solutions and scripts for educational cryptography challenges. The techniques demonstrated here are intended to help understand the weaknesses in historical and weak encryption algorithms.

## 🔗 References

* [OverTheWire Krypton](https://overthewire.org/wargames/krypton/)
* [Practical Cryptography](http://practicalcryptography.com/)
* [Frequency Analysis (English Letter Frequency)](https://en.wikipedia.org/wiki/Letter_frequency)

---
*Created for Educational Documentation*
</div>
