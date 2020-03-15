import os

import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('STEVE_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "throw" in message.content.lower() or "yeet" in message.content.lower():
        await message.channel.send("***NO PROJECTILES***")
        print("stop throwing stuff")
    elif "shut up" in message.content.lower() or "shutup" in message.content.lower():
        await message.channel.send("**NO SHUT UP** *ding*")
    elif "fuck off" in message.content.lower():
        await message.channel.send("no fuck off 3 1/2 nice things")
        

client.run(token)
