import google.generativeai as genai

API_KEY = "AIzaSyD_F4FyJwm2I3eXAXE0Z1gnDis1TIjHB6A"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def get_response(prompt):
    response = model.generate_content(prompt)
    return response
