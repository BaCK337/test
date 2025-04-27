import random
import asyncio
import pandas as pd
from database import add_user

async def random_delay(min_sec, max_sec):
    await asyncio.sleep(random.randint(min_sec, max_sec))

def load_targets_csv(path):
    df = pd.read_csv(path)
    for username in df['username'].dropna():
        add_user(username)
