#!/usr/bin/env python3

# Implement the following in this script:
# - Create a card generator
# - Create option for number of generated cards

# Solution #1
# import random

# face = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
# suit = ["Clubs", "Hearts", "Diamonds", "Spades"]

# rf = random.randint(0, 12)
# rs = random.randint(0, 3)

# print("Would you like to see a magic trick? ")
# reply = input()
# if reply.lower() == "yes" or reply.lower() == "y":
#     print("Your card is ", face[rf], " of ", suit[rs], ".")
# else:
#     print("You could have had three wishes, maybe next time.... ;) ")

# Solution #2
import random

face = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suit = ["Clubs", "Hearts", "Diamonds", "Spades"]

i = 0
count = int(input("How many cards would you like drawn? "))
print()
while i < count:
    i += 1
    rf = random.randint(0, 12)
    rs = random.randint(0, 3)
    print("Your card is ", face[rf], " of ", suit[rs], ".", sep="")

print("\nHope one of those were the card you were looking for.  Good luck next time.")
