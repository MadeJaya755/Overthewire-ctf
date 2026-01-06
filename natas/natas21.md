<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">


# OverTheWire Natas — Level 21

## Objective

Exploit a session synchronization vulnerability between two co-located websites to inject administrative privileges.

## Access

* URL: http://natas21.natas.labs.overthewire.org/
* Username: natas21
* Password: d8rwGBl0Xslg3b76uh3fEbSlnOUBlozz

## Method

The main website reads session data but does not provide a way to modify it. However, the source code references a "co-located" website at `http://natas21-experiment.natas.labs.overthewire.org/`.

The experimental site allows users to update their session variables, including an `admin` flag. Since both sites are hosted on the same server and share the same session storage path, we can create a session on the experiment site and use it on the main site.

1.  **Visit the Experiment Site:** Go to the experiment URL.
2.  **Inject Admin Status:** Submit the form to update the session with `admin=1`.
3.  **Capture Session ID:** Copy the value of the `PHPSESSID` cookie from the experiment site.
4.  **Hijack Session:** Return to the main `natas21` website. Edit the `PHPSESSID` cookie to match the one from the experiment site and reload the page.

## Result

Password for the next level obtained successfully.

dIUQcI3uSus1JEOSSWRAEXBG8KbR8tRs


## Key Takeaway

* Applications hosted on the same server often share session storage directories (`/tmp` or `/var/lib/php/sessions`).
* If session IDs are not segregated by application, vulnerabilities in one application can compromise others.
</div>
