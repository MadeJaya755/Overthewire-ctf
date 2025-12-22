# OverTheWire Leviathan Write-up

## Leviathan Level 4 → Level 5

## Objective
Retrieve the password for the next level by discovering and decoding hidden data stored in a non-human-readable file.

Level ini tidak menguji exploit.
Tidak menguji SUID.
Tidak menguji binary.

Yang diuji di sini cuma satu:
**apakah lo bisa mengenali tipe data dan memperlakukannya dengan benar**.

---

## Environment
- Remote Linux system (OverTheWire Leviathan)
- SSH access
- User: `leviathan4`
- Standard user privileges
- Readable home directory
- Standard Linux utilities available

---

## Challenge Overview
Tidak ada binary executable di home directory.

Sebagai gantinya, terdapat sebuah directory tersembunyi yang berisi file aneh:
- Tidak bisa dibaca langsung
- Tidak bisa dipahami dengan `cat`
- Tapi **jelas bukan random**

Password level berikutnya disimpan di sana,  
hanya saja **tidak dalam format teks biasa**.

---


