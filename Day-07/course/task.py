#hangman - basic
word_list = ["aardvark", "baboon", "camel"]

import random
choice = random.choice(word_list)
print(choice)
user_guess = input("Enter your guess: ").lower()
for letter in choice:
    if user_guess == letter:
        print("Right")
    else:
        print("Wrong")

#hangman - step-2
import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder =''
for word in chosen_word:
    placeholder += "_"
print(placeholder)

guess = input("Guess a letter: ").lower()

display = ""
for letter in chosen_word:
    if letter == guess:
        display += guess
    else:
        display += "_"

print(display)

#hangman - step-3
import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
guessed_words = []
while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""


    for letter in chosen_word:
        if letter == guess:
            display += letter
            guessed_words.append(letter)
        elif letter in guessed_words:
            display += letter
        else:
            display += "_"
    print(display)

    if "_" not in display:
        game_over = True
        print("You win!")

#hangman - step-4
import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]

#  Set 'lives' to equal 6.
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in correct_letters:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            game_over = True
            print("You lose.")

    if "_" not in display:
        game_over = True
        print("You win.")

