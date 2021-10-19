import json
import os
from random import randrange

from discord.ext import commands


TOKEN = os.environ['DISCORD_ROASTME_TOKEN']
bot = commands.Bot(command_prefix="/")


def load_data():
    f = open('data.JSON',)
    data = json.load(f)
    f.close()
    return data


data = load_data()


def create_insult(user):
    adjective = data["adjectives"][randrange(0, len(data["adjectives"]))]
    include_adverb = bool(randrange(0, 2))
    if include_adverb:
        adverb = data["adverbs"][randrange(0, len(data["adverbs"]))]
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

