<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">

## 📖 Overview

This repository serves as a comprehensive documentation and solution guide for the **Natas** wargame hosted by [OverTheWire](https://overthewire.org/wargames/natas/). 

Natas focuses on server-side web security. The challenges cover a wide spectrum of vulnerabilities commonly found in web applications, ranging from basic configuration errors to complex code execution exploits.

## 🎯 Objective

The primary goal of this repository is to document the learning process and methodology used to solve each level. It is intended to serve as a reference for:
* **Web Vulnerability Analysis:** Understanding how vulnerabilities occur in PHP code.
* **Exploitation Techniques:** Demonstrating how to leverage vulnerabilities to retrieve sensitive data.
* **Remediation:** recognizing insecure coding practices.

## 📂 Repository Structure

The solutions are organized by level. Each entry includes the objective, the vulnerability analysis, the exploitation method, and the retrieved flag.

| Level Range | Key Concepts Covered |
| :--- | :--- |
| **Level 0 – 5** | Source code inspection, HTTP headers, Cookies, Access Control. |
| **Level 6 – 10** | Server-side Includes, Directory Traversal, Command Injection. |
| **Level 11 – 15** | XOR Encryption, File Uploads, SQL Injection (Basic). |
| **Level 16 – 20** | Blind SQL Injection (Boolean & Time-based), Session Hijacking. |
| **Level 21 – 26** | Session Manipulation, Logic Flaws, Insecure Deserialization. |

## 🛠️ Tools Used

The following tools and languages were utilized to solve these challenges:
* **Burp Suite Community:** For intercepting and modifying HTTP requests.
* **Python:** For automating Blind SQL Injection and brute-force attacks.
* **cURL:** For command-line HTTP interaction.
* **Browser Developer Tools:** For client-side inspection and cookie management.
* **PHP:** For generating local payloads (serialization/encryption).

## ⚠️ Disclaimer

**Educational Purposes Only**

This repository contains write-ups and exploits for educational web security challenges. These techniques should only be used in authorized environments (like CTFs or systems you own). Unauthorized access to computer systems is illegal. The author is not responsible for any misuse of the information contained herein.

## 🔗 References

* [OverTheWire Natas Wargame](https://overthewire.org/wargames/natas/)
* [OWASP Top 10](https://owasp.org/www-project-top-ten/)
* [PHP Documentation](https://www.php.net/docs.php)

---
*Created by [Made Jaya Setiawan]*
</div>
