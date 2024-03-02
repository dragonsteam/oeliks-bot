import os
from dotenv import load_dotenv
from telethon import TelegramClient, events
from telethon.tl import functions
from telethon.sync import Button

load_dotenv()

TG_API_ID = os.getenv("TG_API_ID")
TG_API_HASH = os.getenv("TG_API_HASH")
TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")


# Create a TelegramClient instance
client = TelegramClient('bot_session', TG_API_ID, TG_API_HASH).start(bot_token=TG_BOT_TOKEN)

# Register an event handler for when the bot receives the /start command
@client.on(events.NewMessage(pattern='/start2'))
async def start2(event):
    # Respond with "Hello, world!" when the /start command is received
    await event.respond('Hello, world!')

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    # Request the user's phone number
    await event.respond('Please provide your phone number', buttons=[Button.request_phone(text='Send my number')])

@client.on(events.NewMessage())
async def contact(event):
    user_id = event.message.peer_id.user_id
    if event.message.media:
        contact_user_id = event.message.media.user_id
        # check if user really send his number
        if contact_user_id == user_id:
            print("number recieved")
            print(event.message.media.phone_number)
        else:
            await event.respond('This is not your number')

# Run the bot
client.run_until_disconnected()
