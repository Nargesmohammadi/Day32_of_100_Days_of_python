# import smtplib

# my_email = "appbreweryinfo@gmail.com"
# password = "wer432"
# connection = smtplib.SMTP("smtp.gmail.com")
# this line will make this connection secure.
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email,
#                    to_addrs="appbreweryinfo@gmail.com",
#                     msg="Subject:Hello\n\nThis is the body of my email")
# connection.close()
# import datetime as dt

# now method gets us current time and date:
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(year)

# date_of_birth = dt.datetime(year=1990, month=12, day=15)
# print(date_of_birth)

import smtplib
import datetime as dt
import random

MY_EMAIL = "mohammadimitra533@gmail.com"
MY_PASSWORD = ""
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:  # Monday
    with open("./Day32/quotes.txt") as quotes:
        all_quotes = quotes.readline()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # for security:
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"subject:Monday Motivation\n\n{quote}")
