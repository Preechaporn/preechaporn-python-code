"""
Question 1: Beginner Number Guessing Game

Create a simple number guessing game with these requirements:

Random number between 1-20
    Maximum 6 attempts
    Show remaining attempts after each guess
    Display appropriate win/lose messages
    Validate numeric input only
    
Example 

    === SIMPLE GUESSING GAME ===
    Guess my number between 1 and 20!
    You have 6 attempts.

    Attempt 1/6 - Enter your guess: 10
    Too low! Try again.

    Attempt 2/6 - Enter your guess: 15
    Too high! Try again.

    Attempt 3/6 - Enter your guess: 12
    Congratulations! You won in 3 attempts!

"""

import random

print("=== SIMPLE GUESSING GAME ===\nGuess my number between 1 and 20!\nYou have 6 attempts.")

random_number = random.randint(1,20)

for i in range(6):
    guess_number = int(input(f"Attempt {i+1}/6 - Enter your guess: "))

    if guess_number == random_number :
        print("Congretulations")
        break
    elif guess_number < random_number:
        print("Too low! Try again.")
    elif guess_number > random_number:
        print("too high! Try again.")
    if i == 5 :
        print(f"You lose\nThe number is {random_number}")
        break