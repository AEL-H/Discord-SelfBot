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

BG_COLOUR = None 
RESOLUTION = {'width' : 1920, 'height' : 1080} 
MAX_WORDS = 1000 
FILENAME = "wordcloud.png"
MASK_PATH = "heartmask.png"
FONT_PATH = "C:/Windows/Fonts/I Love What You Do!!...ttf" 
MODE = "RGBA"

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
        async for message in channel.history(limit=None):
            if message.author.id != user.id:
                continue
            text += message.content
            text += " "
        the_mask = np.array(Image.open(MASK_PATH))
        wc = WordCloud(width=RESOLUTION['width'], height=RESOLUTION['height'], background_color=BG_COLOUR, max_words=MAX_WORDS,font_path=FONT_PATH, mask=the_mask).generate(text)        
        wc.to_file(FILENAME)
        wordcloudfile = discord.File(fp=open(os.path.join(os.getcwd(),FILENAME),'rb'))
        await channel.send(file=wordcloudfile)        


def setup(bot):
    bot.add_cog(WC(bot))
