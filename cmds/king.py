import discord
from discord.ext import commands
import json
from core.classes import Cog_Extension
from cmds.start import start
from cmds.join import people

with open ("background_setting.json",'r',encoding="utf8") as jfile:
    jdata=json.load(jfile)

class king(people):
    def compare(self,list):
        a=0
        for i in range(4):
            if list[i]>a: 
                a=list[i] 
                max=i 
        return max

    def judge(self,card:list,player):
        number=[]
        if self.king_color=="NK": 
            king_card=card[0]
            king_for_this_round=king_card[:-2]
            for i in range(4):
                if card[i][:-2]!=king_for_this_round:
                    number.append[0]
                else: number.append[jdata["No King"][card[-1]]]
            winner=player[king.compare(self,number)]
            return winner
        elif self.king_color=="mn":
            king_card=card[0]
            king_for_this_round=king_card[:-2]
            for i in range(4):
                if card[i][:-2]!=king_for_this_round:
                    number.append[0]
                else: number.append[jdata["mini"][card[-1]]]
            winner=player[king.compare(self,number)]
            return winner
        elif self.king_color=="Md":
            king_card=card[0]
            king_for_this_round=king_card[:-2]
            for i in range(4):
                if card[i][:-2]!=king_for_this_round:
                    number.append[0]
                else: number.append[jdata["Medium"][card[-1]]]
            winner=player[king.compare(self,number)]
            return winner
        else:
            king_card=card[0]
            king_for_this_round=king_card[:-2]
            for i in range(4):
                if card[i][:-2]==self.king_color:
                    number.append[jdata["normal"][card[-1]+13]]
                elif card[i][:-2]!=king_for_this_round:
                    number.append[0]
                else: number.append[jdata["normal"][card[-1]]]
            winner=player[king.compare(self,number)]
            return winner

    @commands.command()
    async def set(self,ctx):
        if Cog_Extension.startplaying==True:
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
            Cog_Extension.startplaying=False
            self.channel=ctx.channel
            self.a_wincount,self.b_wincount=0,0
            self.cards=[]
            self.win_count_start=True
            print(self.player)
    
    @commands.Cog.listener()
    async def on_message(self,msg):
        if self.win_count_start==True:
            self.counter+=1
            print (self.counter)
            print (self.player)
            if msg.content in jdata["poker"] and msg.author==self.player[self.counter] and msg.author!=self.bot.user:
                if self.win_count_start==True:
                    self.cards+=msg.content
            if len(self.cards)==4:
                print ("finish")
                win=king.judge(self,self.cards,self.player)
                if win in self.ateam:self.a_wincount+=1
                else: self.b_wincount+=1
                await self.channel.send(F"{win}贏了這一墩\n目前a隊拿了{self.a_wincount}墩，還要拿{self.a_win_edition-self.a_wincount}\n目前b隊拿了{self.b_wincount}墩，還要拿{self.a_win_edition-self.a_wincount}")
                self.cards=[]
            if self.a_wincount==self.a_win_edition or self.b_wincount==self.b_win_edition:
                self.channel.send("遊戲結束")
            

           
def setup(bot):
    bot.add_cog(king(bot)) 