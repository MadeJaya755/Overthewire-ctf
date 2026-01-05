# OverTheWire Bandit — Level 10

## Objective

Retrieve the password stored in a file encoded using Base64.

## Access

* Host: bandit.labs.overthewire.org
* Port: 2220
* Username: bandit10

## Method

The file content is not plaintext but encoded.

By identifying the encoding format and decoding it correctly, the original password can be recovered.

## Result

Password for the next level retrieved successfully.

```
dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
```

## Key Takeaway

* Encoding is not encryption.
* Always check whether data is merely transformed rather than protected.
