import asyncio
import nest_asyncio
import sys
from telethon.client.telegramclient import TelegramClient

from function_init import init
from functions import add_members_to_group, logo
from myconfig import *

sys.setrecursionlimit(10000)
nest_asyncio.apply()


async def front(client: TelegramClient, username: str):
    await add_members_to_group(client, username)


async def main():
    logo()
    for i in range(0, split_by):
        for session in api_list:
            client = await init(session['api_id'], session['api_hash'])
            async with client:
                loop = asyncio.get_event_loop()
                loop.run_until_complete(front(client, session['username']))
                await client.disconnect()
    print("\n\nEND")

if __name__ == '__main__':
    asyncio.run(main())
