# Natas Level 13 → Level 14

## Objective
Retrieve the password by bypassing server-side file type verification.

## Environment
- Web-based challenge (OverTheWire Natas)
- Access via web browser
- HTTP Basic Authentication

## Challenge Overview
The application improves the previous upload restriction by validating image files using server-side checks.  
Only files that pass the image verification are accepted.

The developer assumes this is sufficient.

It is still not.

## Approach
The server checks whether the uploaded file is a valid image, but does not restrict executable content within it.  
By embedding server-executable code inside a valid image file, both checks can be satisfied.

This allows code execution after upload.

## Steps Taken
1. Open the Natas Level 13 webpage.
2. Analyze server-side image validation behavior.
3. Embed executable code inside a valid image file.
4. Upload the crafted image.
5. Access the uploaded file to execute code.
6. Read and extract the password.

## Tools Used
- Web Browser
- Image manipulation
- Manual payload crafting

## Result
The password for **Natas Level 14** was successfully retrieved despite server-side image validation.
