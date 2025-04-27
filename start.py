import asyncio
from session_manager import load_clients
from worker import spam_worker
from database import init_db
from utils import load_targets_csv
from config import MAILBASE_PATH

async def main():
    init_db()
    load_targets_csv(MAILBASE_PATH)

    clients = await load_clients()

    tasks = []
    for client in clients:
        tasks.append(spam_worker(client))

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
