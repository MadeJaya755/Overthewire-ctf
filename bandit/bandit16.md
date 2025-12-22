# Bandit Level 16 → Level 17

## Objective
Retrieve the password for the next level by interacting with a service running on a non-standard port.

## Environment
- Remote Linux system (OverTheWire Bandit)
- SSH access
- Service running on localhost port 30002

## Challenge Overview
- Service berjalan di port **30002**.  
- Tidak ada file atau interface web.  
- Koneksi harus dilakukan via TCP, service menerima password dari level sebelumnya dan mengembalikan password berikutnya.

Mirip Level 15, tapi **non-SSL**, jadi cukup TCP polos.

## Approach
1. Read current password:
```bash
cat /etc/bandit_pass/bandit16
