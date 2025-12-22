# Natas Level 12 → Level 13

## Objective
Retrieve the password by abusing insecure file upload validation.

## Environment
- Web-based challenge (OverTheWire Natas)
- Access via web browser
- HTTP Basic Authentication

## Challenge Overview
The application provides a file upload feature with restrictions on file type.  
Only image files are supposedly allowed to be uploaded.

The validation is weak and relies on client-controlled values.

## Approach
The file type check is performed using the file extension and/or client-supplied metadata.  
By uploading a file with a valid image extension but containing executable code, server-side execution can be achieved.

Once code execution is available, the password file can be read directly.

## Steps Taken
1. Open the Natas Level 12 webpage.
2. Inspect the upload form and validation logic.
3. Prepare a malicious file with an allowed extension.
4. Upload the file to the server.
5. Access the uploaded file to execute code.
6. Read and extract the password.

## Tools Used
- Web Browser
- File upload manipulation
- Manual payload crafting

## Result
The password for **Natas Level 13** was successfully retrieved by exploiting insecure file upload handling.
