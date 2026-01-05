# OverTheWire Bandit — Level 15

## Objective
Retrieve the password for the next level by submitting the current password to an SSL-encrypted network service running on localhost.

## Access
* **Host:** bandit.labs.overthewire.org
* **Port:** 2220
* **Username:** bandit15

## Method
The service on port **30001** requires the current password but operates over **SSL/TLS** encryption. Standard tools like Netcat cannot natively handle the encryption handshake.

By using **OpenSSL** (`openssl s_client -connect localhost:30001`) to establish a secure connection and submitting the current password (`kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx`), the service accepts the input and returns the password for the next level.

## Result
Password for the next level retrieved successfully.

`EReVavePLFHtFlFsjn3hyzMlvSuSAcRD`

## Key Takeaway
* Network services may require encrypted communication channels (SSL/TLS).
* The `openssl s_client` command is a vital tool for debugging and interacting with SSL-enabled services when standard text-based tools fail.
