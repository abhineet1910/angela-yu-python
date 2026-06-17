##################### Hard Starting Project ######################
import pandas as pd
import datetime as dt
import smtplib
import random

my_email = "testingmail1910@gmail.com"
my_password = "pgvihylddsxwxqyb"




data = pd.read_csv('birthdays.csv')
birthdays = data.to_dict('records')
birthday_dict = {(person["month"], person["day"]): person
for person in birthdays}
print(birthday_dict)
def load_letter(path):
    with open(path) as file:
        return file.read()

l1 = load_letter('letter_templates/letter_1.txt')
l2 = load_letter('letter_templates/letter_2.txt')
l3 = load_letter('letter_templates/letter_3.txt')
random_letter = random.choice([l1,l2,l3])
print(random_letter)






now = dt.datetime.now()
today_day = now.day
today_month = now.month
today_tuple = (today_month, today_day)
if today_tuple in birthday_dict:

    person = birthday_dict[today_tuple]

    name = person["name"]
    email = person["email"]

    letter = random_letter.replace("[NAME]", name)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()

        connection.login(
            user=my_email,
            password=my_password
        )
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:HAPPY BIRTHDYA\n\n{letter}"
        )



