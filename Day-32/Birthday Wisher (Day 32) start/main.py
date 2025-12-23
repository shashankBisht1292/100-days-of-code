import smtplib
import datetime as dt
import random

MY_EMAIL = "shashankbishtgehu@gmail.com"
PASSWORD = "lvddhinwkbutrtvn"

def send_mail(message):
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="somilfosters@gmail.com",
            msg=f"Subject:Quote of the day\n\n{message}"
        )

week_day = dt.datetime.now().weekday()
if week_day == 1:
    with open("./quotes.txt", "r") as file:
        quotes = file.readlines()
        send_mail(random.choice(quotes))
