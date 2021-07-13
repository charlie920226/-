import discord
from discord.ext import commands
import json
from core.classes import Cog_Extension
from cmds.start import start

with open ("background_setting.json",'r',encoding="utf8") as jfile:
    jdata=json.load(jfile)

class king(Cog_Extension):
    @commands.command()
    async def set(self,ctx):
        if self.startplaying==True:
            content=ctx.message.content
            a=content[5]
            self.team=content[-1]
            self.king_color=content[6:-1]
            if self.team=="a":
                self.a_win_edition=int(a)+6
                self.b_win_edition=14-self.a_win_edition
                await ctx.channel.send(F"王牌花色是{self.king_color}\na隊要拿{self.a_win_edition}墩，b隊要拿{self.b_win_edition}墩")
            elif self.team=="b":
                self.b_win_edition=int(a)+6
                self.a_win_edition=14-self.b_win_edition
                await ctx.channel.send(F"王牌花色是{self.king_color}\na隊要拿{self.a_win_edition}墩，b隊要拿{self.b_win_edition}墩")
            self.startplaying=False
            self.play=True
            self.channel=ctx.channel
            await start.game(self)
           
def setup(bot):
    bot.add_cog(king(bot))      

