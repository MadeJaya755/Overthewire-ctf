# Bandit Level 15 → Level 16

## Objective
Retrieve the password for the next level by connecting to a secure SSL/TLS-enabled service.

## Environment
- Remote Linux system (OverTheWire Bandit)
- SSH access
- SSL/TLS service on localhost port 30001

## Challenge Overview
Mirip level sebelumnya, tapi sekarang:
- Service berjalan di port **30001**
- Koneksi **wajib SSL/TLS**
- Netcat biasa akan gagal

Kalau masih maksa `nc`, berarti belum ngerti bedanya TCP polos vs encrypted channel.

## Approach
1. Read current password from `/etc/bandit_pass/bandit15`.
2. Connect to the SSL service using `openssl s_client`.
3. Send the password through the encrypted connection.
4. Read the response containing the next password.

## Commands Used
```bash
cat /etc/bandit_pass/bandit15
