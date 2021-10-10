from discord.ext import commands
from random import randrange
import insults
import os

TOKEN = os.environ['DISCORD_ROASTME_TOKEN']

def createInsult(user):
    includeAdverb = bool(randrange(0,2))
    adjective = insults.adjectives[randrange(0, len(insults.adjectives))]
    if (includeAdverb):
        adverb = insults.adverbs[randrange(0, len(insults.adverbs))]
        return user + " is " + adverb + " " + adjective
    else:
        return user + " is " + adjective
   
bot = commands.Bot(command_prefix="/")

@bot.command()
async def roast(ctx, arg):
    print(arg)
    if (arg == 'me'):
        await ctx.send("You're garbage.")
    if (arg.startswith("<@", 0)):
        await ctx.send(createInsult(arg))

bot.run(TOKEN)

