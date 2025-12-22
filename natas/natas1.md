# Natas Level 1 → Level 2

## Objective
Retrieve the password for the next level despite client-side restrictions that block common inspection actions.

## Environment
- Web-based challenge (OverTheWire Natas)
- Access via web browser
- HTTP Basic Authentication

## Challenge Overview
The webpage disables right-click to prevent users from accessing the context menu.  
At first glance, this may appear to block source code inspection.

This is a **fake restriction**.

## Approach
Client-side restrictions do not provide real security.  
The page source can still be accessed directly using browser shortcuts or menus.

The password remains embedded inside the HTML source code.

## Steps Taken
1. Open the Natas Level 1 webpage.
2. Use browser menu or shortcut (`Ctrl+U`) to view page source.
3. Locate the HTML comment containing the password.

## Tools Used
- Web Browser
- View Page Source (menu / shortcut)

## Result
The password for **Natas Level 2** was successfully extracted from the HTML source code.
