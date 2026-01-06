<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">


# OverTheWire Natas — Level 19

## Objective

Bypass authentication by reversing a weak custom session ID generation scheme.

## Access

* URL: http://natas19.natas.labs.overthewire.org/
* Username: natas19
* Password: p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw

## Method

Similar to the previous level, this page uses a custom session ID. However, the IDs are not simple integers. Observing the cookies set by the server (e.g., `3238312d6e617461733139`), we can decode them from Hexadecimal to ASCII.
`3238312d6e617461733139` decodes to `281-natas19`.

The format is `{id}-natas19` encoded in Hex. To find an admin session:
1.  Generate payloads: `1-natas19`, `2-natas19`, etc.
2.  Convert them to Hexadecimal.
3.  Brute-force the `PHPSESSID` cookie with these values until the admin session is found.

## Result

Password for the next level obtained successfully.

BPhv63cKE1lkQl04cE5CuFTzXe15NfiH


## Key Takeaway

* Obscurity (encoding) is not security.
* Custom session handlers often introduce weaknesses compared to standard, framework-provided session management.
</div>
