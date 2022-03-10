import smtplib
import datetime as dt
import pandas

my_email = "pythonguru14@gmail.com"
data = pandas.read_csv("birthday.csv")

t = dt.datetime.now()
d = t.day
m = t.month
for row, _ in data.iterrows():
    birth_day = data['day'][row]
    birth_month = data['month'][row]
    if birth_day == d and birth_month == m:
        name = data['name'][row]
        message = f"Subject:Happy Birthday {name}!\n\nI hope you have a great birthday and year ahead!"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password="Mushishi1@")
            connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=message)