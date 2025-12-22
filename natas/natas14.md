# Natas Level 14 → Level 15

## Objective
Retrieve the password by exploiting SQL Injection in a login form.

## Environment
- Web-based challenge (OverTheWire Natas)
- Access via web browser
- HTTP Basic Authentication
- Backend database authentication

## Challenge Overview
The application presents a username and password login form.  
Access is granted only if the supplied credentials match a database record.

User input is inserted directly into an SQL query.

## Approach
The login logic does not properly sanitize user input.  
By injecting SQL syntax into the username or password field, authentication checks can be bypassed.

This allows access without knowing valid credentials.

## Steps Taken
1. Open the Natas Level 14 webpage.
2. Submit normal credentials to observe behavior.
3. Inject SQL logic into an input field.
4. Force the authentication query to always evaluate as true.
5. Access the protected page and extract the password.

## Tools Used
- Web Browser
- Manual SQL injection

## Result
The password for **Natas Level 15** was successfully retrieved via SQL Injection.
