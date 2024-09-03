import threading
import time
import logging

from imap_service import fetch_emails
from gemini_service import get_response
from smtp_service import send_email

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def send_email_thread(header, response):
    """Sends an email in a separate thread."""
    threading.Thread(target=send_email, args=(header, response)).start()


def main():
    """Main loop to fetch emails, process them, and send responses."""
    while True:
        logging.info("Fetching emails...")
        emails = fetch_emails()
        if emails:
            logging.info(f"Found {len(emails)} new emails.")
            for email in emails:
                header = email[0]
                content = email[1]
                prompt = " ".join([header["Subject"], content.decode("utf-8")])
                logging.info(f"Processing email with subject: {header['Subject']}")
                response = get_response(prompt).text
                logging.info(f"Sending response to email...")
                send_email_thread(header, response)
        else:
            logging.info("No new emails found.")
        time.sleep(30)  # Check for new emails every 60 seconds


if __name__ == "__main__":
    main()
