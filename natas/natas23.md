# Natas Level 23 → Level 24

## Objective
Retrieve the password by exploiting weak string comparison logic.

## Environment
- Web-based challenge (OverTheWire Natas)
- Access via web browser
- HTTP Basic Authentication

## Challenge Overview
The application checks whether a provided input matches a required phrase.  
Access is granted only if the condition evaluates to true.

The comparison logic is flawed.

## Approach
The server performs an unsafe string comparison that can be manipulated.  
By crafting input that satisfies the comparison condition without matching the exact expected string, the check can be bypassed.

This exploits improper use of comparison operators.

## Steps Taken
1. Open the Natas Level 23 webpage.
2. Review the validation message and behavior.
3. Craft input that triggers the comparison condition.
4. Submit the manipulated input.
5. Extract the password displayed.

## Tools Used
- Web Browser
- Manual input manipulation

## Result
The password for **Natas Level 24** was successfully retrieved by abusing weak string comparison.
