import discord
from discord.ext import commands
import json
from core.classes import Cog_Extension
import random

with open ("background_setting.json",'r',encoding="utf8") as jfile:
    jdata=json.load(jfile)

class distribution(Cog_Extension):
    async def distribution(self):
        if len(self.player)==4:
            print ("distribution")
            for people in self.player:
                message=""
                for i in range(13):
                    a=random.choice(jdata["poker"])
                    message+=F"{a} "
                    jdata["poker"].remove(a)
                    with open("background_setting.json",'w',encoding="utf8")as jfile:
                        json.dump(jdata,jfile,indent=4)
                await people.send(message)
            Cog_Extension.startplaying=True
            print(self.startplaying)
            print ("OK")
            jdata["poker"]=[
        "club A",
        "club 2",
        "club 3",
        "club 4",
        "club 5",
        "club 6",
        "club 7",
        "club 8",
        "club 9",
        "club 10",
        "club J",
        "club Q",
        "club K",
        "diamond A",
        "diamond 2",
        "diamond 3",
        "diamond 4",
        "diamond 5",
        "diamond 6",
        "diamond 7",
        "diamond 8",
        "diamond 9",
        "diamond 10",
        "diamond J",
        "diamond Q",
        "diamond K",
        "heart A",
        "heart 2",
        "heart 3",
        "heart 4",
        "heart 5",
        "heart 6",
        "heart 7",
        "heart 8",
        "heart 9",
        "heart 10",
        "heart J",
        "heart Q",
        "heart K",
        "space A",
        "space 2",
        "space 3",
        "space 4",
        "space 5",
        "space 6",
        "space 7",
        "space 8",
        "space 9",
        "space 10",
        "space J",
        "space Q",
        "space K"
    ]
            with open("background_setting.json",'w',encoding="utf8")as jfile:
                json.dump(jdata,jfile,indent=4)

            

def setup(bot):
    bot.add_cog(distribution(bot))