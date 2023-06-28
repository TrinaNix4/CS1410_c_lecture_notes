'''
File: main.py
author: Trina Nixon
brief: Slot Machine generates 3 random numbers and the user wins if they match
date: 06/27/2023
'''

import random

print("Slot Machine")

tokens = 100
print("Tokens: ", tokens)

choice = input("Press p to pull")

while tokens > 0 and choice == "p" or choice == "P":
    slot1 = random.randrange(1, 7)
    slot2 = random.randrange(1, 7)
    slot3 = random.randrange(1, 7)

    print(slot1, slot2, slot3)

    if slot1 == slot2 and slot1 == slot3:
        print("You win 6 tokens!")
        tokens += 6
    # if any 2 are equal
    elif slot1 == slot2 or slot1 == slot3 or slot2 == slot3:
        print("You win 2 tokens!")
        tokens += 2
    else:
        print("You lose!")
        tokens -= 1
    print("Tokens: ", tokens)
    choice = input("Press p to pull")
