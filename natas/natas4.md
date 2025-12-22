# Natas Level 4 → Level 5

## Objective
Bypass access restrictions by manipulating HTTP request headers to retrieve the next password.

## Environment
- Web-based challenge (OverTheWire Natas)
- Access via web browser
- HTTP Basic Authentication

## Challenge Overview
Direct access to the page is blocked with an authorization error.  
The application checks where the request is coming from before granting access.

This is a **referer-based restriction**.

## Approach
HTTP headers are controlled by the client.  
By modifying the `Referer` header to match the expected value, the restriction can be bypassed.

This highlights the danger of trusting client-supplied headers for security decisions.

## Steps Taken
1. Attempt to access the Natas Level 4 page.
2. Observe the access restriction message.
3. Send a request with a forged `Referer` header.
4. Reload the page with the modified header.
5. Extract the password displayed on the page.

## Tools Used
- Web Browser
- HTTP proxy / header manipulation tool

## Result
The password for **Natas Level 5** was successfully retrieved after spoofing the HTTP `Referer` header.
