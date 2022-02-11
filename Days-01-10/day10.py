#!/usr/bin/env python3

# Implement the following in this script:
# - Make a simple quest generator
# - Give option for multiple quests
# - Color reference list:
# - Regular colors 30 - 37: black, red, green, yellow, blue, magenta, cyan, white
# - Bright colors 90 - 97: black, red, green, yellow, blue, magenta, cyan, white

import random

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

source = ["blacksmith", "barkeep", "maid", "hermit", "urchin", "priest", "merchant"]
action = ["recover the ", "save the ", "deliver the ", "find the "]
enemy = ["goblins", "wolves", "bandits", "mad wizard", "corrupt sheriff"]
reward = ["some copper", "family heirloom", "some alcohol", "a weapon"]
mcg = ["holy symbol", "village crops", "a book", "money", "medical supplies"]
mac = ["a child", "holy person", "grandparent", "spouse", "local official", "soldier"]

print("Welcome you, tired soul.  Let me help you out.\n")

count = int(input("How many quests do you need, today? "))
print()
for i in range(count):
    rs = random.choice(source)
    ra = random.choice(action)
    re = random.choice(enemy)
    rr = random.choice(reward)
    rmcg = random.choice(mcg)
    rmac = random.choice(mac)
    if ra == "recover the " or ra == "deliver the ":
        ra = ra + rmcg
    else:
        ra = ra + rmac
    print("A local", bcolors.OK + rs + bcolors.RESET, "wants you to", bcolors.WARNING + ra + bcolors.RESET, 
          ".  They believe that", bcolors.FAIL + re + bcolors.RESET, "will be a problem.  They can give you", 
          bcolors.OK + rr + bcolors.RESET, "for helping them out.")

print("\nHopefully, this helped you out.  We look forward to seeing you again.")
