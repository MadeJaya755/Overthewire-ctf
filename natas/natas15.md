<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">


# OverTheWire Natas — Level 15

## Objective

Extract data from the database using a Boolean-based Blind SQL Injection vulnerability, where the application returns no data but indicates whether a query is true or false.

## Access

* URL: http://natas15.natas.labs.overthewire.org/
* Username: natas15
* Password: hPkjKYviLQctEW33QmuXL6eDVfMW4sGo

## Method

The application checks if a username exists. The source code uses the query:
`SELECT * from users where username="<input>"`

While the query is vulnerable to injection, the application does not print the result (e.g., the password). It only says "This user exists" or "This user doesn't exist."

To exploit this, we use **Blind SQL Injection**. We can ask the database true/false questions to guess the password character by character. We inject a query to check if the password for user `natas16` starts with a specific character.

**Payload Concept:**
`natas16" AND password LIKE BINARY "a%`

If the response is "This user exists," the first letter is 'a'. If not, we try 'b', and so on. This process requires a script (e.g., Python) to automate the brute-forcing of all 32 characters.

## Result

Password for the next level obtained successfully.

EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC


## Key Takeaway

* Even if an application does not display database errors or data, it can still be vulnerable to Blind SQL Injection.
* The `LIKE BINARY` operator ensures case-sensitive matching, which is crucial for passwords.
</div>
