import discord
from discord.ext import commands
import json
import random

# 读取设置文件
with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def url(self, ctx):
        await ctx.send(ctx.author.avatar.url)

    @commands.command()
    async def 頭像(self, ctx):
        pic = discord.File(jdata['bot_head'])
        await ctx.send(file=pic)

    @commands.command()
    async def 圖片(self, ctx):
        random_pic = random.choice(jdata['pic'])
        pic = discord.File(random_pic)
        await ctx.send(file=pic)

    @commands.command()
    async def web(self, ctx):
        random_pic = random.choice(jdata['url_pic'])
        await ctx.send(random_pic)

async def setup(bot: commands.Bot):
    await bot.add_cog(Core(bot))
