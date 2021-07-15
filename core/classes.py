import discord
from discord.ext import commands

class Cog_Extension(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        self.join=True
        self.a_win_edition=0
        self.b_win_edition=0
        self.channel=0
        startplaying=False
        self.win_count_start=False
        self.counter=-1


