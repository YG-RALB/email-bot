from fastapi import FastAPI
from imap_service import fetch_emails
from gemini_service import get_response
from smtp_service import send_email

app = FastAPI()


@app.get("/")
async def root():
    emails = fetch_emails()

    for email in emails:
        header = email[0]
        content = email[1]
        prompt = " ".join([header["Subject"], content.decode("utf-8")])
        response = get_response(prompt).text
        send_email(header, response)
        return response
