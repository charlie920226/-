import discord
from discord.ext import commands
import json
from core.classes import Cog_Extension
from cmds.發牌 import 發牌
import random
with open ("background_setting.json",'r',encoding="utf8") as jfile:
    jdata=json.load(jfile)

class 人數(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content=="來打牌":
            self.people+=1
            self.player.append(msg.author)
            await msg.channel.send(F"目前有{self.people}人")
            if self.people==2:
                發牌.distribution(self)
        elif msg.content=="不打了":
            self.people-=1
            self.player.remove(msg.author)
            await msg.channel.send(F"目前有{self.people}人")
        
def setup(bot):
    bot.add_cog(人數(bot))