# Natas Level 10 → Level 11

## Objective
Retrieve the password for the next level by bypassing weak input filtering to exploit command execution.

## Environment
- Web-based challenge (OverTheWire Natas)
- Access via web browser
- HTTP Basic Authentication

## Challenge Overview
The application still executes a system command based on user input.  
This time, a basic blacklist filter is applied to block certain characters.

The developer assumes filtering a few symbols is enough.

It is not.

## Approach
The blacklist only blocks specific characters, not command logic itself.  
By crafting input that avoids the filtered characters but still performs command execution, the filter can be bypassed.

Once command execution is achieved, sensitive files can be read.

## Steps Taken
1. Open the Natas Level 10 webpage.
2. Review the filtering logic shown in the source code.
3. Craft an input payload that avoids blacklisted characters.
4. Execute a command to read the password file.
5. Extract the password from the output.

## Tools Used
- Web Browser
- View Page Source
- Manual payload crafting

## Result
The password for **Natas Level 11** was successfully retrieved by bypassing blacklist-based filtering.
