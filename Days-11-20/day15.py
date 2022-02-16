#!/usr/bin/env python3

# Implement the following in this script:
# - Take input and store in a list
# - Provide count of items in list
# - Provide output of first & last in list
# - Reverse the list
# - Sort the list
# - Bright colors 90 - 97: black, red, green, yellow, blue, magenta, cyan, white
# - Future improvement - Allow choice of outputs


class bc:
    mg = '\033[95m' 
    gr = '\033[92m' 
    norm = '\033[0m'  #RESET COLOR

print("Thank you for playing today.")

custom = []
while True:
    custom.append(input("What do you want to store? "))
    cont = str(input("Store another?? Type break if done.")).lower()
    if cont == "break":
        break

print("\nThank you for your input today.")
print("\nYour list of items are the following: ")
print(custom)
print("\nThe total number of items in your list is ", bc.gr + str(len(custom)) + bc.norm, ".", sep="")
print("The first item in your list is ", custom[0], ".", sep="")
print("The last item in your list is ", custom[-1], ".", sep="")
print("Your list in", bc.mg + "reverse" + bc.norm, "is the following: ")
custom.reverse()
print(custom)
print("\nYour list", bc.mg + "sorted" + bc.norm, "is the following: ")
custom.sort()
print(custom)
print("\nThank you for coming today.  I hope that was a fun exercise.")