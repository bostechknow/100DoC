#!/usr/bin/env python3

# Implement the following in this script:
# - rock, paper, scissors game
# - Future improvements:
# - Win/loss count/ratio upon exiting
# - Convert to rock, paper, scissors, lizard, spock

import random

print("Do you want to play a game? ")
start = str(input()).lower()

while start == "y" or start == "yes":
    choice = str(input("Rock, paper, or scissors? ")).lower()
    opts = ("rock", "paper", "scissors")
    comp = random.choice(opts)

    print("\nYou chose ", choice)
    print("The computer chose ", comp, "\n")

    if choice == "rock" and comp == "scissors":
        print("You win.\n")
    elif choice == "scissors" and comp == "paper":
        print("You win.\n")
    elif choice == "paper" and comp == "rock":
        print("You win.\n")
    elif choice == "rock" and comp == "rock":
        print("Tied.\n")
    elif choice == "scissors" and comp == "scissors":
        print("Tied.\n")
    elif choice == "paper" and comp == "paper":
        print("Tied.\n")
    else:
        print("You lost.\n")

    start = str(input("Another game? ")).lower()


print("Thanks for stopping by today.")