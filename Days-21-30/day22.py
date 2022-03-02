#!/usr/bin/env python3

# Implement the following in this script:
# - Run some tests using the json plugin
# - Future script - zippopotam updated to accept alternate date
#                 - allow for zip code input
#                 - allow for state / city input
#
# Some useful APIs for future scripts
# Public API List - https://github.com/public-apis/public-apis#index
# Nationality Predictor - https://nationalize.io/
# Cocktail DB - https://www.thecocktaildb.com/api.php
# Random User Data - https://randomuser.me/api/
# Random Data - https://random-data-api.com/documentation
# Unix Time Converter - https://showcase.api.linx.twenty57.net/UnixTime/fromunix?timestamp=15454869175
# MTG CCG Info - https://docs.magicthegathering.io/#documentationgetting_started
# XKCD Json API - https://xkcd.com/json.html


import json
import requests

###################### 3rd test ######################
# Simple test loading json data from a file
# Populated with sample data from the internet

with open('day22.json') as json_file:
    data = json.load(json_file)
    dd = json.dumps(data, indent=4)

    print("Type:", type(data))
    print()
    print(data)
    print()
    print(data["gadget"])
    print()
    print(dd)



###################### 1st test ######################
# Example pulled from the internet for first experiment

# some JSON:
x =  '{ "name":"Tom", "age":45, "city":"Trenton"}'


# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print()
print(x)
print(y)
print(y["age"]) 
print()

###################### 2nd test ######################
# Pulled the example from the internet
# Tested some of the formatting options for json.dumps

z = {
  "name": "Mary",
  "age": 37,
  "married": False,
  "widowed": True,
  "children": ("Nick","Sara","Leigh"),
  "pets": None,
  "cars": [
    {"model": "Fiat 500 Sport", "year": 2015, "tank": 8.5},
    {"model": "Nissan Pathfinder", "year": 2017, "tank": 16.3}
  ]
}

# print(json.dumps(z, indent=4))
print(json.dumps(z, indent=4, separators=(". ", " = ")))
print()
print(json.dumps(z, indent=4, separators=(", ", " - "), sort_keys=True))
# print(json.dumps(z, indent=4, separators=("", " -- ")))
print(json.dumps(z["children"]))


###################### 4th test ######################
# Sample pulled from Stack Overflow
# https://stackoverflow.com/questions/23306653/python-accessing-nested-json-data
# Played with formatting and alternate data set

r = requests.get('http://api.zippopotam.us/us/tx/paris')
j = r.json()
dj = json.dumps(j, indent=4)

print(j['state'])
print(j['places'][1]['post code'])
print(dj)