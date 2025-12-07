from turtle import Turtle, Screen
import random

sita = Turtle()
screen = Screen()

def get_random_color():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

screen.colormode(255)
sita.speed("fastest")

for _ in range(int(360/5)):
    sita.color(get_random_color())
    sita.circle(100)
    sita.setheading(sita.heading() + 5)

screen.exitonclick()
