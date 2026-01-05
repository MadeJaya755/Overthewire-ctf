# OverTheWire Bandit — Level 24

## Objective
Retrieve the password for the next level by brute-forcing a 4-digit PIN code on a local network service.

## Access
* **Host:** bandit.labs.overthewire.org
* **Port:** 2220
* **Username:** bandit24

## Method
A daemon is listening on port **30002**. To retrieve the password, it requires the current password (`bandit24`) followed by a space and a secret 4-digit PIN (0000-9999).

Since the search space is small (10,000 combinations), a simple bash loop can be used to generate all possible PINs and pipe them to the network service.

1.  **Scripting the Attack:** Used a loop to generate lines in the format `<password> <pin>`:
    ```bash
    for i in {0000..9999}; do echo "iCi86ttT4KSNe1armKiwbQNmB3YJP3q4 $i"; done | nc localhost 30002 | grep -v "Wrong!"
    ```
2.  **Execution:** The script sends all combinations to the port via Netcat. The `grep -v` command filters out the failure messages, leaving only the success message containing the new password.

## Result
Password for the next level retrieved successfully.

`s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ`

## Key Takeaway
* **Brute-forcing:** Rapidly trying all possible combinations is a viable attack method when the search space (entropy) is low, such as a 4-digit PIN.
* **Scripting:** Bash loops combined with network tools (`nc`) allow for powerful, automated interaction with services.
