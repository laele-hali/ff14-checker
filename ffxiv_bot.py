import discord
import socket
import asyncio

TOKEN = 'YOUR_BOT_TOKEN_HERE'

server_ip = "204.2.29.116"
server_port = 54993

intents = discord.Intents.default()
client = discord.Client(intents=intents)

def is_port_open(ip, port, timeout=3):
    try:
        with socket.create_connection((ip, port), timeout=timeout):
            return True
    except:
        return False

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.lower().strip() == '!check':
        status = is_port_open(server_ip, server_port)
        status_msg = f"**Halicarnassus** is {'🟢 ONLINE' if status else '🔴 OFFLINE'}"
        await message.channel.send(status_msg)

client.run(TOKEN)
