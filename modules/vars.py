

#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "24037760"))
API_HASH = environ.get("API_HASH", "7979573314:AAH8T2v8DYu2Nihio8elxJuKpez5ZIgNlpo")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER = int(environ.get("OWNER", "7834875502"))
CREDIT = environ.get("CREDIT", "ǟʟʟ ƈʟǟֆֆɛֆ ʍօʀɛռǟ一")
AUTH_USER = os.environ.get('AUTH_USERS', '7834875502,7290128282,1184922780').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
