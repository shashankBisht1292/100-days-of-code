##################### Extra Hard Starting Project ######################
import smtplib
import pandas as pd
import random
from datetime import datetime

LETTER_TEMPLATES = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
MY_EMAIL = "shashankbishtgehu@gmail.com"
PASSWORD = "lvddhinwkbutrtvn"


def send_birthday_email(message, email):
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email,
            msg=f"Subject:Happy Birthday !!!\n\n{message}"
        )

def get_birthday_template(name, email):
    template = random.choice(LETTER_TEMPLATES)
    with open(f"./letter_templates/{template}", "r") as file:
        content = file.read().replace("[NAME]", name)
        send_birthday_email(message=content, email=email)

def check_any_birthday():
    data = pd.read_csv("./birthdays.csv")
    data_dict = data.to_dict("records")
    now = datetime.now()
    today = (now.month, now.day)
    # month = now.month
    # today = now.day
    for entry in data_dict:
        if entry.get("month") == today[0] and entry.get("day") == today[1]:
            get_birthday_template(name=entry.get("name"), email=entry.get("email"))

check_any_birthday()




