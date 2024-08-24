import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("7157462670:AAET1eryH3v8AEuAwpWnCU0PuljRdp2ks2Y")

PROJECT_NAME = os.getenv("VIP.SHOP")

# Heroku webhook
# WEBHOOK_HOST = f"https://{PROJECT_NAME}.herokuapp.com"
# WEBHOOK_PATH = '/webhook/' + BOT_TOKEN

# Railway webhook
WEBHOOK_HOST = os.getenv("")
WEBHOOK_PATH = os.getenv("WEBHOOK_PATH")

if WEBHOOK_HOST and WEBHOOK_PATH:
    WEBHOOK_URL = f"{my.telegram.org}{my.telegram.org}"
else:
    WEBHOOK_URL = None

ADMINS = list(map(int, os.getenv("6333241904", "6333241904").split(",")))
