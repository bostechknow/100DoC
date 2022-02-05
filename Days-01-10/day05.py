#!/usr/bin/env python3

# Implement the following in this script:
# - Create a function to generate a random npc
# - Create a loop to generate a provide number of npcs
# - Future improvement, import details from a json file

import random

def npc ():
    gender = ["Man", "Woman", "Transperson", "Asexual"]
    job = ["Celebrity", "Laborer", "Civil Servent", "Student", "Financier", "Reporter"]
    item = ["Book", "Hold-out Pistol", "PDA", "Messenger Bag", "Pen", "Glasses", "Flask"]
    mood = ["Depressed", "Happy", "Scared", "Nervous", "Kind", "Cruel", "Helpful", "Devious"]
    gr = random.randint(0, 3)
    jr = random.randint(0, 5)
    ir = random.randint(0, 6)
    mr = random.randint(0, 7)
    print("...", mood[mr], gender[gr], "that is a", job[jr], "with a", item[ir], ".")

count = int(input("How many encounters would you like to see? "))
print("\nYou have encountered a ....")
for i in range(count):
    npc()
print()