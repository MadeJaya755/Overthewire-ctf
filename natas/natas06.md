<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">

# OverTheWire Natas — Level 6

## Objective

Bypass a secret string check by locating the server-side include file containing the hardcoded secret.

## Access

* URL: http://natas6.natas.labs.overthewire.org/
* Username: natas6
* Password: 0RoJwHdSKWFTYR5WuiAewauSuNaBXned

## Method

The page requires a "secret" to be entered into a form. Clicking "View sourcecode" reveals the PHP logic, which includes a file named `includes/secret.inc` and compares user input against a `$secret` variable defined therein. Navigating directly to `/includes/secret.inc` and viewing its source reveals the hardcoded secret string. Submitting this string into the form authenticates the user.

## Result

Password for the next level obtained successfully.

bmg8SvU1LizuWjx3y7xkNERkHxGre0GS


## Key Takeaway

* Server-side include files should be protected from direct public access.
* Hardcoding sensitive secrets in files within the web root is a security risk.
</div>
