<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">


# OverTheWire Leviathan — Level 5

## Objective

Exploit a file handling vulnerability (Time-of-Check to Time-of-Use or unsafe file linking) to read a protected password file.

## Access

* **Host:** leviathan.labs.overthewire.org
* **Port:** 2223
* **Username:** leviathan5
* **Password:** szo7HDB88w

## Method

1.  **Analysis:** The binary `leviathan5` attempts to read a file located at `/tmp/file.log` and print its contents. If the file does not exist, it fails.
2.  **Vulnerability:** The program reads `/tmp/file.log` with the privileges of the file owner (leviathan6), but the user has write access to the `/tmp/` directory.
3.  **Exploitation:** Create a symbolic link at `/tmp/file.log` that points to the target password file.
    `ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log`
4.  **Execution:** Run the binary. It follows the symbolic link and reads the password file instead of a log file.
    `./leviathan5`

## Result

Password for the next level obtained successfully.

qEs5Io5yM8


## Key Takeaway

* **Symbolic Links:** Attackers can use symlinks to redirect a program's file operations to unintended targets.
* **Hardcoded Paths:** Relying on files in public directories like `/tmp` without strict validation is a critical security flaw.
</div>
