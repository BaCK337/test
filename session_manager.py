import os
from telethon import TelegramClient
from config import API_ID, API_HASH, SESSIONS_FOLDER

async def load_clients():
    clients = []
    for session_file in os.listdir(SESSIONS_FOLDER):
        if session_file.endswith('.session'):
            path = os.path.join(SESSIONS_FOLDER, session_file)
            client = TelegramClient(path, API_ID, API_HASH)
            await client.start()
            clients.append(client)
    return clients
