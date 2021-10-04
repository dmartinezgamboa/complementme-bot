import discord
from random import randrange
from insults import insults
import os

TOKEN = os.environ['DISCORD_ROASTME_TOKEN']
STEVEN = os.environ['STEVEN_ID']
TEST_CHANNEL = os.environ['DISCORD_TEST_CHANNEL']

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    channel = client.get_channel(TEST_CHANNEL) #test channel ID
    await channel.send("I'm online b*tches!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('&roastmeCommands'):
        await message.channel.send(
          "Do I really need to tell you everything? Here you go:\n \
          $roastme - for randomized\
          ")

    if message.content.startswith('$roastme'):
        await message.channel.send(insults[randrange(len(insults)-1)])
    
    if message.content.startswith('$roastSteven'):
        await message.channel.send('<@!%s> is a c*nt.'%STEVEN)

client.run(TOKEN)