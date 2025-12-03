from art import logo, vs
from game_data import data
import random

def get_option():
    return random.choice(data)

def display_option(option):
    return f"{option['name']}, a {option['description']}, from {option['country']}"

def is_guess_valid(guess, options):
    if options["a"]["follower_count"] > options["b"]["follower_count"]:
        return guess == "a"
    else:
        return guess == "b"

def game():
    score = 0
    options = {}
    game_over = False

    options["a"] = get_option()

    while not game_over:
        print(logo)
        if score > 0:
            print(f"Your are right! Current score: {score}.")


        to_display_option_a = display_option(options["a"])
        print(f"Compare A: {to_display_option_a}")

        print(vs)

        options["b"] = get_option()
        to_display_option_b = display_option(options["b"])
        print(f"Against B: {to_display_option_b}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        print("\n" * 50)
        if is_guess_valid(guess, options):
            score += 1
            options["a"] = options["b"]
        else:
            game_over = True
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}.")


game()