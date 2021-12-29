import os

import discord

from praise import praise_tagged_user

TOKEN = os.environ['DISCORD_PRAISEME_TOKEN']


class PraiseMeClient(discord.Client):
    def __init__(self, praises_parts, praises_full):
        self._praises_parts = praises_parts
        self._praises_full = praises_full
        super().__init__()

    async def on_ready(self):
        print(f"Logged in as {self.user}!")

    async def on_message(self, message):
        if message.author == self.user:
            return
        if self.user in message.mentions:
            user = self.find_tagged_user(message.author, message.mentions)
            praise = praise_tagged_user(
                user_id=user.id, 
                praises_pieces=self.praises_parts, 
                praises_full=self.praises_full
                )
            await message.channel.send(praise)

    def find_tagged_user(self, message_author, mentions):
        if len(mentions) == 1:
            return message_author
        for user in mentions:
            if user != self.user:
                return user

    @property
    def praises_parts(self):
        return self._praises_parts

    @property
    def praises_full(self):
        return self._praises_full
