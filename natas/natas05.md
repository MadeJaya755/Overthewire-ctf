<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">

Markdown

# OverTheWire Natas — Level 5

## Objective

Gain access to the protected page by manipulating authentication status stored in client-side cookies.

## Access

* URL: http://natas5.natas.labs.overthewire.org/
* Username: natas5
* Password: 0n35PkggAPm2zbEpOU802c0x0Msn1ToK

## Method

The page denies access with the message "You are not logged in." Inspecting the HTTP cookies using browser developer tools reveals a cookie named `loggedin` with a value of `0`. Changing this value to `1` and reloading the page bypasses the check.

## Result

Password for the next level obtained successfully.

0RoJwHdSKWFTYR5WuiAewauSuNaBXned


## Key Takeaway

* Cookies are stored on the client side and can be modified by the user.
* Authentication states should never rely solely on simple, unverified cookie values.
</div>
