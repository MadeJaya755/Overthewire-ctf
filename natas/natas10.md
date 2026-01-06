<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">

Markdown

# OverTheWire Natas — Level 10

## Objective

Bypass a character filter (blacklist) to exploit a command injection vulnerability and read a protected file.

## Access

* URL: http://natas10.natas.labs.overthewire.org/
* Username: natas10
* Password: UJdqkK1pTu6VLt9UHWAgRZz6sVUZ3lEk

## Method

This level is similar to the previous one, but the source code now checks for and forbids specific command separators (`;`, `|`, `&`) to prevent command chaining. However, the input is still passed to the `grep` command: `grep -i $key dictionary.txt`.

Instead of chaining a new command, we can exploit `grep`'s ability to search through multiple files. By providing a regex pattern that matches everything (like `.*`) and appending the target file path, `grep` will output the content of the password file.

**Payload:**
`.* /etc/natas_webpass/natas11`

## Result

Password for the next level obtained successfully.

yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB


## Key Takeaway

* Blacklisting specific characters is often insufficient for security.
* Injections can occur via arguments to the executing program (argument injection) even without shell command separators.
</div>
