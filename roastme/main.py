import discord
from random import randrange
from insults import insults

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$roastme'):
        await message.channel.send(insults[randrange(len(insults)-1)])
    
    if message.content.startswith('$roastSteven'):
        await message.channel.send('@Steven (Chubs) is a c*nt')

client.run('ODkyNTYwODEwOTk0NDQ2NDA2.YVOsCA.S4O4bL0vuxaXJqiemwAFGoP8Eg8')