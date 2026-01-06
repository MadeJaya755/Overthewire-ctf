<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">


# OverTheWire Leviathan — Level 4

## Objective

Decode obscured data output by a hidden binary to retrieve the password.

## Access

* **Host:** leviathan.labs.overthewire.org
* **Port:** 2223
* **Username:** leviathan4
* **Password:** 0dyxT7F4QD

## Method

1.  **Enumeration:** A standard listing (`ls`) shows nothing interesting. However, checking for hidden directories (`ls -la`) reveals a folder named `.trash`.
2.  **Analysis:** Inside `.trash`, there is a binary named `bin`. Executing it outputs a sequence of binary digits (0s and 1s).
    ```
    01110100 01101001 01110100 01101001 01110100 01101000 01101111 01100010
    ```
3.  **Decoding:** The output corresponds to 8-bit ASCII characters. Converting the binary sequence to text yields the string `titithob`.
4.  **Exploitation:** Use the decoded string `titithob` as the password for the next level's credentials.
    `cat /etc/leviathan_pass/leviathan5` (This command is protected, so we likely use the decoded password to log in directly or use it as an argument if prompted).
    *Correction:* The decoded string *is* the password for `leviathan5`.

## Result

Password for the next level obtained successfully.

szo7HDB88w


## Key Takeaway

* **Data Encoding:** Sensitive information is often obfuscated using different encodings (Binary, Hex, Base64).
* **Hidden Directories:** Critical assets are frequently hidden in directories starting with a dot (`.`).
</div>
