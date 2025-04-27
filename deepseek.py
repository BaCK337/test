import requests
from config import DEEPSEEK_API_KEY

DEEPSEEK_API_URL = 'https://api.deepseek.ai/generate_message'  # Убедись, что это правильный URL API

def generate_message(user_name):
    data = {
        "user_name": user_name,
        "prompt": f"Напиши персонализированное сообщение для пользователя {user_name}, чтобы пригласить его в Telegram-канал."
    }

    headers = {
        'Authorization': f'Bearer {DEEPSEEK_API_KEY}',
        'Content-Type': 'application/json'
    }

    try:
        response = requests.post(DEEPSEEK_API_URL, json=data, headers=headers)
        response.raise_for_status()  # Поднимет исключение, если код ответа не 200
        message = response.json().get('message', 'Ошибка при генерации сообщения.')
        return message
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к DeepSeek: {e}")
        return "Привет! Присоединяйся к нашему каналу!"
