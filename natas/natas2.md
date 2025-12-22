# Natas Level 2 → Level 3

## Objective
Locate the password for the next level by discovering hidden directories exposed by the web server.

## Environment
- Web-based challenge (OverTheWire Natas)
- Access via web browser
- HTTP Basic Authentication

## Challenge Overview
The webpage only displays an image and no visible password or hints.  
There is no obvious way to interact with the page.

The password is not on the main page.

## Approach
The HTML source code was inspected to identify referenced resources.  
An image file was loaded from a directory that is not directly linked for browsing.

By manually accessing that directory, additional files became visible.

## Steps Taken
1. Open the Natas Level 2 webpage.
2. View the page source.
3. Identify the image path (`/files/`).
4. Navigate directly to the `/files/` directory.
5. Open the text file containing the password.

## Tools Used
- Web Browser
- View Page Source
- Manual URL navigation

## Result
The password for **Natas Level 3** was successfully retrieved from a file inside the exposed directory.
