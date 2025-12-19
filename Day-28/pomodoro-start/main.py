import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    heading.config(text="Timer", font=(FONT_NAME, 35, "normal"), bg=YELLOW, fg=GREEN)
    checkmark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        heading.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        heading.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        heading.config(text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)
    if minutes < 10:
        minutes = "0" + str(minutes)
    sec = count % 60
    if sec < 10:
        sec = "0" + str(sec)
    canvas.itemconfig(timer_text, text=f"{minutes}:{sec}")
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✅"
        checkmark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.configure(padx=100, pady=50, bg=YELLOW)

heading = Label(text="Timer", font=(FONT_NAME, 35, "normal"), bg=YELLOW, fg=GREEN)
heading.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 100, image=tomato_img)
timer_text = canvas.create_text(100, 120, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

Button(text="Start", command=start_timer, highlightthickness=0, pady=2).grid(row=2, column=0)

checkmark = Label(text="", bg=YELLOW, fg=GREEN)
checkmark.grid(row=3, column=1)

Button(text="Reset", command=reset_timer, highlightthickness=0, pady=2).grid(row=2, column=2)



window.mainloop()