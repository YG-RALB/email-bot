## Project Setup and Execution

This guide details setting up a virtual environment, managing environment variables securely, and running `script.py`.

**Prerequisites:**

- Python 3.x ([https://www.python.org/downloads/](https://www.python.org/downloads/))
- Text editor (e.g., Notepad++, Visual Studio Code)

**1. Virtual Environment Setup:**

A virtual environment isolates project dependencies, preventing conflicts with your system-wide Python installation. Here's how to create one:

- **Windows:**

  ```bash
  py -m venv venv  # Replace "venv" with your desired environment name
  ```

- **macOS/Linux:**

  ```bash
  python3 -m venv venv  # Replace "venv" with your desired environment name
  ```

**2. Activate the Virtual Environment:**

- **Windows:**

  ```bash
  venv\Scripts\activate.bat
  ```

- **macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```

Your terminal prompt will now indicate the active virtual environment (e.g., `(venv)your_username@your_machine:~/project$`).

**3. Install Project Dependencies (if applicable):**

If your project has requirements listed in a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

**4. Create a Secure `.env` File:**

To protect sensitive information like passwords from version control, create a file named `.env` in your project directory. It should contain key-value pairs (one per line) for your environment variables:
EMAIL_ADDRESS=your_email@example.com
EMAIL_PASSWORD=your_strong_password
REPLY_TO_EMAIL=another_email@example.com
IMAP_SERVER=imap.gmail.com
IMAP_PORT=993
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
GEMINI_API_KEY=your_api_key

**Important!** Never commit the `.env` file to version control systems like Git. Consider using a separate configuration management tool for more complex setup.
