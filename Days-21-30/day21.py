#!/usr/bin/env python3

# Implement the following in this script:
# - Create a script to get ip from icanhazip.com

import requests

url = "https://icanhazip.com"

res = requests.get(url)
print(res.status_code)


resx = requests.get('https://stackoverflow.com/questions/26000336')
print(resx)


rjs = requests.get(url).json
print(rjs)


response = requests.get('http://icanhazip.com')
fmt = str(response.content).format()
print(fmt)



