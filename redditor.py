# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "/s" in message.content.lower() or "r/" in message.content.lower() or "reddit" in message.content.lower():
        await message.channel.send(file=discord.File('redditor.jpg'))
        print("REDDITOR DETECTED")

client.run(token)
