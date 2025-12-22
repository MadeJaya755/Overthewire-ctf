# Leviathan Level 0 → Level 1

## Objective
Retrieve the password for the next level by performing basic file enumeration on the target system.

Level ini menguji hal paling dasar: **apakah bisa membaca lingkungan Linux dengan benar**.

---

## Environment
- Remote Linux system (OverTheWire Leviathan)
- SSH access
- User: `leviathan0`
- Standard user privileges
- Readable home directory

---

## Challenge Overview
Tidak ada binary.
Tidak ada SUID.
Tidak ada exploit.

Password **sudah tersedia di home directory**, disimpan dalam sebuah file tersembunyi.
Satu-satunya tantangan adalah **menemukannya**.

---

## Approach

### 1. Login via SSH
```bash
ssh leviathan0@leviathan.labs.overthewire.org -p 2223

2. Enumerate home directory
ls -la


Output akan menampilkan file tersembunyi:

.bookmarks.html


File ini readable oleh user saat ini.

3. Inspect file content
cat .bookmarks.html


Di dalam file HTML tersebut terdapat bookmark yang menyimpan credential secara plain text.

Password untuk user leviathan1 dapat langsung dibaca tanpa decoding atau dekripsi.

Result

Password untuk Leviathan Level 1 berhasil diperoleh dari file .bookmarks.html.


