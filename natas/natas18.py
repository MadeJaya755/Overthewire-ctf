# Natas Level 18 → Level 19

## Objective
Retrieve the password by exploiting weak session management based on predictable session IDs.

## Environment
- Web-based challenge (OverTheWire Natas)
- Access via web browser
- HTTP Basic Authentication
- Session-based authentication

## Challenge Overview
The application uses session IDs to identify authenticated users.  
However, session IDs are generated using a simple numeric range.

There is no randomness. No entropy. No protection.

## Approach
Since session IDs are predictable, they can be brute-forced.  
By iterating through possible session values and checking the server response, a valid authenticated session can be discovered.

Once an admin-level session is found, the password is revealed.

## Steps Taken
1. Open the Natas Level 18 webpage.
2. Observe the session cookie format.
3. Enumerate possible session ID values.
4. Send requests with different session IDs.
5. Identify the session with elevated privileges.
6. Extract the password.

## Tools Used
- Web Browser
- Manual session manipulation
- Brute-force enumeration

## Result
The password for **Natas Level 19** was successfully retrieved by abusing predictable session IDs.
