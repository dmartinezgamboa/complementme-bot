import os
from random import randrange

from discord.ext import commands

import insults


TOKEN = os.environ['DISCORD_ROASTME_TOKEN']
bot = commands.Bot(command_prefix="/")


def create_insult(user):
    adjective = insults.adjectives[randrange(0, len(insults.adjectives))]
    include_adverb = bool(randrange(0, 2))
    if include_adverb:
        adverb = insults.adverbs[randrange(0, len(insults.adverbs))]
        return user + " is " + adverb + " " + adjective
    else:
        return user + " is " + adjective


@bot.command()
async def roast(context, arg):
    print(arg)
    if (arg == 'me'):
        await context.send("You're garbage.")
    if (arg.startswith("<@", 0)):
        await context.send(create_insult(arg))


if __name__ == "__main__":
    bot.run(TOKEN)
