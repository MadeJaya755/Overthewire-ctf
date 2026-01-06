<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">

Markdown

# OverTheWire Natas — Level 18

## Objective

Bypass authentication by exploiting insecure session ID generation (Session Hijacking/Prediction).

## Access

* URL: http://natas18.natas.labs.overthewire.org/
* Username: natas18
* Password: tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr

## Method

The source code reveals that the application checks if a session is valid and if the `admin` flag is set to 1. However, the `createID` function relies on a simple incremental integer for the `PHPSESSID`. The maximum ID (`$maxid`) is 640.

This means an active admin session likely exists within the range of 1 to 640. We can perform a brute-force attack on the `PHPSESSID` cookie.
1.  Script a loop to send requests with `PHPSESSID=1`, `PHPSESSID=2`, etc.
2.  Check the response for the text "You are an admin."

## Result

Password for the next level obtained successfully.

p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw


## Key Takeaway

* Session IDs must be long, random, and unpredictable.
* Using sequential numbers for session identifiers allows attackers to easily hijack other users' sessions.
</div>
