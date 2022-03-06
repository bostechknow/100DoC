#!/usr/bin/env python3

# Implement the following in this script:
# - Create an input for character information
# - Utilize f-string to format output

print("Welcome in, I hope we can help you out today.")
print("\nWe are going to ask you for some information.\n")

name = input("What is your character's name? ")
age = input("What is your character's age? ")
gender = input("What is your character's gender? ")
ancest = input("What is your character's ancestry? ")
prof = input("What is your character's profession? ")
path = input("What is your novice path? ")
gift = input("What is your starting gift? ")

print(f"Character sheet\n---------------\nName:         {name}\nAge:          {age}\nGender:       {gender}\nAncestry:     {ancest}\nProfession:   {prof}\nNovice Path:  {path}\nTrinket:      {gift}")