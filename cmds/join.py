import discord
from discord.ext import commands
import json
from core.classes import Cog_Extension
from cmds.distribution import distribution
import random
with open ("background_setting.json",'r',encoding="utf8") as jfile:
    jdata=json.load(jfile)

class people(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content=="來打牌":
            self.people+=1
            self.player.append(msg.author)
            await msg.channel.send(F"目前有{self.people}人")
            if self.people==4:
                self.player=random.sample(self.player,k=4)
                team_1=""
                for i in range(2):
                    team_1+=F"{self.player[i]} "
                team_2=""
                for i in range(2,4):
                    team_2+=F"{self.player[i]} "
                await msg.channel.send(F"{team_1} 是一隊\n{team_2}是一隊")
                distribution.distribution(self)
        elif msg.content=="不打了":
            self.people-=1
            self.player.remove(msg.author)
            await msg.channel.send(F"目前有{self.people}人")
        
def setup(bot):
    bot.add_cog(people(bot))