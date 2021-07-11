import discord
from discord.ext import commands

class Cog_Extension(commands.Cog):
    def __init__(self,bot):
        self.people=0
        self.bot=bot
        self.player=[]
