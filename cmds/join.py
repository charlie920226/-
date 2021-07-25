import discord
from discord.ext import commands
import json
from core.classes import Cog_Extension
from cmds.distribution import distribution
import random
with open ("background_setting.json",'r',encoding="utf8") as jfile:
    jdata=json.load(jfile)

class people(Cog_Extension):
    @commands.Cog.listener()  #參加遊戲的指令
    async def on_message(self,msg):
        with open ("background_setting.json",'r',encoding="utf8") as jfile:
            jdata=json.load(jfile)
        if jdata["join"]=="True":  #參加遊戲指令的開關
            if msg.content=="來打牌":#如果輸入訊息為{來打牌}，就把傳訊息的人id加進json的player
                jdata["player"].append(msg.author.id)
                self.people+=1
                with open("background_setting.json",'w',encoding="utf8")as jfile:
                    json.dump(jdata,jfile,indent=4)
                await msg.channel.send(F"目前有{self.people}人")  
                if self.people==4:  #玩家滿四個人後，先用random.sample將player隨機排列，再將第一、二個人定為a組，第三、四個人為b組
                    jdata["player"]=random.sample(jdata["player"],k=4)
                    with open("background_setting.json",'w',encoding="utf8")as jfile:
                        json.dump(jdata,jfile,indent=4)
                    team_a=""
                    for i in range(2):
                        user=await self.bot.fetch_user(jdata["player"][i])
                        team_a+=F"{user} "
                    team_b=""
                    for i in range(2,4):
                        user=await self.bot.fetch_user(jdata["player"][i])
                        team_b+=F"{user} "
                    await msg.channel.send(F"{team_a} 是a隊\n{team_b}是b隊")
                    jdata["player"][1],jdata["player"][2]=jdata["player"][2],jdata["player"][1]
                    jdata["join"]="False"
                    with open("background_setting.json",'w',encoding="utf8")as jfile:
                        json.dump(jdata,jfile,indent=4)
                    Cog_Extension.distribute=True
                    self.people=0
                elif self.people>=5:
                    jdata["player"]=[]
                    with open("background_setting.json",'w',encoding="utf8")as jfile:
                        json.dump(jdata,jfile,indent=4)
                    await msg.channel.send("超過四人，發生錯誤\n將人數歸零，重新開始")
            elif msg.content=="不打了":  #若輸入{不打了}，則把此玩家id從player中移除
                jdata["player"].remove(msg.author.id)
                self.people-=1
                with open("background_setting.json",'w',encoding="utf8") as jfile:
                    json.dump(jdata,jfile,indent=4)
                await msg.channel.send(F"目前有{self.people}人")

    @commands.command()
    async def use(self,ctx):
        await ctx.send("橋牌機器人使用說明:\n1.輸入(來打牌)，機器人會登錄玩家；輸入(不打了)，則可以取消登錄\n2.湊滿4個人時，會將玩家隨機分為a、b隊，左上、左下、右上、右下編號分別牌為1、2、3、4(出牌順序)\3.喊牌時以出牌反方向進行，喊完牌後用([set 喊的墩數 王花色 隊伍 喊到王的玩家編號)的形式輸入\n花色:mini,club,diamond,Middle,heart,\nspace,No_King\nex:[set 3 No_King b 2(注意每項輸入間有空格)\n4.出牌方式為在頻道上把自己要打的牌用訊息送出")

        #await ctx.send("""橋牌機器人使用說明:
        #1.輸入(來打牌)，機器人會登錄玩家；輸入(不打了)，則可以取消登錄
        #2.湊滿4個人時，會將玩家隨機分為a、b隊，左上、左下、右上、右下編號分別為1、2、3、4(出牌順序)  
        #3.喊牌時以出牌反方向進行，喊完牌後用([set 喊的墩數 王牌花色 隊伍 喊到王的玩家編號)的形式輸入
        #花色:mini,club,diamond,Middle,heart,space,No_King
        #ex:[set 3 No_King b 2(注意每項輸入間有空格)
        #4.出牌方式為在頻道上把自己要打的牌用訊息送出""")
def setup(bot):
    bot.add_cog(people(bot))