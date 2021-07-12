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
                team_a=""
                for i in range(2):
                    team_a+=F"{self.player[i]} "
                team_b=""
                for i in range(2,4):
                    team_b+=F"{self.player[i]} "
                await msg.channel.send(F"{team_a} 是a隊\n{team_b}是b隊")
                distribution.distribution(self)
        elif msg.content=="不打了":
            self.people-=1
            self.player.remove(msg.author)
            await msg.channel.send(F"目前有{self.people}人")
        
def setup(bot):
    bot.add_cog(people(bot))