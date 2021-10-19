import json
import os
from random import randrange

import discord


TOKEN = os.environ['DISCORD_ROASTME_TOKEN']


def load_data():
    f = open('data.JSON',)
    data = json.load(f)
    f.close()
    return data


class RoastMeClient(discord.Client):
    def __init__(self, data):
        self._data = data
        super().__init__()

    async def on_ready(self):
        print('Logged in as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == client.user:
            return
        if message.content.startswith("<@!" + str(client.user.id)):
            await message.channel.send(
                f'You\'re dog sh*t. <@{message.author.id}>')

    def create_insult(self, user):
        randomIndex = randrange(0, len(self.data["adjectives"]))
        adjective = self.data["adjectives"][randomIndex]
        include_adverb = bool(randrange(0, 2))

        if include_adverb:
            randomIndex = randrange(0, len(self.data["adverbs"]))
            adverb = self.data["adverbs"][randomIndex]
            return user + " is " + adverb + " " + adjective
        else:
            return user + " is " + adjective

if __name__ == "__main__":
    data = load_data()
    client = RoastMeClient(data)
    client.run(TOKEN)

