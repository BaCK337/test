import aiohttp
from config import DEEPSEEK_API_KEY, DEEPSEEK_API_URL

async def generate_message(prompt: str) -> str:
    async with aiohttp.ClientSession() as session:
        headers = {
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        }
        json_data = {
            "prompt": prompt,
            "temperature": 0.7,
            "max_tokens": 200
        }
        async with session.post(DEEPSEEK_API_URL, headers=headers, json=json_data) as response:
            result = await response.json()
            return result.get('reply', 'Привет! Рад знакомству :)')
