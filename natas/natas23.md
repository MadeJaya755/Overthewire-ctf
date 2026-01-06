<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">

# OverTheWire Natas — Level 23

## Objective

Bypass a password check by exploiting PHP's loose type comparison ("Type Juggling") behavior.

## Access

* URL: http://natas23.natas.labs.overthewire.org/
* Username: natas23
* Password: MeuqmfJ8DDKuTr5pcvzFKSwlxedZYEWd

## Method

The application checks user input against a request parameter `passwd`. The logic requires two conditions to be met simultaneously:
1.  The input must contain the string "iloveyou" (`strstr($passwd,"iloveyou")`).
2.  The input must be numerically greater than 10 (`$passwd > 10`).

In PHP, when a string is compared to a number, the interpreter parses the string from the beginning to find a numerical value.
* Input `iloveyou` converts to `0` (False).
* Input `10iloveyou` converts to `10` (False, as 10 is not > 10).
* Input `11iloveyou` converts to `11` (True, 11 > 10).

**Payload:**
`11iloveyou`

## Result

Password for the next level obtained successfully.

ckELKUWZUfpOv6uxS6M7lXBpBssJZ4Ws


## Key Takeaway

* PHP "Magic Comparisons" (loose typing) can lead to logic bypasses.
* Always use strict comparison operators (`===`) when validating security-critical input.
</div>
