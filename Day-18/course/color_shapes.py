from turtle import Turtle, Screen
import random

colors = ["dark green", "coral", "blue violet", "gold", "powder blue", "yellow"]
screen = Screen()

sita = Turtle()
screen.bgcolor("black")

for side in range(3,11):
    angle = 360 / side
    print(side, angle)
    sita.pencolor(random.choice(colors))
    for _ in range(side):
        sita.fd(100)
        sita.right(angle)



screen = Screen()
screen.exitonclick()
