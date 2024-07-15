import discord
from discord.ext import commands
import json
import random
import requests
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
    @commands.command()
    async def test(self,ctx):
        response=requests.get('https://api.jsonstorage.net/v1/json/cbb72183-db06-418e-86a0-2e13bb50ae64/57754650-6175-45ea-95d7-99b44169d253')
        data=response.json()
        print(data['test'])
        data['test']="new test"
        update=requests.put('https://api.jsonstorage.net/v1/json/cbb72183-db06-418e-86a0-2e13bb50ae64/57754650-6175-45ea-95d7-99b44169d253?apiKey=0af7aee9-ecc1-49a2-990f-0a6dfeac2a24',
                            json=data
                            )
        print(update)
async def setup(bot: commands.Bot):
    await bot.add_cog(Main(bot))
