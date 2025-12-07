# import colorgram
# colors = colorgram.extract('image.jpg', 30)
# new_list = []
# for color in colors:
#     new_list.append((color.rgb.r, color.rgb.g, color.rgb.b))
# print(new_list)

import turtle as t
import random

t.colormode(255)
tim = t.Turtle()

tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(185, 162, 132), (129, 92, 70), (79, 93, 118), (147, 161, 180), (179, 152, 162), (210, 207, 135), (28, 35, 49), (119, 79, 92), (54, 24, 33), (46, 25, 19), (147, 170, 154), (86, 107, 91), (161, 156, 60), (113, 31, 43), (168, 107, 98), (27, 37, 33), (51, 58, 92), (212, 179, 189), (110, 123, 155), (117, 37, 27), (161, 107, 118), (219, 178, 170), (177, 202, 186), (180, 187, 209), (106, 144, 116), (67, 75, 35)]
tim.setheading(225)
tim.fd(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(10, random.choice(color_list))
    tim.fd(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()