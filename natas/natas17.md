<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">

# OverTheWire Natas — Level 17

## Objective

Extract data using Time-Based Blind SQL Injection, as the server provides no visual feedback (output or errors) regarding the query result.

## Access

* URL: http://natas17.natas.labs.overthewire.org/
* Username: natas17
* Password: 6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ

## Method

This level is similar to Level 15, but the code has been patched to not print "User exists." We cannot see the result of our query. However, we can measure *how long* the database takes to respond.

We can inject a `SLEEP()` command. If our guess is correct, the database will pause before responding.
**Payload Logic:**
`natas18" AND IF(password LIKE BINARY "a%", SLEEP(5), 0) --`

If the response takes longer than 5 seconds, the first character is 'a'. If it returns immediately, the guess is wrong. A script is required to automate this timing analysis for each character.

## Result

Password for the next level obtained successfully.

tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr


## Key Takeaway

* Even with zero visual feedback, SQL injection is possible via side channels like response time.
* Suppressing errors does not fix the underlying vulnerability.
</div>
