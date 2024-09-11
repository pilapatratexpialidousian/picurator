import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("7437111119:AAGXODPNumex6CMDKAmAV8MhunrF_JRP_Fg")

PROJECT_NAME = os.getenv("Ton")

# Heroku webhook
# WEBHOOK_HOST = f"https://{PROJECT_NAME}.herokuapp.com"
# WEBHOOK_PATH = '/webhook/' + BOT_TOKEN

# Railway webhook
WEBHOOK_HOST = os.getenv("RAILWAY_PUBLIC_DOMAIN")
WEBHOOK_PATH = os.getenv("WEBHOOK_PATH")

if WEBHOOK_HOST and WEBHOOK_PATH:
    WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
else:
    WEBHOOK_URL = None

ADMINS = list(map(int, os.getenv("ADMINS", "").split(",")))
