<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">


# OverTheWire Leviathan — Level 6

## Objective

Perform a brute-force attack on a 4-digit Personal Identification Number (PIN) to access a restricted shell.

## Access

* **Host:** leviathan.labs.overthewire.org
* **Port:** 2223
* **Username:** leviathan6
* **Password:** qEs5Io5yM8

## Method

1.  **Analysis:** The binary `leviathan6` prompts for a 4-digit PIN.
2.  **Strategy:** Since the keyspace is small (0000 to 9999), it is feasible to brute-force the PIN using a script.
3.  **Exploitation:** Use a simple bash loop to try all combinations.
    ```bash
    for i in {0000..9999}; do ./leviathan6 $i; done
    ```
4.  **Execution:** The loop runs rapidly. When the correct PIN (which varies, e.g., `7123`) is hit, the program executes a shell.
5.  **Retrieval:** Once the shell is spawned (indicated by the user prompt changing), read the password file.
    `cat /etc/leviathan_pass/leviathan7`

## Result

Password for the next level obtained successfully.

qEs5Io5yM8


## Key Takeaway

* **Brute Force:** Short numeric PINs provide weak security and can be exhausted in seconds by automated scripts.
* **Rate Limiting:** Authentication mechanisms must implement delays or lockouts to prevent rapid guessing attacks.
</div>
