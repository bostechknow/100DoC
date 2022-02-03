#!/usr/bin/env python3

num = int(input("Please provide my a whole starting number: "))
num2 = int(input("Please provide me a whole ending number: "))
for i in range(num, num2+1):
    print(chr(i), end=" ")