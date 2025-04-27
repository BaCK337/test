from deepseek import generate_message
from config import SPAM_DELAY, DIALOG_REPLIES, INVITE_DELAY, GROUP_LINK
from utils import random_delay
from database import get_pending_users, update_status
from telethon.errors import FloodWaitError
import asyncio

async def spam_worker(client):
    while True:
        targets = get_pending_users(limit=10)
        if not targets:
            print(f"[{client.session.filename}] База пуста!")
            await asyncio.sleep(60)
            continue

        for username in targets:
            try:
                print(f"[{client.session.filename}] Пишем пользователю @{username}")
                await random_delay(*SPAM_DELAY)

                for i in range(DIALOG_REPLIES):
                    msg = await generate_message(f"Сообщение {i+1} для начала общения")
                    await client.send_message(username, msg)
                    print(f"[{client.session.filename}] Реплика {i+1} для @{username}")

                    await random_delay(*SPAM_DELAY)

                    # Ждем ответ
                    history = await client.get_messages(username, limit=5)
                    if any(m.from_id.user_id == (await client.get_me()).id for m in history):
                        # Только наши сообщения
                        continue
                    else:
                        print(f"[{client.session.filename}] @{username} ответил!")
                        update_status(username, "replied")
                        break
                else:
                    # Нет ответа после всех реплик
                    print(f"[{client.session.filename}] Нет ответа от @{username}, готовим инвайт")
                    await random_delay(*INVITE_DELAY)
                    invite_text = await generate_message(f"Приглашение в группу {GROUP_LINK}")
                    await client.send_message(username, f"{invite_text}\n\n{GROUP_LINK}")
                    update_status(username, "invited")

            except FloodWaitError as e:
                print(f"[{client.session.filename}] FloodWait: ждем {e.seconds} сек")
                await asyncio.sleep(e.seconds + 5)
            except Exception as e:
                print(f"[{client.session.filename}] Ошибка при отправке @{username}: {e}")
                update_status(username, "error")
                continue
