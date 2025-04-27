import asyncio
from telethon import TelegramClient
from telethon.tl.types import PeerUser
from telethon.sessions import StringSession
from deepseek import generate_message
from db import get_users, update_user_status, insert_user
from config import TELEGRAM_ACCOUNTS


# Функция для отправки сообщений
async def send_message(client, user_id, message):
    try:
        await client.send_message(user_id, message)
        print(f"Сообщение отправлено {user_id}")
    except Exception as e:
        print(f"Ошибка при отправке: {e}")

# Функция для обработки одного аккаунта
async def handle_account(account, users):
    client = TelegramClient(StringSession(), account['api_id'], account['api_hash'])
    await client.start()

    for user in users:
        user_id = user[1]  # Telegram ID
        user_name = user[2]  # Имя пользователя или email (если это нужно)

        # Генерация сообщения через DeepSeek
        message = generate_message(user_name)

        # Отправляем сообщение
        await send_message(client, user_id, message)

        # Обновляем статус пользователя
        update_user_status(user[0], 'message_sent')

    await client.disconnect()

# Основная функция
async def main():
    users = get_users()  # Получаем список пользователей из базы данных

    tasks = []
    for account in TELEGRAM_ACCOUNTS:
        tasks.append(handle_account(account, users))  # Создаём задачу для каждого аккаунта

    await asyncio.gather(*tasks)  # Запускаем задачи одновременно

# Запуск бота
if __name__ == "__main__":
    asyncio.run(main())
