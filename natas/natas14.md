<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">


# OverTheWire Natas — Level 14

## Objective

Bypass a login authentication form using a classic SQL Injection vulnerability.

## Access

* URL: http://natas14.natas.labs.overthewire.org/
* Username: natas14
* Password: SdqIqBsFcz3yotlNYErZSZwblkm0lrvx

## Method

The page presents a username and password login form. Examining the source code reveals the database query structure:

"SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\""
The inputs are inserted directly into the SQL query without sanitization. To bypass the check, we can inject SQL syntax that makes the WHERE clause always evaluate to true.

Payload: In the username field, enter: " OR 1=1 --

This alters the query to: SELECT * from users where username="" OR 1=1 --" and password="..." Since 1=1 is always true, the database returns a valid user record, bypassing the password check.

## Result
Password for the next level obtained successfully.

hPkjKYviLQctEW33QmuXL6eDVfMW4sGo

## Key Takeaway
String concatenation should never be used to build SQL queries.

SQL Injection allows attackers to manipulate database queries, bypassing authentication or accessing unauthorized data.

Always use Prepared Statements (Parameterized Queries) to prevent SQL injection.


</div>
