#!/usr/bin/env python3

# Implement the following in this script:
# - Create a function to generate a random npc
# - Create a loop to generate a provide number of npcs
# - Convert day 5 script to create SotDL npcs

import random

def subpro(prof):
    academic =   ["Architecture", "Astrology", "Engineering", "Etiquette", "Folklore", "Geography", "Heraldry",
                  "History", "Law", "Literature", "Magic", "Medicine", "Navigation", "Occult", "Philosophy",
                  "Politics", "Nature", "Religion", "Science", "War"]
    commoner =   ["Animal Trainer", "Apothacary", "Artisan", "Artist", "Boatman", "Butcher", "Cook", "Drover", 
                  "Entertainer", "Farmer", "Fisher", "Groom", "Laborer", "Merchant", "Miner", "Musician",
                  "Sailor", "Servant", "Shopkeeper", "Teamster"]
    criminal =   ["Agitator", "Beggar", "Burgler", "Carouser", "Charlatan", "Cultist", "Fence", "Forger",
                  "Gambler", "Grave Robber", "Informant", "Murderer", "Pickpocket", "Pirate", "Prostitute",
                  "Rebel", "Saboteur", "Spy", "Thug", "Urchin"]
    martial =    ["Constable", "Detective", "Guard", "Jailer", "Officer", "Marine", "Mercenary",
                  "Militia Member", "Patroller", "Peasant Conscript", "Slave", "Soldier", "Squire", "Torturer"]
    religious =  ["Devotee", "Evangalist", "Fanatic", "Heretic", "Initiate of the Old Faith", "Minister",
                  "Acolyte of the New God", "Inquisitor's Henchman", "Pilgrim", "Street Preacher", "Temple Ward"]
    wilderness = ["Bandit", "Brigand", "Barbarian", "Exile", "Gatherer", "Guide", "Hermit", "Hunter", "Nomad",
                  "Pioneer", "Poacher", "Prospector", "Outlaw", "Refugee", "Spelunker", "Tracker", "Trapper", "Woodcutter"]

    if prof == "Academic":
        subp = academic[random.randint(0, 19)]
    elif prof == "Commoner":
        subp = commoner[random.randint(0, 19)]
    elif prof == "Criminal":
        subp = criminal[random.randint(0, 19)]
    elif prof == "Martial":
        subp = martial[random.randint(0, 13)]
    elif prof == "Religious":
        subp = religious[random.randint(0, 10)]
    else:
        subp = wilderness[random.randint(0, 17)]
    
    return subp

def npc ():
    gender =     ["Man", "Woman", "Transperson", "Androgynous"]
    ancestry =   ["Human", "Changling", "Clockwork", "Dwarf", "Goblin", "Orc"]
    profession = ["Academic", "Commoner", "Criminal", "Martial", "Religious", "Wilderness"]
    wealth =     ["Destitute", "Poor", "Getting By", "Comfortable", "Wealthy", "Rich"]
    
    gr = gender[random.randint(0, 3)]
    ar = ancestry[random.randint(0, 5)]
    pr = profession[random.randint(0, 5)]
    wr = wealth[random.randint(0, 5)]
    sp = subpro(pr)

    print("... ",  wr, " ",ar, " ", gr, " that is a ", pr, " - ", str(sp), ".", sep="")




count = int(input("How many encounters would you like to see? "))
print("\nYou have encountered a ....")
for i in range(count):
    npc()
print()