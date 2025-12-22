# Natas Level 11 → Level 12

## Objective
Retrieve the password by breaking weak cryptographic logic used to protect client-side data.

## Environment
- Web-based challenge (OverTheWire Natas)
- Access via web browser
- HTTP Basic Authentication

## Challenge Overview
The application uses a cookie to store user-related data.  
The data appears encrypted and is assumed to be secure.

However, the encryption mechanism is custom-made.

That is already a red flag.

## Approach
The source code reveals that the cookie is encrypted using XOR with a repeating key.  
Because XOR is reversible and the structure of the plaintext is predictable, the key can be recovered.

Once the key is known, the cookie can be decrypted, modified, and re-encrypted to gain access.

## Steps Taken
1. View the page source to understand how the cookie is generated.
2. Extract the encrypted cookie value.
3. Analyze the XOR operation and recover the encryption key.
4. Decrypt the cookie and modify the data to enable access.
5. Re-encrypt the cookie and send it back to the server.
6. Extract the password displayed.

## Tools Used
- Web Browser
- View Page Source
- Manual XOR analysis

## Result
The password for **Natas Level 12** was successfully retrieved by exploiting weak XOR-based encryption.
