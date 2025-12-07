from turtle import Turtle, Screen
import random

colors = ["dark green", "coral", "blue violet", "gold", "powder blue", "yellow"]
direction = [0, 90, 180, 270]

screen = Screen()
sita = Turtle()
screen.colormode(255)

sita.pensize(15)
sita.speed("fastest")

def get_random_color():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

for _ in range(200):
    sita.pencolor(get_random_color())
    sita.forward(30)
    sita.setheading(random.choice(direction))



screen = Screen()
screen.exitonclick()
