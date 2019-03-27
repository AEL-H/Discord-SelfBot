from discord.ext import commands
from cogs.utils.checks import *
from os import path
from PIL import Image
import io
import os
import sys
from wordcloud import WordCloud
from wordcloud import STOPWORDS
import io
from PIL import Image
import discord
import matplotlib
import numpy as np

matplotlib.use('Agg')

class WC:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def wc(self, ctx):
        print("Working")
        user = ctx.message.mentions[0]
        print(user.id)
        text = ""
        channel = ctx.message.channel
        async for message in channel.history(limit=10**10):
            if message.author.id != user.id:
                continue
            text += message.content
            text += " "
        wc = WordCloud(width=1920, height=1080, background_color="white", max_words=1000).generate(text)
        wc.to_file("wordcloud.png")
        wordcloudfile = discord.File(fp=open(os.path.join(os.getcwd(),"wordcloud.png"),'rb'))
        await channel.send(file=wordcloudfile)
        
    @commands.command(pass_context=True)
    async def wcc(self, ctx):
        print("Working")
        user = ctx.message.mentions[0]
        print(user.id)
        text = ""
        channel = ctx.message.channel
        async for message in channel.history(limit=10**10):
            if message.author.id != user.id:
                continue
            text += message.content
            text += " "
        the_mask = np.array(Image.open("heartmask.png"))
        wc = WordCloud(width=1920, height=1080, background_color="white", max_words=1000,font_path="C:/Windows/Fonts/I Love What You Do!!...ttf", mask=the_mask).generate(text)        
        wc.to_file("wordcloud.png")
        wordcloudfile = discord.File(fp=open(os.path.join(os.getcwd(),"wordcloud.png"),'rb'))
        await channel.send(file=wordcloudfile)        


def setup(bot):
    bot.add_cog(WC(bot))
