import discord
from discord.ext import commands
import json

from discord.ext.commands.cog import Cog
from core.classes import Cog_Extension
import random

with open ("background_setting.json",'r',encoding="utf8") as jfile:
    jdata=json.load(jfile)

class king(Cog_Extension):
    def compare(self,list):#傳入list後，挑出其中最大數字的引數
        a=0
        for i in range(4):
            if list[i]>a: 
                a=list[i] 
                max=i 
        return max

    def judge(self,card:list):
        number=[]
        king_card=card[0]
        if king_card[-2:]=="10":
            king_for_this_round=king_card[:-3]
        else :king_for_this_round=king_card[:-2]
        if self.king_color=="No_King": 
            for i in range(4):
                if card[i][:-2]==king_for_this_round:  number.append(jdata["No King"][card[i][-1]])
                elif card[i][:-3]==king_for_this_round:  number.append(jdata["No King"]["10"])
                else: number.append(0)
            print (number)
            win=king.compare(self,number)
            return win
        elif self.king_color=="mini":
            for i in range(4):
                if card[i][:-2]==king_for_this_round:  number.append(jdata["mini"][card[i][-1]])
                elif card[i][:-3]==king_for_this_round:  number.append(jdata["mini"]["10"])
                else: number.append(0)
            print (number)
            win=king.compare(self,number)
            return win
        elif self.king_color=="Middle":
            for i in range(4):
                if card[i][:-2]==king_for_this_round:  number.append(jdata["Middle"][card[i][-1]])
                elif card[i][:-3]==king_for_this_round:  number.append(jdata["Middle"]["10"])
                else: number.append(0)
            print (number)
            win=king.compare(self,number)
            return win
        else:
            for i in range(4):
                if card[i][:-2]==self.king_color:  number.append(jdata["normal"][card[i][-1]]+13)
                elif card[i][:-3]==self.king_color:  number.append(jdata["normal"]["10"]+13)
                elif card[i][:-2]==king_for_this_round:  number.append(jdata["normal"][card[i][-1]])
                elif card[i][:-3]==king_for_this_round:  number.append(jdata["normal"]["10"])
                else: number.append(0)
            print (number)
            win=king.compare(self,number)
            return win

    @commands.command()#待做:1.改成贏敦的人先出 2.出過的牌削掉 3.判斷遊戲輸贏 4.玩家超過五人 5.奇怪訊息處理
    async def set(self,ctx,a:int,king_color,team,win_player:int):
        if Cog_Extension.startplaying==True:
            with open ("background_setting.json",'r',encoding="utf8") as jfile:
                jdata=json.load(jfile)
            self.team=team
            self.king_color=king_color
            self.counter=win_player-2
            if self.king_color in jdata["color"] and 1<=a and a<=7 and (self.team=="a" or self.team=="b"):
                if self.team=="a":
                    self.a_win_edition=a+6
                    self.b_win_edition=14-self.a_win_edition
                    await ctx.channel.send(F"王牌花色是{self.king_color}\na隊要拿{self.a_win_edition}墩，b隊要拿{self.b_win_edition}墩")
                elif self.team=="b":
                    self.b_win_edition=a+6
                    self.a_win_edition=14-self.b_win_edition
                    await ctx.channel.send(F"王牌花色是{self.king_color}\na隊要拿{self.a_win_edition}墩，b隊要拿{self.b_win_edition}墩")
                if self.king_color=="Middle" or self.king_color=="mini":
                    for i in range(4):
                        with open ("background_setting.json",'r',encoding="utf8") as jfile:
                            jdata=json.load(jfile)
                        sort_list=[]
                        for element in jdata[F"player{i}_cards"]:  sort_list.append(jdata[F"sort {self.king_color}"][element])
                        sort_list.sort()
                        for a in range(13): jdata[F"player{i}_cards"][a]=jdata[F"sort_back {self.king_color}"][str(sort_list[a])]
                        with open("background_setting.json",'w',encoding="utf8")as jfile:
                            json.dump(jdata,jfile,indent=4)
                        message=''
                        for card in jdata[F"player{i}_cards"]: message+=F"{card},"
                        user=await self.bot.fetch_user(jdata["player"][i])
                        delete=await user.fetch_message(jdata[F"player{i}_id"])
                        await delete.delete()
                        text=await user.send(message)
                        jdata[F"player{i}_id"]=text.id
                        with open("background_setting.json",'w',encoding="utf8")as jfile:
                            json.dump(jdata,jfile,indent=4)
                Cog_Extension.startplaying=False
                self.channel=ctx.channel
                self.a_wincount,self.b_wincount=0,0
                self.cards=[]
                self.win_count_start=True
                print(self.join)
            else : await ctx.channel.send("你真的要這樣打牌嗎?")
    
    @commands.Cog.listener()
    async def on_message(self,msg):
        if self.win_count_start==True and msg.author!=self.bot.user:
            self.counter+=1
            if self.counter==4: self.counter=0
            with open ("background_setting.json",'r',encoding="utf8") as jfile:
                jdata=json.load(jfile)
            player=await self.bot.fetch_user(jdata["player"][self.counter])
            if msg.content in jdata["poker"] and msg.author==player:
                if msg.content in jdata[F"player{self.counter}_cards"]:
                    print ("receive")
                    content=msg.content
                    self.cards.append(content)
                    jdata[F"player{self.counter}_cards"].remove(content)
                    with open("background_setting.json",'w',encoding="utf8")as jfile:
                        json.dump(jdata,jfile,indent=4)
                else: 
                    await msg.channel.send("作弊爛ㄐㄐ")
                    self.counter-=1 
            else : self.counter-=1
            if len(self.cards)==4:
                print (self.cards)
                win=king.judge(self,self.cards)
                print (win)
                win-=(self.counter+1)
                print (win)
                if win<=-1: win+=4
                if win==0 or win==2: self.a_wincount+=1
                elif win==1 or win==3: self.b_wincount+=1
                winner=await self.bot.fetch_user(jdata["player"][win])
                await self.channel.send(F"{winner}贏了這一墩\n目前a隊拿了{self.a_wincount}墩，還要拿{self.a_win_edition-self.a_wincount}\n目前b隊拿了{self.b_wincount}墩，還要拿{self.b_win_edition-self.b_wincount}")
                self.cards=[]
                self.counter=win-1
                if self.a_wincount==self.a_win_edition:
                    await self.channel.send("遊戲結束，a隊勝利")
                    jdata["player"]=[]
                    for i in range(4):
                        jdata[F"player{i}_cards"]=[]
                    Cog_Extension.join=True
                    self.win_count_start=False
                elif self.b_wincount==self.b_win_edition:
                    await self.channel.send("遊戲結束，b隊勝利")
                    jdata["player"]=[]
                    for i in range(4):
                        jdata[F"player{i}_cards"]=[]
                    jdata["join"]="True"
                    self.win_count_start=False
                else:
                    for i in range(4):
                        with open ("background_setting.json",'r',encoding="utf8") as jfile:
                            jdata=json.load(jfile)
                        message=''
                        for card in jdata[F"player{i}_cards"]: message+=F"{card},"
                        user=await self.bot.fetch_user(jdata["player"][i])
                        delete=await user.fetch_message(jdata[F"player{i}_id"])
                        await delete.delete()
                        text=await user.send(message)
                        jdata[F"player{i}_id"]=text.id
                        with open("background_setting.json",'w',encoding="utf8")as jfile:
                            json.dump(jdata,jfile,indent=4)
            

def setup(bot):
    bot.add_cog(king(bot)) 