# Natas Level 26 → Level 27

## Objective
Retrieve the password by exploiting insecure object deserialization.

## Environment
- Web-based challenge (OverTheWire Natas)
- Access via web browser
- HTTP Basic Authentication
- PHP backend

## Challenge Overview
The application stores user-related data inside a serialized object.  
This object is sent to the client and later deserialized by the server.

The server assumes the object data is trustworthy.

It is not.

## Approach
Serialized objects can be modified before being sent back to the server.  
By crafting a malicious serialized payload that manipulates object properties, server-side behavior can be altered.

This allows writing arbitrary files to the server and executing code.

## Steps Taken
1. Open the Natas Level 26 webpage.
2. Inspect the serialized object sent to the client.
3. Analyze the object structure and properties.
4. Modify the serialized data to write a malicious file.
5. Send the modified object back to the server.
6. Execute the uploaded file and extract the password.

## Tools Used
- Web Browser
- Manual object serialization manipulation

## Result
The password for **Natas Level 27** was successfully retrieved via insecure object deserialization.
