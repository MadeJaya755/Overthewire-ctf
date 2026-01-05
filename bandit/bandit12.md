# OverTheWire Bandit — Level 12

## Objective

Extract the password hidden in a file that has been repeatedly compressed and encoded.

## Access

* Host: bandit.labs.overthewire.org
* Port: 2220
* Username: bandit12

## Method

The file contains data that has gone through multiple layers of compression and encoding.

By identifying each format step-by-step and reversing the process iteratively, the original plaintext containing the password can be recovered.

## Result

Password for the next level retrieved successfully.

```
FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn
```

## Key Takeaway

* Layered encoding and compression require systematic analysis.
* Rushing without identifying formats leads to mistakes.
