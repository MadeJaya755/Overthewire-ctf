<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">


# OverTheWire Natas — Level 22

## Objective

Retrieve information leaked by a server-side script that attempts to redirect the user but fails to terminate execution.

## Access

* URL: http://natas22.natas.labs.overthewire.org/
* Username: natas22
* Password: dIUQcI3uSus1JEOSSWRAEXBG8KbR8tRs

## Method

The source code contains logic to print the password if a GET parameter named `revelio` is present. However, immediately after printing the credentials, the script executes `header("Location: /");` to redirect the user back to the homepage.

```php
if(array_key_exists("revelio", $_GET)) {
    print "Password: ...";
}
header("Location: /");
Browsers automatically follow this redirect, hiding the output. To view the password, we must prevent the browser from following the redirect. This can be done by:

Using a proxy like Burp Suite to intercept the response.

Using the view-source: protocol: view-source:http://natas22.natas.labs.overthewire.org/?revelio

Using curl without the location-follow flag.

Result
Password for the next level obtained successfully.

MeuqmfJ8DDKuTr5pcvzFKSwlxedZYEWd
Key Takeaway
The PHP header("Location: ...") function does not stop the script from executing the subsequent code.

Developers must explicitly call exit() or die() after a redirect to prevent data leakage.


</div>
