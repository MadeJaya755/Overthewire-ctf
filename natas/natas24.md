<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">


# OverTheWire Natas — Level 24

## Objective

Bypass a password comparison check by exploiting the behavior of the `strcmp()` function when handling arrays.

## Access

* URL: http://natas24.natas.labs.overthewire.org/
* Username: natas24
* Password: ckELKUWZUfpOv6uxS6M7lXBpBssJZ4Ws

## Method

The code uses `strcmp($passwd, $_REQUEST["passwd"])` to check the password. If `strcmp` returns `0`, the password is considered correct.
`strcmp` is designed to compare two strings. However, if one of the arguments is an **Array**, `strcmp` fails and returns `NULL` (or issues a warning depending on the PHP version).

In PHP logic, `NULL` behaves "falsy" in loose comparisons. The check `if(!strcmp(...))` evaluates `!NULL` as `True`.

**Payload:**
Pass the password parameter as an array array via the URL:
`?passwd[]=1`

## Result

Password for the next level obtained successfully.

cVXXwxMS3Y26n5UZU89QgpGmWCelaQlE


## Key Takeaway

* Input validation should check the data type (String, Array, Integer) before processing.
* Relying on functions that behave unpredictably with unexpected types creates authentication bypass vulnerabilities.
</div>
