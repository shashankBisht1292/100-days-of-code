from turtle import Turtle, Screen

sita = Turtle()
sita.shape("turtle")
sita.color("red")

for _ in range(4):
    sita.forward(100)
    sita.right(90)

screen = Screen()
screen.exitonclick()
