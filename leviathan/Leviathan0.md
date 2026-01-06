<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">


# OverTheWire Leviathan — Level 0

## Objective

Log in to the Leviathan server using SSH and locate the password for the next level hidden within the user's home directory.

## Access

* **Host:** leviathan.labs.overthewire.org
* **Port:** 2223
* **Username:** leviathan0
* **Password:** leviathan0

## Method

1.  **Establish Connection:** Connect to the server via SSH on port 2223.
    `ssh leviathan0@leviathan.labs.overthewire.org -p 2223`
2.  **Reconnaissance:** List all files in the home directory, including hidden files, using `ls -la`.
3.  **Identify Targets:** A hidden directory named `.backup` is observed.
4.  **Extraction:** Navigate into the directory (`cd .backup`) and list its contents. A file named `bookmarks.html` is found. Searching this file (using `grep` or `cat`) reveals the password hidden in the HTML text.
    `grep "password" bookmarks.html`

## Result

Password for the next level obtained successfully.

3QJ3TgzHDq


## Key Takeaway

* **Enumeration:** Always check for hidden files (starting with `.`) in Linux environments.
* **Grep:** Text search tools are essential for filtering large files to find sensitive keywords.
</div>
