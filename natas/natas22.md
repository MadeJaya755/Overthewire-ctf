# Natas Level 22 → Level 23

## Objective
Retrieve the password by bypassing client-side redirection logic.

## Environment
- Web-based challenge (OverTheWire Natas)
- Access via web browser
- HTTP Basic Authentication

## Challenge Overview
The application immediately redirects users away from the page that contains the password.  
The redirection is enforced using client-side logic.

The server still sends the sensitive content.

## Approach
Client-side redirects do not prevent access to server responses.  
By stopping or bypassing the redirect, the response body can be inspected directly.

The password is present in the original HTTP response.

## Steps Taken
1. Open the Natas Level 22 webpage.
2. Observe the automatic redirection behavior.
3. Disable or bypass the redirect.
4. Inspect the raw HTTP response.
5. Extract the password from the response body.

## Tools Used
- Web Browser
- HTTP proxy / Developer Tools

## Result
The password for **Natas Level 23** was successfully retrieved by bypassing client-side redirection.
