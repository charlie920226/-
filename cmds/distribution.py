import discord
from discord.ext import commands
import json
from core.classes import Cog_Extension
import random

with open ("background_setting.json",'r',encoding="utf8") as jfile:
    jdata=json.load(jfile)

class distribution(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content.endswith("是b隊") and msg.author==self.bot.user:
            print("OK")
            with open ("background_setting.json",'r',encoding="utf8") as jfile:
                jdata=json.load(jfile)
            for i in range(4):
                cards=random.sample(jdata["poker"],k=13)
                sort_list=[]
                for element in cards: 
                    jdata["poker"].remove(element)
                    sort_list.append(jdata["sort normal"][element])
                sort_list.sort()
                for a in range(13): cards[a]=jdata["sort_back normal"][str(sort_list[a])]
                jdata[F"player{i}_cards"]=cards
                with open("background_setting.json",'w',encoding="utf8")as jfile:
                    json.dump(jdata,jfile,indent=4)
            for i in range(4):
                message=''
                for card in jdata[F"player{i}_cards"]: message+=F"{card},"
                user=await self.bot.fetch_user(jdata["player"][i])
                text=await user.send(message)
                jdata[F"player{i}_id"]=text.id
                with open("background_setting.json",'w',encoding="utf8")as jfile:
                    json.dump(jdata,jfile,indent=4)
                print(jdata[F"player{i}_id"])
            Cog_Extension.getcard=True
            Cog_Extension.startplaying=True
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
            Cog_Extension.distribute=False
            print(self.join)
            self.join=True

            

def setup(bot):
    bot.add_cog(distribution(bot))