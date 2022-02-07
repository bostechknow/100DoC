#!/usr/bin/env python3

# Implement the following in this script:
# - Create a simple beer journal
# - Store entry in a local file


f = open("beer.txt", "a")

name = input("What is the name of the beer? ")
type = input("What type of beer is it? ")
brew = input("What is the name of the brewery? ")
rate = input("What rating out of 5 stars? ")
note = input("Any particular notes you want to share? ")

beer_note = ["Beer:    ", name, "\nType:    ", type, "\nBrewery: ", brew, "\nRating:  ", rate, "\nNotes:   ", note, "\n\n"]

f = open("beer.txt", "a")
f.writelines(beer_note)
f.close()


#open and read the file after the appending:
f = open("beer.txt", "r")
print(f.read()) 