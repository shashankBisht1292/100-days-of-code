from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
selected_word = {}
words_dict = {}
show_answer_timer = ''

try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/french_words.csv")
    words_dict = original_data.to_dict(orient="records")
else:
    words_dict = data.to_dict(orient="records")


#read data
def next_card():
    global selected_word, show_answer_timer
    window.after_cancel(show_answer_timer)
    selected_word = random.choice(words_dict)
    canvas.itemconfig(title_txt, text="French", fill="black")
    canvas.itemconfig(word_txt, text=selected_word["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    show_answer_timer = window.after(3000, show_answer)


def show_answer():
    global selected_word
    canvas.itemconfig(title_txt, text="English", fill="white")
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(word_txt, text=selected_word["English"], fill="white")

def is_known():
    global words_dict
    words_dict.remove(selected_word)
    print(len(words_dict))
    data = pd.DataFrame(words_dict)
    data.to_csv('./data/words_to_learn.csv', index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.configure(pady=50, padx=50, bg=BACKGROUND_COLOR)

show_answer_timer = window.after(3000, show_answer)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back = PhotoImage(file="./images/card_back.png")
card_front= PhotoImage(file="./images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

title_txt = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_txt = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

wrong_image = PhotoImage(file="./images/wrong.png")
Button(image=wrong_image, command=next_card, borderwidth=0, highlightthickness=0).grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
Button(image=right_image, command=is_known, borderwidth=0, highlightthickness=0).grid(row=1, column=1)

next_card()

window.mainloop()
