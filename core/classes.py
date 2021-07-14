import discord
from discord.ext import commands

class Cog_Extension(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        self.join=True
        self.player=[]
        startplaying=False
        a_win_edition=0
        b_win_edition=0
        channel=0


