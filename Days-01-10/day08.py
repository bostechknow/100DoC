#!/usr/bin/env python3

# Implement the following in this script:
# - Create a function to generate a random npc
# - Create a loop to generate a provide number of npcs
# - Convert day 5 script to create SotDL npcs

import random

def prof(pro):
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

    if pro == "academic":
        pro = "Academic - ", academic[random.randint(0, 19)]
    elif pro == "commoner":
        pro = "Commoner - ", commoner[random.randint(0, 19)]
    elif pro == "criminal":
        pro = "Criminal - ", criminal[random.randint(0, 19)]
    elif pro == "martial":
        pro = "Martial - ", martial[random.randint(0, 13)]
    elif pro == "religious":
        pro = "Religious - ", religious[random.randint(0, 10)]
    elif pro == "wilderness":
        pro = "Wilderness - ", wilderness[random.randint(0, 17)]
    return pro

def npc ():
    gender =     ["Man", "Woman", "Transperson", "Androgynous"]
    ancestry =   ["Human", "Changling", "Clockwork", "Dwarf", "Goblin", "Orc"]
    profession = ["Academic", "Commoner", "Criminal", "Martial", "Religious", "Wilderness"]
    wealth =     ["Destitute", "Poor", "Getting By", "Comfortable", "Wealthy", "Rich"]
    
    gr = random.randint(0, 3)
    ar = random.randint(0, 5)
    pr = random.randint(0, 5)
    wr = random.randint(0, 5)
    pro = profession[pr]
    
    print("...",  wealth[wr], ancestry[ar], gender[gr], "that is a", prof(pro), "with a",  ".")




count = int(input("How many encounters would you like to see? "))
print("\nYou have encountered a ....")
for i in range(count):
    npc()
print()