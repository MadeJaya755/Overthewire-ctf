<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">

Markdown

# OverTheWire Natas — Level 9

## Objective

Exploit a command injection vulnerability in a search utility to execute arbitrary shell commands.

## Access

* URL: http://natas9.natas.labs.overthewire.org/
* Username: natas9
* Password: ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t

## Method

The application provides a search box that looks for words in a dictionary. Inspecting the source code reveals the following backend logic:

```php passthru("grep -i $key dictionary.txt");
The $key variable (user input) is passed directly into the passthru function without sanitization. This allows for Command Injection. We can use a semicolon (;) to terminate the grep command and append a new command to read the password file.

Payload: ; cat /etc/natas_webpass/natas10

Entering this into the search field executes grep, followed immediately by cat, revealing the password.

Result
Password for the next level obtained successfully.

t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu
Key Takeaway
Passing unsanitized user input directly to system execution functions like passthru, system, or exec creates critical command injection vulnerabilities.

Input should always be sanitized or parameterized.


</div>
