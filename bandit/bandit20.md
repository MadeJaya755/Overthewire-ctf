# OverTheWire Bandit — Level 20

## Objective
Retrieve the password for the next level by interacting with a SUID binary that connects to a local network port.

## Access
* **Host:** bandit.labs.overthewire.org
* **Port:** 2220
* **Username:** bandit20

## Method
The home directory contains a SUID binary named `suconnect`. This program is designed to connect to a specific port on `localhost`. Upon connection, it expects to receive the current level's password. If the password matches, it sends back the password for the next level.

1.  **Set up a Listener:** Use Netcat to listen on a random port (e.g., `nc -l -p 1234`) in one terminal window (or using `&` to run in background).
2.  **Execute Binary:** Run `./suconnect 1234` to force the binary to connect to your listener.
3.  **Authenticate:** Paste the current password (`EeoULMCra2q0dSkYj561DX7s1CpBuOBt`) into the Netcat listener. The binary verifies it and replies with the new password.

## Result
Password for the next level retrieved successfully.

`tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q`

## Key Takeaway
* **Netcat (`nc`)** can operate in listening mode (`-l`), acting effectively as a server.
* Testing network applications often requires setting up your own endpoints to receive and validate connections.
