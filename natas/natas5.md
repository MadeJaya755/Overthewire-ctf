# Natas Level 5 → Level 6

## Objective
Bypass authentication logic that relies on client-side state to obtain the next password.

## Environment
- Web-based challenge (OverTheWire Natas)
- Access via web browser
- HTTP Basic Authentication

## Challenge Overview
The webpage indicates that access is restricted to logged-in users.  
However, there is no visible login form or authentication mechanism.

Access control is handled entirely on the client side.

## Approach
The application relies on a cookie to determine whether a user is logged in.  
Since cookies are fully controlled by the client, the value can be modified manually.

By setting the authentication cookie to the expected value, access is granted.

## Steps Taken
1. Open the Natas Level 5 webpage.
2. Inspect the cookies set by the application.
3. Identify the authentication-related cookie.
4. Modify the cookie value to indicate an authenticated state.
5. Reload the page and extract the password.

## Tools Used
- Web Browser
- Cookie editor / Developer Tools / HTTP proxy

## Result
The password for **Natas Level 6** was successfully retrieved by manipulating client-side cookies.
