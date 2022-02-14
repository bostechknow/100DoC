#!/usr/bin/env python3

# Implement the following in this script:
# - Take the random npc generator and write output to character file
# - Future Improvement - More options to the npc generator from other script will help
# - Future Improvement - Put lists and random generators back into a function
# - Future Improvement - A Better true/false check

import random

gender =     ["Man", "Woman", "Transperson", "Androgynous"]
ancestry =   ["Human", "Changling", "Clockwork", "Dwarf", "Goblin", "Orc"]
profession = ["Academic", "Commoner", "Criminal", "Martial", "Religious", "Wilderness"]
wealth =     ["Destitute", "Poor", "Getting By", "Comfortable", "Wealthy", "Rich"]


f = open("npc.txt", "a")

print("Welcome to the NPC generator.")
count = int(input("How many npcs should I generate for you? "))
print("\nYou have encountered a ....")
for i in range(count):
    gr = gender[random.randint(0, 3)]
    ar = ancestry[random.randint(0, 5)]
    pr = profession[random.randint(0, 5)]
    wr = wealth[random.randint(0, 5)]   
    print("...",  wr, ar, gr, "that is a", pr, ".")
    npc_note = ["Wealth:      ", wr, "\nAncestry:    ", ar, "\nGender:      ", gr, "\nProfession:  ", pr, "\n\n"]
    f = open("npc.txt", "a")
    f.writelines(npc_note)
    f.close()   
print()

#open and read the file after the appending:
read = input("\nI hope those were helpful.  Would you like to see the text file(True/False)? ")
if bool(read) != True:
    print("Thanks for stopping by.  Hope to see you again.")
else:
    f = open("npc.txt", "r")
    print(f.read())
