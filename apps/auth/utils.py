import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from core.file_manager import FileManager


def get_random_code(email: str):
    codes = FileManager("codes").read()
    random_code = random.randint(1000, 9999)
    for code in codes:
        if code[1] == str(random_code):
            get_random_code(email=email)

    FileManager("codes").append([email,random_code])

    return random_code


def send_mail(receiver_email, body):
    sender_email = "sanjarbeksocial@gmail.com"
    password = "ajvd xsnx jowk hujh"

    subject = "Confirmation code"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            print("Code sent successfully!")

    except Exception as e:
        print(f"Failed to send email. Error: {e}")


def get_active_user():
    users = FileManager("users").read()
    for user in users:
        if user[-2]:
            return user
    return False