# Natas Level 20 → Level 21

## Objective
Retrieve the password by exploiting insecure server-side session data handling.

## Environment
- Web-based challenge (OverTheWire Natas)
- Access via web browser
- HTTP Basic Authentication
- Server-side session storage

## Challenge Overview
The application stores session data on the server using a custom format.  
User-controlled input is written directly into the session without proper validation.

Session data persists across requests.

## Approach
By injecting crafted data into the session storage, server-side variables can be manipulated.  
This allows overwriting values that control authorization logic.

Once the session is poisoned with privileged data, access is granted.

## Steps Taken
1. Open the Natas Level 20 webpage.
2. Submit input that is stored in the server-side session.
3. Inject structured data to modify session variables.
4. Reload the page using the poisoned session.
5. Extract the password displayed.

## Tools Used
- Web Browser
- Manual session poisoning

## Result
The password for **Natas Level 21** was successfully retrieved via server-side session manipulation.
