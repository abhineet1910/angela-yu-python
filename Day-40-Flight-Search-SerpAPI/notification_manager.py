import os
import smtplib

import dotenv
from twilio.rest import Client

# Using a .env file to retrieve the phone numbers and tokens.
dotenv.load_dotenv()
class NotificationManager:

    def __init__(self):
        self.my_email = os.environ["SMTP_EMAIL"]
        self.my_password = os.environ["SMTP_PASSWORD"]
        self.client = Client(os.environ['TWILIO_SID'],os.environ["TWILIO_AUTH_TOKEN"])
        self.connection = smtplib.SMTP('smtp.gmail.com', 587)

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
            body=message_body,
            to=os.environ["TWILIO_VERIFIED_NUMBER"]
        )
        # Prints if successfully sent.
        print(message.sid)
        print(message.status)

    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
        )
        print(message.sid)
        print(message.status)
    def send_email(self,email_list,email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(user=self.my_email, password=self.my_password)
        for email in email_list:
            self.connection.sendmail(
                from_addr=self.my_email,
                to_addrs=email,
                msg=f"Subject:New Low Price Flight!\n\n{email_body}"
            )

