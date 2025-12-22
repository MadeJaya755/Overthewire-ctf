# OverTheWire Leviathan Write-up

## Leviathan Level 6 → Level 7 (Final)

## Objective
Retrieve the password for the final level by exploiting a SUID binary through controlled brute force of a numeric PIN.

Level terakhir ini menguji:
- Pemahaman SUID binary
- Kesabaran dan automasi sederhana
- Realistisnya brute force dalam ruang pencarian kecil

Ini bukan soal pinter.  
Ini soal **nggak males dan tahu kapan brute force itu masuk akal**.

---

## Environment
- Remote Linux system (OverTheWire Leviathan)
- SSH access
- User: `leviathan6`
- SUID executable binary
- No source code provided
- Standard Linux utilities available (`bash`, `seq`, `grep`)

---

## Challenge Overview
Di home directory user `leviathan6` terdapat sebuah binary bernama:

```text
leviathan6
