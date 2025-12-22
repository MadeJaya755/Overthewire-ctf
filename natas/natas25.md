# Natas Level 25 → Level 26

## Objective
Retrieve the password by exploiting local file inclusion through log poisoning.

## Environment
- Web-based challenge (OverTheWire Natas)
- Access via web browser
- HTTP Basic Authentication
- PHP backend
- Server-side logging enabled

## Challenge Overview
The application allows including files based on a user-controlled parameter.  
Direct inclusion of sensitive files is restricted.

However, server log files are writable and readable.

## Approach
User input is written into server log files without sanitization.  
By injecting executable code into the logs and then including the log file via the vulnerable parameter, server-side code execution is achieved.

This is a classic **log poisoning + LFI** chain.

## Steps Taken
1. Open the Natas Level 25 webpage.
2. Identify the file inclusion parameter.
3. Inject executable payload into server logs via HTTP headers.
4. Locate the log file path.
5. Include the poisoned log file through the vulnerable parameter.
6. Execute code and extract the password.

## Tools Used
- Web Browser
- Manual HTTP header manipulation
- Local File Inclusion

## Result
The password for **Natas Level 26** was successfully retrieved via log poisoning and local file inclusion.
