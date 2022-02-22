#!/usr/bin/env python3

# Implement the following in this script:
# - Create a random tarot generator
# - Allow option for multiple draws
# - Reference:
# -  https://en.wikipedia.org/wiki/Minor_Arcana
# -  https://en.wikipedia.org/wiki/Major_Arcana
# - Future Improvements -
# -            Colorize suit output
# -            Provide short meaning with return
# -            Prevent duplicate draws

import random

def major():
    arcana = [
        "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor", "The Heirophant",
        "The Lovers", "The Chariot", "Justice", "The Hermit", "Wheel of Fortune", "Strength", "The Hanged Man",
        "Death", "Temperance", "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World"
    ]
    choice = random.choice(arcana)
    return choice

def minor():
    suit = ["swords", "rods", "coins", "cups"]
    face = ["ace of ", "two of ", "three of ", "four of ", "five of ", "six of ", "seven of ",
            "eight of ", "nine of ", "ten of ", "page of ", "knight of ", "queen of ", "king of "]
    rface = random.choice(face)
    rsuit = random.choice(suit)
    choice = rface + rsuit
    return choice

print("Welcome in weary traveler.  Hopefully, we can help you today.\n")

while True:
    draw = int(input("How many cards should I draw for you? "))
    print()
    print("I've drawn the following cards for you ...\n")
    call = ["major", "minor"]
    for i in range(draw):
        card = random.choice(call)
        if card == "major":
            out = major()
            print("     ...", out)
        else:
            out = minor()
            print("     ...", out)
    again = str(input("\nWould you like us to draw some more cards for you? (Y/N) ")).lower()
    if again == "y" or again == "yes":
        continue
    else:
        break

print("\nI hope this was helpful for you today.  We look forward to helping you again in the future.")
    