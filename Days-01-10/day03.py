#!/usr/bin/env python3

# Implement the following in this script:
# - Create a function for math
# - Math - Square and Cube
# - Output the UTF-8 character that matches the number
# - Use the while loop again

def math(num):
    print("\nYour number is ", num)
    # print("The square of your number is ", int(num) * int(num))
    # print("The cube of your number is ", int(num) * int(num) * int(num))    
    print("The square of your number is ", int(num) ** 2)
    print("The cube of your number is ", int(num) ** 3)
    print("Your number as a UTF-8 character is ", chr(int(num)))

while True:
    num = input("Please provide me with a whole number: ")
    math(num)

    run = input("\nI hope that was interesting.  Would you like to try another number(True/False)? ")
    if bool(run) != True:
        break

print("\nThanks for stopping by today.  Hope to see you again soon.")