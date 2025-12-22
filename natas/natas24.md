# Natas Level 24 → Level 25

## Objective
Retrieve the password by exploiting PHP type juggling in input validation.

## Environment
- Web-based challenge (OverTheWire Natas)
- Access via web browser
- HTTP Basic Authentication
- PHP backend

## Challenge Overview
The application validates user input using a loose comparison.  
The comparison logic assumes input types behave as expected.

In PHP, that assumption is wrong.

## Approach
PHP performs automatic type juggling when using loose comparison operators.  
By supplying specially crafted input, the comparison can be forced to evaluate as true even when the values do not actually match.

This allows bypassing the validation logic.

## Steps Taken
1. Open the Natas Level 24 webpage.
2. Observe the input validation behavior.
3. Identify the use of loose comparison.
4. Submit crafted input that abuses PHP type juggling.
5. Extract the password displayed.

## Tools Used
- Web Browser
- Manual input crafting

## Result
The password for **Natas Level 25** was successfully retrieved by abusing PHP type juggling.
