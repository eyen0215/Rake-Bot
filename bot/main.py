from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response
import asyncio
#test
# LOAD  TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN: Final[str] = ""

# BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)


#  MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return
    try:

        if user_message[0] == "!":
            if user_message[1] == '?':
                user_message = user_message[1:]
                is_private = True
            else:
                is_private = False

            user_message = user_message[1:]
            response: str = get_response(user_message)
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


#HANDLING THE STARTUP FOR OUR BOT
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


#HANDLING INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


#MAIN ENTRY POINT
def main() -> None:
    client.run(token=TOKEN)



if __name__ == '__main__':
    main()
