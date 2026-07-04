import os
import smtplib

import dotenv
from email.message import EmailMessage



class SENDMAIL:

    def __init__(self):
        dotenv.load_dotenv()
        self.my_email = os.environ.get("MY_EMAIL")
        self.my_password = os.environ.get("MY_PASSWORD")
        print(f"Email: {self.my_email}")
        print(f"Password: {self.my_password}")



    def send_email(self, email, email_body):
        msg = EmailMessage()
        msg["Subject"] = "FOUND LOWEST PRICE"
        msg["From"] = self.my_email
        msg["To"] = email
        msg.set_content(email_body)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(self.my_email, self.my_password)
            connection.send_message(msg)

