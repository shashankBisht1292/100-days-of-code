from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()

move_space = 10

def forward():
    tom.fd(move_space)

def backward():
    tom.bk(move_space)

def counter_clockwise():
    tom.setheading(tom.heading() + 10)

def clockwise():
    tom.setheading(tom.heading() - 10)

def clear():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()

screen.onkey(forward, 'w')
screen.onkey(backward, 's')
screen.onkey(counter_clockwise, 'a')
screen.onkey(clockwise, 'd')
screen.onkey(clear, 'c')
screen.listen()

screen.exitonclick()
