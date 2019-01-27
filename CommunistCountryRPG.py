import discord
import asyncio
import time
import os
from discord.ext import commands
from discord import Game

Client = discord.client
client = commands.Bot(command_prefix = 'c!')
Clientdiscord = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(game=Game(name='Bot',type = 1))
    print("Online")
    print(f"Logged in as {client.user}")
        
client.run('NDg0NzE0MTM3MDAwMjE0NTM5.Dy9Nhw.Awsvr16cHKXdLZeK01iNZY5MxHE')
