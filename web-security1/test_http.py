#!/usr/bin/python
#******************************************************************************
# How to script HTTP requests, and receive their responses
# http://canyouhack.it/Content/Challenges/Web/Web2.php
#******************************************************************************
import requests

website = r"http://canyouhack.it/Content/Challenges/Web/Web2.php"
r = requests.get(website)
print r.headers
print r.status_code
print r.text

headers = {"isAdmin" : "1"}
r = requests.post(website, cookies=headers)
print r.status_code
print r.text
