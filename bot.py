from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import UserStatusOffline
from dotenv import load_dotenv
import os

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_STRING = os.getenv("SESSION_STRING")

MSG_UZ = os.getenv("MESSAGE_UZ", "👋 Salom! Hozir javob bera olmayman.")
MSG_RU = os.getenv("MESSAGE_RU", "👋 Привет! Сейчас не могу ответить.")
MSG_EN = os.getenv("MESSAGE_EN", "👋 Hello! I can't reply right now.")

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

@client.on(events.NewMessage(incoming=True))
async def auto_reply(event):
    if event.is_private:
        me = await client.get_me()
        full_me = await client.get_entity(me.id)
        status = full_me.status
        if isinstance(status, UserStatusOffline):
            await event.reply(f"{MSG_UZ}\n{MSG_RU}\n{MSG_EN}")

client.start()
print("✅ Avto-otvet bot ishga tushdi!")
client.run_until_disconnected()
