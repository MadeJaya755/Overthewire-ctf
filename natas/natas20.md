<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">

Markdown

# OverTheWire Natas — Level 20

## Objective

Exploit a Session Injection vulnerability caused by improper handling of newline characters in session storage.

## Access

* URL: http://natas20.natas.labs.overthewire.org/
* Username: natas20
* Password: BPhv63cKE1lkQl04cE5CuFTzXe15NfiH

## Method

The source code shows that the application manages sessions by reading and writing to a text file. It parses the file line-by-line, splitting keys and values by spaces.
Function: `write($key, $value)` saves data as `$key $value\n`.

We can inject a newline character (`\n` or `%0a`) into the input field to create a new entry in the session file.
**Payload:**
In the "name" field, enter:
`guinea%0aadmin 1`

This writes:
name guinea admin 1

When the page reloads and reads the session, it interprets the second line as `admin=1`, granting access.

## Result

Password for the next level obtained successfully.

d8rwGBl0Xslg3b76uh3fEbSlnOUBlozz


## Key Takeaway

* When writing user input to files or logs, delimiter characters (like newlines) must be sanitized.
* This is similar to HTTP Header Injection or Log Injection attacks.
</div>
