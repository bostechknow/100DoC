#!/usr/bin/env python3

# Implement the following in this script:
# - Make a calculator
# - Give math operators
# - Use loop to allow multiple calculations
# - Future improvement - allow int or float

print("Welcome to the Bare Bones Calculator.")

while True:
    n1 = int(input("\nWhat is your first integer?           "))
    op = str(input("Which operation is needed? + - * /    "))
    n2 = int(input("What is your second integer?          "))
    if op == "+":
        out = n1 + n2
    elif op == "-":
        out = n1 - n2
    elif op == "*":
        out = n1 * n2
    else:
        out = n1 / n2
    print("The result of", str(n1), op, str(n2), "=", out, ".")
    run = input("\nI hope that was helpful.  Would you like another calculation(True/False)? ")
    if bool(run) != True:
        break

print("Thanks for stopping by today.  Hope to see you again real soon.")