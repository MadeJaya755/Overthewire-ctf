# Natas Level 17 → Level 18

## Objective
Retrieve the password by exploiting time-based blind SQL injection.

## Environment
- Web-based challenge (OverTheWire Natas)
- Access via web browser
- HTTP Basic Authentication
- Backend database

## Challenge Overview
The application checks user input against a database but provides no visible output.  
There are no error messages and no content differences in responses.

The only observable difference is **response time**.

## Approach
Since no data is returned directly, time delays can be used as a side channel.  
By injecting SQL statements that cause conditional delays, database values can be inferred.

Each character of the password is extracted by measuring response time.

## Steps Taken
1. Open the Natas Level 17 webpage.
2. Submit a normal request to establish baseline response time.
3. Inject time-based SQL conditions.
4. Measure server response delays.
5. Extract the password character by character.
6. Reconstruct the full password.

## Tools Used
- Web Browser
- Manual time-based SQL injection
- Timing analysis

## Result
The password for **Natas Level 18** was successfully retrieved using time-based blind SQL injection.
