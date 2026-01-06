<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">

# OverTheWire Natas — Level 13

## Objective

Bypass server-side file type validation that checks for image signatures (Magic Bytes) to upload and execute a web shell.

## Access

* URL: http://natas13.natas.labs.overthewire.org/
* Username: natas13
* Password: z3UYcr4v4uBpeX8f7EZbMHlzK4UR2XtQ

## Method

This level improves upon the previous one by using the `exif_imagetype()` function to ensure the uploaded file is an image. However, this function only validates the file header (Magic Bytes).

To bypass this:
1.  **Forge the File:** Create a file that starts with the JPEG Magic Bytes (`\xFF\xD8\xFF\xE0`) followed by the PHP payload:
    `<?php passthru('cat /etc/natas_webpass/natas14'); ?>`
2.  **Upload & Intercept:** Upload this forged file. Intercept the request (using Burp Suite or by modifying the HTML input) to ensure the `filename` parameter ends in `.php` instead of `.jpg`.
3.  **Execute:** Navigate to the uploaded file URL. The server sees it as an image due to the header, but the PHP interpreter executes the code because of the extension.

## Result

Password for the next level obtained successfully.

SdqIqBsFcz3yotlNYErZSZwblkm0lrvx


## Key Takeaway

* Validating file headers (Magic Bytes) alone is insufficient to prevent malicious uploads.
* Ideally, servers should re-encode uploaded images (stripping metadata and code) or store them on a separate server that does not execute PHP.
</div>
