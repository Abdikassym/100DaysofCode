##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import random
import smtplib
import datetime as dt
import pandas

my_email = "abdikasymt@yahoo.com"
my_pass = "rktctzhfkqtthjup"

now = dt.datetime.now()
month = now.month
day = now.day

data = pandas.read_csv("birthdays.csv")
for index, row in data.iterrows():
    b_day = row["day"]
    b_month = row["month"]
    b_mail = row["email"]
    b_name = row["name"]
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", "r") as templates:
        b_day_letter = templates.read()
    b_letter = b_day_letter.replace("[NAME]", b_name)
    bday_letter = b_letter.replace("Angela", "Abdikasym")

    if b_month == month and b_day == day:
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(my_email, my_pass)
            connection.sendmail(from_addr=my_email,
                                to_addrs=b_mail,
                                msg=f"Subject:Happy Birthday, {b_name}!\n\n{bday_letter}")




