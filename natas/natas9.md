# Natas Level 9 → Level 10

## Objective
Retrieve the password for the next level by exploiting command injection in user-supplied input.

## Environment
- Web-based challenge (OverTheWire Natas)
- Access via web browser
- HTTP Basic Authentication

## Challenge Overview
The application provides a search function that takes user input and executes it on the server.  
The input is intended to be used as a parameter for a system command.

Input validation is weak.

## Approach
User input is passed directly into a shell command without proper sanitization.  
By injecting additional shell operators, arbitrary commands can be executed.

This allows reading sensitive files on the server.

## Steps Taken
1. Open the Natas Level 9 webpage.
2. Submit a normal search query to observe behavior.
3. Inject a command separator into the input.
4. Execute a command to read the password file.
5. Capture the password from the output.

## Tools Used
- Web Browser
- Manual command injection

## Result
The password for **Natas Level 10** was successfully retrieved via command injection.
