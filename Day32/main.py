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
import datetime as dt

# now method gets us current time and date:
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(year)

date_of_birth = dt.datetime(year=1990, month=12, day=15)
print(date_of_birth)
