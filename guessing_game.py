""" Author: INDROJIT DHE SHAON
Personal Code: 17
File: guessing_game.py """

import random as ran

# Create a random number between 1 and 20.
random_number = ran.randrange(1, 21)

print("Welcome. All the best to you.")

# Endless cycle until the guess is accurate
while True:

    guess_input = input("Enter the guess number between 1 t0 20: ")
 
    # Verify whether the input is a number
    if not guess_input.isdigit():
        print("Error. Try again.")
        continue

    guess_input = int(guess_input)

    # Compare the random number to the estimate.
    if guess_input > random_number:
        print("Your number is too high.")

    elif guess_input < random_number:
        print("Your number is too low.")

    else:
        print("Congratulations!!! You win the game.")
        break