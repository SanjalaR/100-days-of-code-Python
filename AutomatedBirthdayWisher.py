##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import csv
import pandas as pd
import random
import smtplib
import datetime as dt

MY_EMAIL = "sanjalaramesh27@gmail.com"
MY_PW = "pw"

dobs = pd.read_csv("birthdays.csv")
dob_dict = dobs.to_dict(orient="records")
print(dob_dict)

now = dt.datetime.now()
for i in dob_dict:
    if i["month"] == now.month and i["day"] == now.day:
        files = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
        send = random.choice(files)
        with open(file=f"letter_templates/{send}") as file:
            content = file.read()
            content = content.replace("Angela", "Sanjala")
            content = content.replace("[NAME]", i["name"])
        with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
            conn.starttls()
            conn.login(user=MY_EMAIL, password=MY_PW)
            conn.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=i["email"],
                msg=f"Subject:Happy Birthday!\n\n{content}"
            )
