import pandas
import smtplib
import datetime as dt
import random

with open("letter_templates/letter_1.txt") as file:
    letter1 = file.read()
with open("letter_templates/letter_2.txt") as file:
    letter2 = file.read()
with open("letter_templates/letter_3.txt") as file:
    letter3 = file.read()

date = dt.datetime.now()
today = date.day

my_email = "test@gmail.com" # NOT REAL EMAIL, MUST USE OWN
password = "test@" # NOT REAL PASSWORD


letters_list = [letter1, letter2, letter3]
frame = pandas.read_csv("birthdays.csv")
name_list = frame.name.to_list()
if today == 19:
    name = "Gabriel"
    chosen_letter = random.choice(letters_list).replace("[NAME]", name)
    with open("letter_templates/Gabriel_letter.txt", "w") as new_file:
        card = new_file.write(chosen_letter)
    with open("letter_templates/Gabriel_letter.txt") as new_file:
        data2 = new_file.read()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Happy Birthday {name}!\n\n{data2}")
    print("Your message was sent!")



