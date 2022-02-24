#!/usr/bin/env python3

# Implement the following in this script:
# - Clue random generator
# - Guessing game
# - Regular colors 30 - 37: black, red, green, yellow, blue, magenta, cyan, white
# - Bright colors 90 - 97: black, red, green, yellow, blue, magenta, cyan, white
# - Future Improvement - Give list of options, allow for upper/lower case input

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
    rroom = random.choice(room)
    rtool = random.choice(tool)
    rwho = random.choice(who)
    return rroom, rtool, rwho


#for i in range(10):
#    x, y, z = clue()
#    print(x, y, z)

x, y, z = clue()
count = 0

print("Welcome in today.  I hope you are ready to play a mystery game.")

print("Who do you think is the killer?")
while True:
    gwho = input()
    if gwho != z:
        count += 1
        print("That's not correct, try again.\n")
    else:
        count += 1
        break

print("Great, you got it right.  Where do you think they committed the crime?")
while True:
    groom = input()
    if groom != x:
        count += 1
        print("That's not correct, try again.\n")
    else:
        count += 1
        break

print("Awesome, you are almost done.  What do you think was the murder weapon?")
while True:
    gtool = input()
    if gtool != y:
        count += 1
        print("That's not correct, try again.\n")
    else:
        count += 1
        break


score = str(input("I hope that was fun.  Would you like to see your score? ")).lower()
if score == "yes" or score == "y":
    print("It took you", str(count), "guesses to figure out the killer.")

print("You were correct.  It was ", ct.cya + z + ct.nor, " with the ", ct.red + y + ct.nor, " in the ", ct.yel + x + ct.nor, ".", sep="")
print("We look forward to seeing you again in the future.  Have a great day.")