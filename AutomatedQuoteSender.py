# Quote Sender

import datetime as dt
import smtplib
import random

with open(file="quotes.txt") as files:
    quotes = files.readlines()

my_email = "sanjalaramesh27@gmail.com"  # smtp.gmail.com
my_pw = "pw"

now = dt.datetime.now()
if now.weekday() == 6:
    with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
        conn.starttls()
        conn.login(user=my_email, password=my_pw)
        conn.sendmail(
            from_addr=my_email,
            to_addrs="126158046@sastra.ac.in",
            msg=f"Subject:Quote\n\n{random.choice(quotes).strip()}"
        )
