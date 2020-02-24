#!/usr/bin/env python3
from discord.ext.commands.errors import *
from discord.ext import commands
import discord

from aiohttp import ClientSession
import datetime
import asyncio

from config import TOKEN

initial_cogs = [
    'cogs.commands'
]

class Welfare(commands.AutoShardedBot):
    def __init__(self, **kwargs):
        super().__init__(command_prefix=kwargs.pop('command_prefix', ('w.','welfare.')), case_insensitive=True, **kwargs)
        self.session = ClientSession(loop=self.loop)
        self.start_time = datetime.datetime.utcnow()
        self.clean_text = commands.clean_content(escape_markdown=True, fix_channel_mentions=True)

    async def on_ready(self):
        print(f'Successfully logged in as {self.user}\nSharded to {len(self.guilds)} guilds')

        for ext in initial_cogs:
            self.load_extension(ext)
        print('Loaded Cogs')

    @classmethod
    async def setup(cls, **kwargs):
        bot = cls()
        try:
            await bot.start(TOKEN, **kwargs)
        except KeyboardInterrupt:
            await bot.close()
    
    # @commands.command()
    # async def alli(self, member:discord.Member):
    #     jailrole=get(guild.roles, name="welfare")
    #     await member.add_roles(jailrole)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(Welfare.setup())