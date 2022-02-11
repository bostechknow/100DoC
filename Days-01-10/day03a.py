#!/usr/bin/env python3

# First solution to test out UTF-8 character printing

# Prints the UTF-8 characters from 0 through num input
#num = int(input("Please provide my a whole number: "))
#for i in range(num):
#    print(chr(i), end=" ")

# Second solution to test out UTF-8 character printing
# Allows for input for start and end of the range
num = int(input("Please provide me a whole starting number: "))
num2 = int(input("Please provide me a whole ending number: "))
for i in range(num, num2+1):
    print(chr(i), end=" ")