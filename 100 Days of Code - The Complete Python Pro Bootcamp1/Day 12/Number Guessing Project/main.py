import difflib

import art
import random
number=[]
for i in range(1,100):
    number.append(i)
print(number)
guess_number = random.choice(number)
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
def correct_guess(input,guess_number,turns):
    if input > guess_number:
        print("Too high!")
        return turns -1
    elif input < guess_number:
        print("Too low!")
        return turns-1
    else:
        print(f"you got the  Answer!:{guess_number}")
def set_difficulty():
    play = input("I'm thinking of a number between 1 and 100.Choose a difficulty. Type 'easy' or 'hard':")
    if play=="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
print(art.logo)
                # Choosing a random number between 1 and 100.
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = guess_number
print(f"Pssst, the correct answer is {answer}")
guess = 0
turns = set_difficulty()
while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input("Make a guess: "))
        # Track the number of turns and reduce by 1 if they get it wrong
        turns = correct_guess(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
        elif guess != answer:
            print("Guess again.")



