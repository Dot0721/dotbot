import discord
from discord.ext import commands

class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="ping")
    async def ping(self, ctx):
        latency_ms = int(self.bot.latency * 1000)  # 使用 self.bot 获取延迟
        await ctx.send(f'{latency_ms}(ms)')

async def setup(bot: commands.Bot):
    await bot.add_cog(Main(bot))
