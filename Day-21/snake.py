from turtle import Turtle, Screen
screen = Screen()

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DIRECTIONS = {
    "up": 90,
    "down": 270,
    "left": 180,
    "right": 0
}

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DIRECTIONS["down"]:
            self.snake_head.setheading(DIRECTIONS["up"])

    def down(self):
        if self.snake_head.heading() != DIRECTIONS["up"]:
            self.snake_head.setheading(DIRECTIONS["down"])

    def left(self):
        if self.snake_head.heading() != DIRECTIONS["right"]:
            self.snake_head.setheading(DIRECTIONS["left"])

    def right(self):
        if self.snake_head.heading() != DIRECTIONS["left"]:
            self.snake_head.setheading(DIRECTIONS["right"])
