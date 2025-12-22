# OverTheWire Leviathan Write-up

## Leviathan Level 3 → Level 4

## Objective
Retrieve the password for the next level by analyzing a SUID binary and extracting hardcoded credentials embedded inside it.

Level ini fokus ke:
- Observasi perilaku binary
- Analisis string statis
- Memahami kesalahan desain program sederhana

Tidak ada exploit rumit.  
Yang diuji di sini adalah **ketelitian dan kebiasaan analisis dasar**.

---

## Environment
- Remote Linux system (OverTheWire Leviathan)
- SSH access
- User: `leviathan3`
- SUID executable binary
- No source code provided
- Standard Linux tools available (`strings`, `ls`, `cat`)

---

## Challenge Overview
Di home directory user `leviathan3` terdapat sebuah binary bernama:

```text
leviathan3
