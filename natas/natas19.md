# Natas Level 19 → Level 20

## Objective
Retrieve the password by exploiting weak session handling combined with predictable encoding.

## Environment
- Web-based challenge (OverTheWire Natas)
- Access via web browser
- HTTP Basic Authentication
- Session-based authentication

## Challenge Overview
The application uses session cookies to track authenticated users.  
Unlike the previous level, the session ID is encoded instead of plain numeric.

However, the encoding scheme is trivial.

## Approach
The session cookie is decoded to reveal its internal structure.  
It turns out the value contains the username and session ID encoded in a reversible format.

By forging a session cookie that impersonates an admin user, access can be escalated.

## Steps Taken
1. Open the Natas Level 19 webpage.
2. Inspect the session cookie.
3. Decode the cookie value to understand its structure.
4. Modify the value to impersonate an admin session.
5. Re-encode the cookie.
6. Send the forged cookie and extract the password.

## Tools Used
- Web Browser
- Cookie manipulation
- Manual encoding/decoding

## Result
The password for **Natas Level 20** was successfully retrieved by forging a valid admin session cookie.
