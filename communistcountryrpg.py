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
    await client.change_presence(game=Game(name='the Communist Manifesto',type = 2))
    print("Online")
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.content == "karl marx":
        await client.send_message(message.channel, "is a God")
num = str()

@client.event
async def on_message(message):
    if message.content.upper().startswith('C!HELP'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Type c!pishka to add a pishka to your counter" % (userID))
    if message.content.upper().startswith('C!SAY'):
        userID = message.author.id
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s"%(" ".join(args[1:])))
    if message.content.upper().startswith('C!PISHKA'):
        userID = message.author.id
        args = message.content.split(" ")
        pishki = 0
        num = args[1]
        numm = int(num)
        lan = int(pishki)
        if lan == 0:
            lan = numm
        else:
            lan = lan + numm
        await client.send_message(message.channel, "imash %s pishki"%(lan))
        pishki = lan

client.run('NDg0NzE0MTM3MDAwMjE0NTM5.Dy9Nhw.Awsvr16cHKXdLZeK01iNZY5MxHE')
