# Natas Level 8 → Level 9

## Objective
Retrieve the password by reversing a weak encoding mechanism used to hide a secret value.

## Environment
- Web-based challenge (OverTheWire Natas)
- Access via web browser
- HTTP Basic Authentication

## Challenge Overview
The application asks for a secret value and validates it server-side.  
The secret is not visible directly, but part of the validation logic is exposed in the page source.

The secret is not encrypted — only encoded.

## Approach
The source code reveals that the secret undergoes multiple encoding steps before comparison.  
By reversing these steps in the correct order, the original secret can be recovered.

Once the correct secret is submitted, the password is revealed.

## Steps Taken
1. View the page source.
2. Identify the encoding functions applied to the secret.
3. Reverse the encoding process manually.
4. Submit the decoded secret through the form.
5. Extract the password displayed.

## Tools Used
- Web Browser
- View Page Source
- Manual decoding

## Result
The password for **Natas Level 9** was successfully retrieved by reversing the encoding logic.
