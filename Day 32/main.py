import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 3:

    with open("quotes.txt") as file:
        quotes = [line for line in file]

    message = random.choice(quotes)
    print(message)
    my_email = "pythonguru14@gmail.com"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        # TLS = Transport Layer Security, encrypts and secures the email as its being sent to avoid interception hacks.
        connection.starttls()
        connection.login(user=my_email, password="Mushishi1@")
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Motivational Quote of the Week\n\n{message}")