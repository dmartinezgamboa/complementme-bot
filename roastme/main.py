from discord.ext import commands
from random import randrange
from insults import insults
import os

TOKEN = os.environ['DISCORD_ROASTME_TOKEN']
STEVEN = os.environ['STEVEN_ID']
TEST_CHANNEL = os.environ['DISCORD_TEST_CHANNEL']

bot = commands.Bot(command_prefix="/")

@bot.command()
async def roast(ctx, arg):
    await ctx.send(arg)

bot.run(TOKEN)

