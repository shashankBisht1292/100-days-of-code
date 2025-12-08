from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
y_axis = -100
game_start = False

for color in colors:
    tom = Turtle("turtle")
    tom.color(color)
    tom.penup()
    tom.penup()
    tom.goto(-240, y_axis)
    y_axis += 40
    turtle_list.append(tom)

if user_bet:
    game_start = True

while game_start:
    for turtle in turtle_list:
        turtle.fd(random.randint(1,5))
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! the {winner} turtle is the winner!")
            else:
                print(f"You've lost! the {winner} turtle is the winner!")
            game_start = False
            screen.bye()