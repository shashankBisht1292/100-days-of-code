from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = False
user = screen.textinput("", "Player Name")
if user != "":
    scoreboard.read_high_score(user)
    game_is_on = True

screen.listen()
screen.onkey(snake.up ,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move(snake.start_moving)

    #Detect food collision
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    #Detect wall collision
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() < -280 or snake.snake_head.ycor() > 280:
        snake.reset()
        scoreboard.reset(user)

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            snake.reset()
            scoreboard.reset(user)

screen.exitonclick()