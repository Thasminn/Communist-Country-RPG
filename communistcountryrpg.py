import discord
import asyncio
import time
import os
from discord.ext import commands
from discord import Game
from itertools import cycle

Client = discord.client
client = commands.Bot(command_prefix = 'c!')
Clientdiscord = discord.Client()

client.remove_command('help')
@client.event
async def on_ready():
    await client.change_presence(game=Game(name='the screams of GULAG',type = 2))
    print("Online")
    print(f"Logged in as {client.user}")

@client.command()
async def sugondese():
    await client.say("```Sugondese nuts!```")

@client.command()
async def add(*args):
    output = int(0)

    for word in args:
        output += int(word)

    await client.say('The result is %s' %(output))

@client.command()
async def help():
    embed = discord.Embed(
    title = 'CommunistCountryRPG Bot - Help',
    decription = 'Settings',
    colour = discord.Colour.blue())
    embed.set_footer(text='CommunistCountryRPG - Thasminn#7478 - 2019')
    embed.set_thumbnail(url = 'https://i.imgur.com/FvyoMVp.jpg')
    embed.add_field(name='**Add numbers**',value='**Use c!add <number> <number> \n You can add as many numbers as you want**', inline=False)
    embed.add_field(name='**:speech_balloon: Make the bot say something**',value='Use c!say <sentence>', inline=False)
    embed.add_field(name='**:speaking_head: Send an anonimous message to a user**',value='Use c!anon <user> <message>', inline=False)
    embed.add_field(name='**:x: Clear messages**',value='Use c!clear <number>', inline=False)
    embed.add_field(name='**:peanuts: Sugondese**',value='Use c!sugondese', inline=False)
    await client.say(embed=embed)

@client.command()
async def say(*num):
    phr = ''
    for word in num:
        phr += word
        phr += ' '
    await client.say(phr)

@client.command(pass_context=True)
async def anon(ctx, member: discord.Member, *msg):
    await client.send_message(member, "Sent by an anonimous user:")
    await client.send_message(member, " ".join(msg[0:]))
    await client.say("Anonimous message has been sent")
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit = int(2)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('%s Messages deleted' %(amount))

@client.command(pass_context=True)
async def clear(ctx, amount = 100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit = int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('%s Messages deleted' %(amount))

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

client.run('NDg0NzE0MTM3MDAwMjE0NTM5.Dy9Nhw.Awsvr16cHKXdLZeK01iNZY5MxHE')
