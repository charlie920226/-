import discord
from discord.ext import commands
import json
from core.classes import Cog_Extension
import random

with open ("background_setting.json",'r',encoding="utf8") as jfile:
    jdata=json.load(jfile)

class distribution(Cog_Extension):
    async def distribution(self):
        if self.people==2:
            self.people=0
            print ("distribution")
            for people in self.player:
                message=""
                for i in range(13):
                    a=random.choice(jdata["poker"])
                    message+=F"{a} "
                    jdata["poker"].remove(a)
                    with open("background_setting.json",'w',encoding="utf8")as jfile:
                        json.dump(jdata,jfile,indent=4)
                    message+='stop'
                await people.send(message)
            

def setup(bot):
    bot.add_cog(distribution(bot))