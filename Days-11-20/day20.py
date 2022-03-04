#!/usr/bin/env python3

# Implement the following in this script:
# - Clue random generator
# - Guessing game
# - Regular colors 30 - 37: black, red, green, yellow, blue, magenta, cyan, white
# - Bright colors 90 - 97: black, red, green, yellow, blue, magenta, cyan, white
# - Future Improvement - Give list of options, allow for upper/lower case input (Completed 03/03/22)

import random

class ct:
    cya = '\033[96m' #CYAN
    yel = '\033[93m' #YELLOW
    red = '\033[91m' #RED
    nor = '\033[0m' #RESET COLOR


def clue():
    room = ["Dining Room", "Kitchen", "Study", "Lounge", "Bathroom", "Basement", "Bedroom", "Hall", "Rec Room"]
    tool = ["Rope", "Candlestick", "Revolver", "Poison", "Lead Pipe", "Dagger", "Wrench"]
    who = ["Prof Plum", "Colonel Mustard", "Mr Green", "Mrs Peacock", "Mrs White", "Miss Scarlett"]
    rroom = str(random.choice(room)).lower()
    rtool = str(random.choice(tool)).lower()
    rwho = str(random.choice(who)).lower()
    return rroom, rtool, rwho

# Testing multiple calls to the function generate different results
#for i in range(10):
#    x, y, z = clue()
#    print(x, y, z)

x, y, z = clue()
count = 0

print("Welcome in today.  I hope you are ready to play a mystery game.")

print("Who do you think is the killer?")
print("     ", ct.yel + str("List") + ct.nor, " - Prof Plum, Colonel Mustard, Mr Green, Mrs Peacock, Mrs White, Miss Scarlett", sep="")
while True:
    gwho = str(input()).lower()
    if gwho != z:
        count += 1
        print("That's not correct, try again.\n")
    else:
        count += 1
        break

print(ct.cya + str("Great") + ct.nor, ", you got it right.  Where do you think they committed the crime?", sep="")
print("     ", ct.yel + str("List") + ct.nor, " - Dining Room, Kitchen, Study, Lounge, Bathroom, Basement, Bedroom, Hall, Rec Room", sep="")
while True:
    groom = str(input()).lower()
    if groom != x:
        count += 1
        print("That's not correct, try again.\n")
    else:
        count += 1
        break

print(ct.cya + str("Awesome") + ct.nor, ", you are almost done.  What do you think was the murder weapon?", sep="")
print("     ", ct.yel + str("List") + ct.nor, " - Rope, Candlestick, Revolver, Poison, Lead Pipe, Dagger, Wrench", sep="")
while True:
    gtool = str(input()).lower()
    if gtool != y:
        count += 1
        print("That's not correct, try again.\n")
    else:
        count += 1
        break


score = str(input("I hope that was fun.  Would you like to see your score? ")).lower()
if score == "yes" or score == "y":
    print("It took you", str(count), "guesses to figure out the killer.")

print("You were correct.  It was ", ct.cya + str(z).title() + ct.nor, " with the ", ct.red + y + ct.nor, " in the ", ct.yel + x + ct.nor, ".", sep="")
print("We look forward to seeing you again in the future.  Have a great day.")