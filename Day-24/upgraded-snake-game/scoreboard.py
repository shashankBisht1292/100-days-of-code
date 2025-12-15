from turtle import Turtle

SCOREBOARD_ALIGNMENT = "center"
SCOREBOARD_FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score} Highscore = {self.high_score}", align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self, user_name):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score(user_name)
        self.score = 0
        self.update_score()

    def read_high_score(self, user_name):
        with open("data.txt", "r") as file:
            for line in file:
                clean_line = line.strip()
                key_value_pair = clean_line.split('=')
                key = key_value_pair[0]
                value_str = key_value_pair[1]
                if key == user_name:
                    self.high_score = int(value_str)
                    self.update_score()



    def write_high_score(self, user_name):
        updated_lines = []
        user_found = False
        with open("data.txt", "r") as file:
            for line in file:
                clean_line = line.strip()
                key_value_pair = clean_line.split('=')
                key = key_value_pair[0]
                if key == user_name:
                    user_found = True
                    new_line = f"{key}={self.high_score}\n"
                    updated_lines.append(new_line)
                else:
                    updated_lines.append(line)

        with open("data.txt", "w") as file:
            if not user_found:
                updated_lines.append(f"{user_name}={self.high_score}")
            file.writelines(updated_lines)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=SCOREBOARD_ALIGNMENT, font=SCOREBOARD_FONT)