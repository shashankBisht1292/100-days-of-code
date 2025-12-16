from turtle import Turtle, Screen
import pandas as pd

IMAGE = 'blank_states_img.gif'

screen = Screen()
screen.title("U.S. States Game")
screen.bgpic(IMAGE)

states_data = pd.read_csv("./50_states.csv")
all_states = states_data.state.to_list()

guessed_states = []
total_states = 50

while len(guessed_states) < total_states:
    user_answer = screen.textinput(title = f"{len(guessed_states)}/{total_states} States Correct", prompt= "What's another state's name?").title()

    if user_answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        print(missing_states)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("./states_to_learn.csv")
        break
    if user_answer in all_states:
        guessed_states.append(user_answer)
        turtle = Turtle()
        turtle.hideturtle()
        turtle.penup()
        answer_state = states_data[states_data.state == user_answer]
        turtle.goto(answer_state.x.item(), answer_state.y.item())
        turtle.write(answer_state.state.item())

#states_to_learn.csv
# print( pd.DataFrame.from_dict(not_guessed_states))

