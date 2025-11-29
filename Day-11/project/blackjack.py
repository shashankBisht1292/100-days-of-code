from art import logo
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    return sum(cards)

def compare_score(user_score, computer_score):
    if user_score == computer_score:
        return "DRAW !!!"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    print(logo)
    u_cards = []
    c_cards = []
    u_score = 0
    c_score = 0
    is_game_over = False



    for _ in range(2):
        u_cards.append(deal_card())
        c_cards.append(deal_card())

    while not is_game_over:
        u_score = calculate_score(u_cards)
        c_score = calculate_score(c_cards)

        print(f"Your cards: {u_cards}, current score: {u_score}")
        print(f"Computer's cards: [{c_cards[0]}, X]")

        if u_score > 21:
            is_game_over = True
        else:
            choice = input("Type 'y' to get another card or 'n' to pass: ").lower()
            if choice == "y":
                u_cards.append(deal_card())
            else:
                is_game_over = True

    print(f"Your final hand: {u_cards}, final score: {u_score}")
    print(f"Computer final hand: {c_cards}, final score: {c_score}")

    print(compare_score(u_score, c_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()