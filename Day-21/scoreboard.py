from turtle import Turtle

SCOREBOARD_ALIGNMENT = "center"
SCOREBOARD_FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score = {self.score}", align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)