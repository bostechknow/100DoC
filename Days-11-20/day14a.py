#!/usr/bin/env python3

# Implement the following in this script:
# - Use random to generate numbers
# - Use a for loop to add the numbers together
# - Bright colors 90 - 97: black, red, green, yellow, blue, magenta, cyan, white

import random


class bcolors:
    blue = '\033[94m' #BLUE
    yell = '\033[93m' #YELLOW
    cyan = '\033[96m' #CYAN
    norm = '\033[0m'  #RESET COLOR

print("Welcome to a numbers game.")

while True:
    count = random.randint(1, 100)
    print("I am going to generate ", str(count), " random numbers and add them together.\n", sep="")

    total = 0
    for i in range(count):
        i += 1
        ri = random.randint(1,1000)
        total += ri
        print("Number ", bcolors.yell + str(i) + bcolors.norm, " is ", bcolors.cyan + str(ri) + bcolors.norm, 
              " and the current total is ", bcolors.blue + str(total) + bcolors.norm, ".", sep="")

    print("\nThe final total is ", str(total), ".", sep="")

    run = str(input("\nI hope that was fun.  Want to do that again? (Y/N) ")).lower()
    if run == "y" or run == "yes":
        continue
    else:
        break

print("\nThanks for stopping by.  Hopefully, we can help you again in the future.")