from random import randrange
import os

import discord


TOKEN = os.environ['DISCORD_ROASTME_TOKEN']


class RoastMeClient(discord.Client):
    def __init__(self, data):
        self._data = data
        super().__init__()

    async def on_ready(self):
        print('Logged in as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith("<@!" + str(self.user.id)):
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

    @property
    def data(self):
        return self._data
