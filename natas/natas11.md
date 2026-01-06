<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">


# OverTheWire Natas — Level 11

## Objective

Exploit weak cryptography (XOR encryption) to manipulate the contents of a protected cookie and escalate privileges.

## Access

* URL: http://natas11.natas.labs.overthewire.org/
* Username: natas11
* Password: yZdkjAYZRd3R7tq7T5kXMjMJlOIkzDeB

## Method

The application stores user settings (background color and a "showpassword" flag) in a cookie named `data`. The source code reveals that this data is a JSON object that is XOR encrypted and then Base64 encoded.

Because the plaintext structure is known (default values are visible in the source), a Known Plaintext Attack can be performed to recover the encryption key.

1.  **Recover the Key:**
    * Ciphertext (from cookie): `ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=`
    * Known Plaintext: `json_encode(array("showpassword"=>"no", "bgcolor"=>"#ffffff"))`
    * Operation: `Key = Plaintext ^ Ciphertext`
    * Resulting Key: `qw8J` (repeating).

2.  **Forge the Payload:**
    * New Plaintext: `json_encode(array("showpassword"=>"yes", "bgcolor"=>"#ffffff"))`
    * Encrypt the new plaintext using the recovered key `qw8J`.
    * Base64 encode the result.

3.  **Inject Cookie:**
    Replace the value of the `data` cookie in the browser with the forged string and reload the page.

## Result

Password for the next level obtained successfully.

trbs5pCjCrkuSknBBKHhaBxq6Wm1j3LC


## Key Takeaway

* XOR encryption is symmetric; if an attacker knows the plaintext and the ciphertext, they can derive the key.
* Never use custom, weak encryption schemes for sensitive data.
* Client-side data storage (cookies) should not be trusted for authorization states.
</div>
