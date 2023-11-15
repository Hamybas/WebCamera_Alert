import smtplib
import ssl
import os
from email.message import EmailMessage
import imghdr

password = "*"
username = "*"
receiver = "*"
context = ssl.create_default_context()


def send_email(path):
    email_message = EmailMessage()
    email_message["Subject"] = 'New Customer'
    email_message.set_content("We just saw a new customer")

    with open(path, 'rb') as image:
        content = image.read()

    email_message.add_attachment(content, maintype='image',
                                 subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(username, password)
    gmail.sendmail(username, receiver, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email(path="images/1.png")
