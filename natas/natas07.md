<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">

# OverTheWire Natas — Level 7

## Objective

Exploit a Local File Inclusion (LFI) vulnerability to read a password file stored outside the web root directory.

## Access

* URL: http://natas7.natas.labs.overthewire.org/
* Username: natas7
* Password: bmg8SvU1LizuWjx3y7xkNERkHxGre0GS

## Method

The website navigation uses a URL parameter `?page=` to load content (e.g., `index.php?page=home`). This structure suggests that the application is reading files based on this input. By manipulating the parameter to traverse directories (Directory Traversal), we can access system files. The source code hints that the password is located at `/etc/natas_webpass/natas8`. 

The payload `?page=/etc/natas_webpass/natas8` is appended to the URL.

## Result

Password for the next level obtained successfully.

xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q


## Key Takeaway

* Input parameters used for file paths must be strictly sanitized.
* Allowing direct user input to control file inclusion (LFI) allows attackers to read arbitrary files on the server.
</div>
