# OverTheWire Bandit — Level 16

## Objective
Retrieve the credentials for the next level by scanning a range of ports to identify a service that accepts the current password over SSL.

## Access
* **Host:** bandit.labs.overthewire.org
* **Port:** 2220
* **Username:** bandit16

## Method
The password for the next level is hosted on a specific port within the range **31000 to 32000**.
1.  **Port Scanning:** Used `nmap` to scan the specified range (`nmap -p 31000-32000 localhost`) to identify open ports.
2.  **Service Identification:** Checked which of the open ports supported **SSL** and echoed input.
3.  **Retrieval:** Connected using `openssl s_client -connect localhost:<found_port>` and submitted the current password (`EReVavePLFHtFlFsjn3hyzMlvSuSAcRD`).

The service responded with an **RSA Private Key** instead of a plain password.

## Result
SSH Private Key for the next level retrieved successfully.
EReVavePLFHtFlFsjn3hyzMlvSuSAcRD.

## Key Takeaway
* Port scanning allows the discovery of hidden services within a network range.
* Not all credentials are simple text strings; SSH keys are a common method for privileged access.
* `nmap` is essential for reconnaissance and discovering listening ports.
