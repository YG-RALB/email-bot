import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def get_response(prompt):
    response = model.generate_content(prompt)
    if response == None:
        response = "There is a violation please ephrase the mail."
    return response
