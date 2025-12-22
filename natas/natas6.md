# Natas Level 6 → Level 7

## Objective
Retrieve the password by exploiting insecure server-side file inclusion.

## Environment
- Web-based challenge (OverTheWire Natas)
- Access via web browser
- HTTP Basic Authentication

## Challenge Overview
The page presents a form that checks whether a submitted secret is correct.  
No password is visible, and input alone does not reveal useful information.

However, the application loads a server-side file that contains validation logic.

## Approach
The source code reveals that the secret is stored in a separate file included by the application.  
This file is accessible due to improper access control.

By directly requesting the included file, the secret value can be disclosed.

## Steps Taken
1. View the page source.
2. Identify the included server-side file.
3. Access the file directly via the browser.
4. Extract the secret value.
5. Submit the correct secret to reveal the password.

## Tools Used
- Web Browser
- View Page Source
- Manual URL access

## Result
The password for **Natas Level 7** was successfully obtained from an exposed server-side file.
