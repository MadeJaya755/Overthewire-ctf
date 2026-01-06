<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">


# OverTheWire Leviathan — Level 2

## Objective

Exploit a command injection vulnerability caused by improper handling of filenames with spaces in a `system()` call.

## Access

* **Host:** leviathan.labs.overthewire.org
* **Port:** 2223
* **Username:** leviathan2
* **Password:** NsN1HwFoyN

## Method

1.  **Analysis:** The executable `printfile` accepts a filename as an argument and displays its content.
    `./printfile /etc/leviathan_pass/leviathan3` fails because the current user lacks read permissions.
2.  **Vulnerability Detection:** Using `ltrace ./printfile test`, we observe:
    * `access("test", 4)`: Checks if the user has read permissions for the file.
    * `system("/bin/cat test")`: Uses `cat` to print the file.
    * **Flaw:** The filename passed to `system()` is not quoted. If the filename contains a space, `cat` interprets it as two separate files.
3.  **Exploitation:**
    * Create a temporary directory: `mktemp -d` and `cd` into it.
    * Create a filename with a space: `touch "foo bar"`.
    * Create a symbolic link named `foo` pointing to the target password file:
        `ln -s /etc/leviathan_pass/leviathan3 foo`
    * Create a dummy file named `bar`: `touch bar`.
4.  **Execution:** Run the vulnerable binary against the file with the space.
    `~/printfile "foo bar"`
    * The `access()` check passes because we own "foo bar".
    * The `system()` call executes: `/bin/cat foo bar`.
    * This cats `foo` (the symlink to the password) and `bar`.

## Result

Password for the next level obtained successfully.

f0n8h2iWLP


## Key Takeaway

* **Command Injection:** Passing unsanitized user input (including filenames) to `system()` or `exec()` is dangerous.
* **Input Sanitization:** Filenames containing spaces or shell metacharacters can alter the intended command logic if not properly escaped or quoted.
</div>
