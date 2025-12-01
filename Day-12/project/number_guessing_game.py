from art import logo
import random

easy_level = 10
hard_level = 5

def get_num_tries():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return easy_level
    else:
        return hard_level

def check_guess(guess, answer, attempts):
    if guess < answer:
        print("Too low")
        return attempts - 1
    elif guess > answer:
        print("Too high")
        return attempts - 1
    else:
        print(f"You got it! The answer was {answer}")
        # return 100


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    attempts = get_num_tries()
    guess = 0
    while guess != answer:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        attempts = check_guess(guess, answer, attempts)

        if attempts == 0:
            print("You've run out of guesses.")
            return
        elif guess != answer:
            print("Guess again .")


game()