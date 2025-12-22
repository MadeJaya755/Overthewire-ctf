# Natas Level 15 → Level 16

## Objective
Retrieve the password by exploiting blind SQL injection through conditional responses.

## Environment
- Web-based challenge (OverTheWire Natas)
- Access via web browser
- HTTP Basic Authentication
- Backend database

## Challenge Overview
The application checks whether a submitted username exists in the database.  
It does not display query results directly—only a boolean-style response.

No error messages. No output. Just yes or no.

This is a **blind SQL injection** scenario.

## Approach
Although the query output is not visible, conditional SQL statements can still be evaluated.  
By injecting logical conditions and observing the application's response, the password can be extracted character by character.

This is slow, methodical, and unavoidable.

## Steps Taken
1. Open the Natas Level 15 webpage.
2. Submit a normal username to observe the response.
3. Inject conditional SQL statements to test character values.
4. Use iterative queries to enumerate the password one character at a time.
5. Reconstruct the full password.

## Tools Used
- Web Browser
- Manual SQL injection
- Logical inference

## Result
The password for **Natas Level 16** was successfully extracted using blind SQL injection.
