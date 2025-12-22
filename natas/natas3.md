# Natas Level 3 → Level 4

## Objective
Retrieve the password for the next level by discovering hidden resources using standard web crawler directives.

## Environment
- Web-based challenge (OverTheWire Natas)
- Access via web browser
- HTTP Basic Authentication

## Challenge Overview
The webpage provides no visible hints and appears empty.  
Unlike previous levels, no directories are referenced directly in the HTML source.

A subtle hint suggests that automated tools are being kept away.

## Approach
When information is intentionally hidden from search engines, the first file to check is `robots.txt`.  
This file instructs web crawlers which paths should not be indexed.

Hidden directories often appear there.

## Steps Taken
1. Open the Natas Level 3 webpage.
2. Manually access `/robots.txt`.
3. Identify the disallowed directory.
4. Navigate to the discovered directory.
5. Open the file containing the password.

## Tools Used
- Web Browser
- Manual URL navigation

## Result
The password for **Natas Level 4** was successfully obtained from a directory listed in `robots.txt`.
