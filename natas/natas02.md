# OverTheWire Natas — Level 2

## Objective

Locate a hidden file containing the password by investigating the web server's directory structure.

## Access

* URL: http://natas2.natas.labs.overthewire.org/
* Username: natas2
* Password: TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI

## Method

The page displays a small pixel image. Inspecting the source code reveals the image source is located at `files/pixel.png`. Navigating directly to the `/files/` directory reveals that directory listing is enabled. This exposes a file named `users.txt`, which contains the credentials.

## Result

Password for the next level obtained successfully.
3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH


## Key Takeaway

* Security by obscurity (hiding files in secret folders) is ineffective.
* Directory listing should be disabled on web servers to prevent information leakage.
