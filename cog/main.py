import discord
from discord.ext import commands
import json
import random
with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="ping")
    async def ping(self, ctx):
        latency_ms = int(self.bot.latency * 1000)  # 使用 self.bot 获取延迟
        await ctx.send(f'{latency_ms}(ms)')
    @commands.command()
    async def nsfw(self,ctx):
        selected = random.choice(jdata['author'])
        author = selected[0]
        author_id = selected[1]
        author_url = selected[2]
        icon_url = selected[3]
        pic_url = selected[4]
        embed=discord.Embed(title=f"{author}", description=f"{author_id}",url=f"{author_url}")
        embed.set_author(name=f"{author}", icon_url=f"{icon_url}")
        embed.set_thumbnail(url=f"{pic_url}")
        embed.set_footer(text="18+")
        await ctx.send(embed=embed)
    @commands.command()
    async def say(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)
    @commands.command()
    async def clean(self,ctx,index:int):
        await ctx.channel.purge(limit=index+1)
        await ctx.send(f'clean {index} messages done.')
async def setup(bot: commands.Bot):
    await bot.add_cog(Main(bot))
