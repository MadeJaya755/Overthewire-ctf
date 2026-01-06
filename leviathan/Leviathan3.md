<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">


# OverTheWire Leviathan — Level 3

## Objective

Bypass a password check within a setuid executable by analyzing library calls to find the hardcoded verification string.

## Access

* **Host:** leviathan.labs.overthewire.org
* **Port:** 2223
* **Username:** leviathan3
* **Password:** WG1egElCvO

## Method

1.  **Analysis:** The home directory contains an executable named `level3`. Running it prompts the user to "Enter the password."
2.  **Dynamic Analysis:** Use `ltrace` to intercept library calls made by the program.
    `ltrace ./level3`
3.  **Observation:** The trace output reveals a `strcmp` function comparing the user's input (e.g., "test") against a hardcoded string: `snlprintf`.
    ```
    strcmp("test", "snlprintf") = 1
    ```
4.  **Exploitation:** Execute the binary again and enter `snlprintf` when prompted. This grants a shell with elevated privileges.
5.  **Retrieval:** Read the password file for the next level.
    `cat /etc/leviathan_pass/leviathan4`

## Result

Password for the next level obtained successfully.

0dyxT7F4QD


## Key Takeaway

* **ltrace/strace:** These tools are invaluable for uncovering hardcoded secrets or logic flaws in binary executables by monitoring system and library interactions.
</div>
