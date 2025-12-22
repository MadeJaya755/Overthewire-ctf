# Natas Level 21 → Level 22

## Objective
Retrieve the password by abusing inconsistent authorization logic across related applications.

## Environment
- Web-based challenge (OverTheWire Natas)
- Multiple related web applications
- HTTP Basic Authentication
- Shared session handling

## Challenge Overview
The level consists of two related web pages hosted on the same server.  
One page allows modifying user-related settings, while the other checks authorization status.

Authorization logic is split across applications.

## Approach
Session data modified in one application is trusted blindly by the other.  
By manipulating session values on the less restricted page, privileged access can be obtained on the protected page.

This is a classic **trust boundary failure**.

## Steps Taken
1. Open the Natas Level 21 main page.
2. Identify the secondary application that modifies session data.
3. Change session values to indicate privileged access.
4. Return to the protected page using the same session.
5. Extract the password.

## Tools Used
- Web Browser
- Session manipulation

## Result
The password for **Natas Level 22** was successfully retrieved by abusing shared session trust.
