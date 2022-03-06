#!/usr/bin/env python3

# Implement the following in this script:
# - Make a tip calculator
# - Give options for several different tip amounts
# - Ask how many people to divide the check
# - Use loop for practice
# - Future improvement - Convert tip calculation into a function
# - Spare code to review:
# final_amount = round(bill_per_person, 2)
# final_amount = "{:.2f}".format(bill_per_person)
    

print("Welcome in.  Hopefully, we can help you out today.\n")

while True:
    base = float(input("What was the total of the bill?                          "))
    tip = int(input("How much of a tip do you want to give - 10, 12, 15, 20?  "))
    if tip == 10 or tip == 12 or tip == 15 or tip == 20:
        heads = int(input("How many people are dividing the check?                  "))
        if tip == 10:
            total = round(base * 1.10, 2)
            part = round(base * 1.10 / float(heads), 2)
        elif tip == 12:
            total = round(base * 1.12, 2)
            part = round(base * 1.12 / float(heads), 2)
        elif tip == 15:
            total = round(base * 1.15, 2)
            part = round(base * 1.15 / float(heads), 2)
        else:
            total = round(base * 1.20, 2)
            part = round(base * 1.20 / float(heads), 2)
        print("\nThe total with tip is $", str(total), ".", sep="")
        print("Each person owes      $", str(part), ".", sep="")
    else:
        print("I'm sorry, I don't know how to calculate that.")

    run = input("\nI hope that was helpful.  Do you need us to calculate another round(True/False)? ")
    if bool(run) != True:
        break

print("\nThanks for stoppping by.  Hope we can help you again in the future.")