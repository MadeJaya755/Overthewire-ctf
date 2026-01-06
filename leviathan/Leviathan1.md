<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">


# OverTheWire Leviathan — Level 1

## Objective

Reverse engineer a small binary executable to discover the hardcoded password required to unlock the credentials for the next level.

## Access

* **Host:** leviathan.labs.overthewire.org
* **Port:** 2223
* **Username:** leviathan1
* **Password:** 3QJ3TgzHDq

## Method

1.  **Analysis:** The home directory contains a setuid executable named `check`. Running it prompts for a password.
2.  **Dynamic Analysis (ltrace):** Use `ltrace` (Library Call Tracer) to inspect the program's interaction with standard libraries.
    `ltrace ./check`
3.  **Observation:** The trace reveals a `strcmp` (string comparison) function comparing the user input against the string `"sex"`.
    ```
    strcmp("test", "sex") = 1
    ```
4.  **Exploitation:** Run the binary again and enter `sex` as the password. This grants access to a shell with `leviathan2` privileges.
5.  **Retrieval:** Read the password file.
    `cat /etc/leviathan_pass/leviathan2`

## Result

Password for the next level obtained successfully.

NsN1HwFoyN


## Key Takeaway

* **Hardcoded Credentials:** Storing passwords directly in the source code allows attackers to easily extract them using tools like `strings` or `ltrace`.
* **ltrace:** A powerful tool for debugging and reverse engineering to see data passed to library functions.
</div>
