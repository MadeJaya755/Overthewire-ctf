# Natas Level 0 → Level 1

## Objective
Retrieve the password for the next level by inspecting the HTML source code of the webpage.

## Environment
- Web-based challenge (OverTheWire Natas)
- Access via web browser
- HTTP Basic Authentication

## Challenge Overview
The webpage shows a simple message and appears harmless.  
No input fields, no buttons, no interaction.

The trick is that the password is not meant to be found visually.

## Approach
The page source code was inspected instead of relying on the rendered view.  
The password was embedded inside an HTML comment, which is invisible during normal page rendering.

This confirms a basic but critical security principle:  
**Anything sent to the client is not secret.**

## Steps Taken
1. Open the Natas Level 0 webpage.
2. Right-click and select **View Page Source**.
3. Locate the HTML comment containing the password.

## Tools Used
- Web Browser (View Page Source)

## Result
The password for **Natas Level 1** was successfully obtained from the HTML source code.
