<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">

Markdown

# OverTheWire Natas — Level 4

## Objective

Bypass an access control mechanism that restricts access based on the visitor's origin URL.

## Access

* URL: http://natas4.natas.labs.overthewire.org/
* Username: natas4
* Password: QryZXc2e0zahULdHrtHxzyYkj59kUxLQ

## Method

The page displays an error stating that authorized users must visit from `http://natas5.natas.labs.overthewire.org/`. This indicates the server is checking the HTTP `Referer` header. To bypass this, the HTTP request was intercepted and the `Referer` header was manually modified to match the required URL.

## Result

Password for the next level obtained successfully.

0n35PkggAPm2zbEpOU802c0x0Msn1ToK


## Key Takeaway

* HTTP headers, including the `Referer` header, are controlled by the client.
* Relying on headers for access control is insecure as they can be easily spoofed by an attacker.
</div>
