# Bandit Level 17 → Level 18

## Objective
Retrieve the password for the next level by comparing two files and identifying the difference.

## Environment
- Remote Linux system (OverTheWire Bandit)
- SSH access
- Two text files provided in the home directory

## Challenge Overview
Terdapat dua file:
- `passwords.old`
- `passwords.new`

Keduanya hampir identik.  
Password untuk level berikutnya adalah **satu-satunya baris yang berbeda** di antara kedua file tersebut.

Kalau lu coba baca manual, buang waktu. Ini kerjaan `diff`.

## Approach
1. List file yang tersedia.
2. Bandingkan kedua file menggunakan `diff`.
3. Identifikasi baris yang berbeda.
4. Ambil password dari hasil perbandingan.

## Commands Used
```bash
ls
diff passwords.old passwords.new
