import datetime as dt
import smtplib
import pandas
import random


my_email = "314159brandon314159@gmail.com"
password = "HolyMoly123!!"

# create datetime object
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

# Ingest CSV data
raw_data = pandas.read_csv("birthdays.csv")
birthday_dict = raw_data.to_dict(orient="records")

# Letter data work
letter_list = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

for item in birthday_dict:
    if item["month"] == month and item["day"] == day:
        random_letter = random.choice(letter_list)
        with open(random_letter, "r") as letter:
            contents = letter.read()
            new_contents = contents.replace("[NAME]", item["name"])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=item["email"],
                msg=f"Subject:Happy Birthday!\n\n{new_contents}")
