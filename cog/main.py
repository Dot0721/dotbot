import discord
from discord.ext import commands

class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="ping")
    async def ping(self, ctx):
        latency_ms = int(self.bot.latency * 1000)  # 使用 self.bot 获取延迟
        await ctx.send(f'{latency_ms}(ms)')
    @commands.command()
    async def nsfw(self,ctx):
        embed=discord.Embed(title="千楼🔞", url="https://x.com/qianlou12374/media", description=" @qianlou12374")
        embed.set_author(name="千楼", icon_url="https://pbs.twimg.com/profile_images/1786370727794573313/iOgjaweS_400x400.jpg")
        embed.set_thumbnail(url="https://pbs.twimg.com/media/GPiqDncb0AAG8Lp?format=jpg&name=medium")
        embed.set_footer(text="18+")
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Main(bot))
