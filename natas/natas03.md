# OverTheWire Natas — Level 3

## Objective

Retrieve the password by identifying hidden content that has been explicitly excluded from search engine crawlers.

## Access

* URL: http://natas3.natas.labs.overthewire.org/
* Username: natas3
* Password: 3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH

## Method

The source code hints that "Not even Google will find it this time." This implies the use of the `robots.txt` file, which instructs web crawlers on which parts of the site to ignore. Checking `/robots.txt` reveals a disallowed directory named `/s3cr3t/`. Navigating to this directory exposes the `users.txt` file containing the credentials.

## Result

Password for the next level obtained successfully.
QryZXc2e0zahULdHrtHxzyYkj59kUxLQ


## Key Takeaway

* `robots.txt` is a standard for crawler behavior, not a security mechanism.
* Listing sensitive directories in `robots.txt` essentially advertises their existence
