##################### Extra Hard Starting Project ######################
import smtplib
from datetime import datetime
import pandas
import random


MY_EMAIL = "mohammadimitra533@gmail.com"
MY_PASSWORD = ""
# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("./Day32/birthdays.csv")
birthday_dic = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv
if today_tuple in birthday_dic:
    birthday_person = birthday_dic[today_tuple]
    file = f"./Day32/letter_{random.randint(1, 3)}.txt"
    with open(file) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])  # save as contents for change the name and
        # doesn't get error.
        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"],
                                msg=f"subject:Happy Birthday\n\n{contents}")


