<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">


# OverTheWire Natas — Level 25

## Objective

Chain a Directory Traversal vulnerability with Log Poisoning (LFI to RCE) to execute code and retrieve the password.

## Access

* URL: http://natas25.natas.labs.overthewire.org/
* Username: natas25
* Password: cVXXwxMS3Y26n5UZU89QgpGmWCelaQlE

## Method

The application includes files based on the `lang` parameter but attempts to sanitize input by replacing `../` with an empty string. This sanitization is not recursive, so `....//` becomes `../`.

Additionally, the application logs the visitor's `User-Agent` string into a log file located at `/var/www/natas/natas25/logs/natas25_<PHPSESSID>.log`.

**Attack Chain:**
1.  **Log Poisoning:** Modify the browser's User-Agent header to inject PHP code:
    `<?php echo file_get_contents('/etc/natas_webpass/natas26'); ?>`
2.  **Trigger Log:** Refresh the page to ensure the malicious User-Agent is written to the log file.
3.  **Local File Inclusion (LFI):** Use the directory traversal bypass to include the log file via the `lang` parameter. The path requires stepping back out of the language directory to reach the logs.
    URL Payload:
    `?lang=....//logs/natas25_<YOUR_SESSION_ID>.log`

The server includes the log file, executes the PHP code stored in the User-Agent entry, and prints the password.

## Result

Password for the next level obtained successfully.

u3RRffXjysjgwFU6b9xa23i6prmUsYne


## Key Takeaway

* Blacklists (removing `../`) are rarely effective; recursive filtering or whitelisting is required.
* Logs are just files; if an attacker can control content written to logs (like User-Agents) and include that file, they can achieve Remote Code Execution (RCE).
</div>
