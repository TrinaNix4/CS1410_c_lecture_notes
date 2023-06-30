# Author: Trina Nixon
# Date: 06/29/2023
# Brief: A card is drawn.
# choose 1 for the next card will be higher
# choose 2 for the next card will be lower
# or 3. to quit
# keep track of wins and losses
import random

wins = 0
losses = 0
game_over = False

# Draw a card - random number between 1 and 15
# while loop to keep the game going unless player chooses 3 to quit
while not game_over:
    card = random.randint(1, 15)
    print("Card Drawn: ", card)

    print(
        "Choose a number!\n 1. The next card will be higher.\n 2. The next card will be lower. \n 3. Quit")

    choice = input("Your choices are: ")
# choice 1 or 2; draw a new card to compare to previous card
    if choice == "1" or choice == "2":
        next_card = random.randint(1, 15)
        print("Card Drawn: ", next_card)

        if choice == '1' and (next_card >= card) or (choice == '2' and next_card <= card):
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1
    elif choice == '3':
        print("Thanks for playing!")
        game_over = True


print("Wins: ", wins)
print("Losses", losses)
