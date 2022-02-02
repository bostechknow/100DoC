#!/usr/bin/env python3

# Implement the following in this script:
# - Implement a simple mad libs
# - Implement a while loop

print("Welcome to the Fun House")

while True:
    name = input("\nName please: ")
    name2 = input("Another name please: ")
    adj = input("A descriptive: ")
    adj2 = input("Another descriptive: ")
    adj3 = input("Another descriptive: ")
    loc = input("Somewhere neat: ")
    act = input("An action verb: ")
    act2 = input("Another action verb: ")
    rand = input("Any word you want: ")


    print("\nOnce upon a time, ", name, " was known to be the ", adj, " alien in ", loc, ".")
    print("However, one day, ", name2, " came to ", loc, " and when they arived, things went downhill.")
    print(name, " and ", name2, " started ", act, ".  This caused everyone else to ", act2, ".")
    print("And, that is why ", adj2, " days are called ", adj3, " ", rand, " days.\n" )

    run = bool(input("Do you want to do this again (True/False)?? "))
    if run != True:
        break

print("\nThank you for stopping by, we look forward to you visiting again soon.")