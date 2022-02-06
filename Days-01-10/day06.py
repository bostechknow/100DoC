#!/usr/bin/env python3

# Implement the following in this script:
# - Create a choice for random generator
# - Create a choice for number of rolls
# - Options - d100, d66, d666

import random

def percent ():
    pr = random.randint(1, 100)
    return pr

def sixs ():
    s1 = random.randint(1, 6)
    s2 = random.randint(1, 6)
    s3 = str(s1) + str(s2)
    return s3

def evil ():
    s1 = random.randint(1, 6)
    s2 = random.randint(1, 6)
    s3 = random.randint(1, 6)
    s4 = str(s1) + str(s2) + str(s3)
    return s4

print("Hello, would you like me to roll some random numbers for you? ")
query = str(input()).lower()
if query == "yes" or query == "y":
    count = int(input("\nHow many numbers should I make for you? "))
    print("\nAwesome which type of numbers do you want - percentile, d66, or d666?")
    dice = str(input()).lower()
    if dice == "percentile":
        for i in range(count):
            print(percent())
    elif dice == "d66":
        for i in range(count):
            print(sixs())
    elif dice == "d666" or dice == "evil":
        for i in range(count):
            print(evil())
    else:
        print("I'm sorry I don't know how to do that.")

print("Thanks for stopping by today.  Look forward to seeing you again.")