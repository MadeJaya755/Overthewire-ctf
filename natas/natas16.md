# Natas Level 16 → Level 17

## Objective
Retrieve the password by exploiting command injection in a web parameter.

## Environment
- Web-based challenge (OverTheWire Natas)
- Access via web browser
- HTTP Basic Authentication

## Challenge Overview
The application allows users to submit input that is later used in server-side commands.  
Previous filtering attempts are present, but insufficient.

Direct execution of user input on the server is possible.

## Approach
The parameter is passed to a shell command without proper sanitization.  
By carefully crafting input, arbitrary commands can be executed.

This allows reading the password file on the server.

## Steps Taken
1. Open the Natas Level 16 webpage.
2. Analyze the input field and observe server response.
3. Inject a shell command to read the password file.
4. Submit the crafted input.
5. Capture the password from the server response.

## Tools Used
- Web Browser
- Manual command injection

## Result
The password for **Natas Level 17** was successfully retrieved via command injection.
