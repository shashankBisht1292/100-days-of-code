rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

options = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
computer_choice = random.randint(0, 2)

if user_choice >= 0 and user_choice <= 2:
    print(options[user_choice])

print(f"Computer chose: {options[computer_choice]}")

if ((user_choice == 0 and computer_choice == 1)
        or (user_choice == 1 and computer_choice == 2)
        or (user_choice == 2 and computer_choice == 0)):
    print("you lose")
elif (user_choice == computer_choice):
    print("Draw, play again")
elif (user_choice > 1 or user_choice < 2):
    print("You typed an invalid number, Ypu lose!")
else:
    print("you Win !!!")
