<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">

Markdown

# OverTheWire Natas — Level 8

## Objective

Reverse engineer an encoded secret string found in the source code to bypass a security check.

## Access

* URL: http://natas8.natas.labs.overthewire.org/
* Username: natas8
* Password: xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q

## Method

The page requires a secret passphrase. The "View sourcecode" link reveals the PHP logic used to encode the secret: `bin2hex(strrev(base64_encode($secret)))`. The encoded string is provided in the variable `$encodedSecret` (`3d3d516343746d4d6d6c315669563362`).

To retrieve the original secret, the encoding operations must be reversed in the specific order:
1. `hex2bin`: Convert hexadecimal back to binary/string (`==QcCtmMml1ViV3b`).
2. `strrev`: Reverse the string (`b3ViV1lmMmCtCcQ==`).
3. `base64_decode`: Decode the Base64 string.

The resulting secret is `oubWYf2kBq`. Submitting this value grants access to the credentials.

## Result

Password for the next level obtained successfully.

ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t


## Key Takeaway

* Encoding is not encryption; if the algorithm is known, it can be reversed.
* Security mechanisms relying on obscure encoding methods are easily bypassed by analyzing the source code.
</div>
