# OverTheWire Bandit — Level 9

## Objective

Extract the password hidden within a file containing mostly non-printable characters.

## Access

* Host: bandit.labs.overthewire.org
* Port: 2220
* Username: bandit9

## Method

The target file includes many non-printable characters, making direct reading ineffective.

By extracting only human-readable strings and searching for meaningful output, the password can be identified efficiently.

## Result

Password for the next level retrieved successfully.

```
FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
```

## Key Takeaway

* Binary data often hides readable strings.
* Filtering readable content is essential when analyzing unknown files.
