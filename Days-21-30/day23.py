#!/usr/bin/env python3

# Implement the following in this script:
# - Use random data api to pull info
# - Store the data into a json file
# - Future improvement - read the file, fix json appending
# - https://www.kite.com/python/answers/how-to-append-to-a-json-file-in-python


import json
import requests

print("Welcome in today.  Hopefully, we can assist with your needs.\n")

count = int(input("How many people should we gather for you today? "))

for i in range(count):
    r = requests.get('https://randomuser.me/api/')
    j = r.json()
    dj = json.dumps(j, indent=4)
    print(dj)
    with open('day23.json', 'a', encoding='utf-8') as f:
        json.dump(j, f, ensure_ascii=False, indent=4)
        f.write(",\n")

print("Thanks for coming in today.  I hope we were able to help you out.")
print("We look forward to assisting you again in the future.")