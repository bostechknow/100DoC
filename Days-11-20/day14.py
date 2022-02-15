#!/usr/bin/env python3

# Implement the following in this script:
# - Use random to generate numbers
# - Use a for loop to add the numbers together

import random

print("Welcome to a numbers game.")

while True:
    count = int(input("How many numbers should I generate? "))
    total = 0
    for i in range(count):
        i += 1
        ri = random.randint(1,1000)
        total += ri
        print("Number ", str(i), " is ", str(ri), " and the current total is ", str(total), ".", sep="")
    print("The final total is ", str(total), ".", sep="")

    run = str(input("I hope that was fun.  Want to do that again? (Y/N) ")).lower()
    if run == "y" or run == "yes":
        continue
    else:
        break

print("Thanks for stopping by.  Hopefully, we can help you again in the future.")