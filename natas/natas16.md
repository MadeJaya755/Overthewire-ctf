<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">


# OverTheWire Natas — Level 16

## Objective

Exploit a Blind Command Injection vulnerability using command substitution to extract the password character by character.

## Access

* URL: http://natas16.natas.labs.overthewire.org/
* Username: natas16
* Password: EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC

## Method

The application executes a `grep` search on a dictionary file based on user input. The code filters characters like `;`, `|`, and `&` to prevent standard command injection, but it does not filter dollar signs `$` or parentheses `()`.

This allows for **Command Substitution** using `$(command)`. The output of the injected command replaces the `$(...)` string before the outer `grep` executes.

We can inject a sub-command to search for the password.
**Logic:**
1. Inject: `$(grep ^a /etc/natas_webpass/natas17)`
2. **If the password starts with 'a':** The sub-command returns the password. The main `grep` searches for this password in `dictionary.txt`. Since passwords aren't dictionary words, the result is empty (No output).
3. **If the password does NOT start with 'a':** The sub-command returns nothing (empty string). The main `grep` searches for "" (nothing) in `dictionary.txt`, which matches every line (Large output).

By automating this check (Empty Response = Correct Character), we can brute-force the password.

## Result

Password for the next level obtained successfully.

6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ


## Key Takeaway

* Blacklisting characters is difficult to do completely.
* Command substitution (`$(...)` or backticks `` ` ``) allows execution even inside quoted strings in many shell environments.
</div>
