from email.mime.text import MIMEText
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()


def send_email(email_message, response):
    # Extract subject and sender
    subject = email_message.get("Subject")
    sender = email_message.get("From")
    message_id = email_message.get("Message-ID")

    # Create the reply message
    reply_message = MIMEText(response, _charset="utf-8")
    reply_message["Subject"] = subject
    reply_message["From"] = os.getenv("EMAIL_ADDRESS")
    reply_message["To"] = sender
    reply_message["In-Reply-To"] = message_id
    reply_message["References"] = message_id

    # Send the reply using SMTP
    try:
        smtp = smtplib.SMTP(os.getenv("SMTP_SERVER"), int(os.getenv("SMTP_PORT")))
        smtp.starttls()
        smtp.login(os.getenv("EMAIL_ADDRESS"), os.getenv("EMAIL_PASSWORD"))
        smtp.sendmail(os.getenv("EMAIL_ADDRESS"), sender, reply_message.as_string())
        smtp.quit()
        return True
    except Exception as e:
        print(e)
        return False
