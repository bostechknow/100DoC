#!/usr/bin/env python3

# Implement the following in this script:
# - Reverse the text
# - Count the number of characters
# - Give the UTF-8 ordinal value of the characters

text = input("Please provide me some text: ")

print("\nWhich would you like to see - text length, reversed text, or UTF-8 values of the text?")
which = input("Please type 1 for length, 2 for reversed, or 3 for UTF-8 values: ")

if which == "1":
    print("\nYour text is ", len(str(text)), " characters in length.")
elif which == "2":
    print("\nYour text in reverse is: ", str(text)[::-1])
elif which == "3":
    print()
    for i in str(text)[::]:
        print("The UTF-8 ordinal value of ", i, " is ", ord(i))
else:
    print("\nI am sorry we could not help you today.  Maybe next time.")