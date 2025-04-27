import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/your_endpoint"

SPAM_DELAY = (8, 15)  # разброс задержек между сообщениями (сек)
DIALOG_REPLIES = 2  # сколько реплик сделать
INVITE_DELAY = (600, 900)  # через сколько секунд кидать приглашение (10-15 мин)
GROUP_LINK = "https://t.me/yourgroup"
SESSIONS_FOLDER = "accounts"
MAILBASE_PATH = "mailbase.csv"
