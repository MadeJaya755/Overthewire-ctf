# Natas Level 7 → Level 8

## Objective
Retrieve the password by exploiting insecure direct object references in URL parameters.

## Environment
- Web-based challenge (OverTheWire Natas)
- Access via web browser
- HTTP Basic Authentication

## Challenge Overview
The application uses a URL parameter to load different pages.  
Links such as `?page=home` and `?page=about` are used for navigation.

The password is not directly visible on the main page.

## Approach
The page parameter is directly mapped to server-side files without proper validation.  
By changing the parameter value to point to a sensitive file, restricted content can be accessed.

This is a classic **Local File Inclusion (LFI)** vulnerability.

## Steps Taken
1. Open the Natas Level 7 webpage.
2. Observe the `page` parameter in the URL.
3. Modify the parameter to reference the password file.
4. Load the page with the manipulated parameter.
5. Extract the password displayed.

## Tools Used
- Web Browser
- Manual URL parameter manipulation

## Result
The password for **Natas Level 8** was successfully retrieved via local file inclusion.
