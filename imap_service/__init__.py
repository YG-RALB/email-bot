import os
from dotenv import load_dotenv
import imaplib
import email

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
IMAP_SERVER = os.getenv("IMAP_SERVER")
IMAP_PORT = int(os.getenv("IMAP_PORT"))


def fetch_emails():
    imap = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    imap.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    imap.select("INBOX")

    status, messages = imap.search(None, "UNSEEN")
    messages = messages[0].split()
    email_messages = []
    for mail_id in messages:
        _, msg = imap.fetch(mail_id, "(RFC822)")
        email_message = email.message_from_bytes(msg[0][1])
        email_header = email_message
        while email_message.is_multipart():
            email_message = email_message.get_payload(0)
        content = email_message.get_payload(decode=True)
        email_messages.append([email_header, content])
    imap.close()
    imap.logout()
    return email_messages
