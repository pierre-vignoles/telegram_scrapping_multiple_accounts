from telethon.client.telegramclient import TelegramClient


async def init(api_id: int, api_hash: str) -> TelegramClient:
    client = TelegramClient('sessions/{}'.format(str(api_id)), api_id, api_hash)
    await client.connect()
    return client
