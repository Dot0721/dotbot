import discord
from discord.ext import commands
import json
import random

# 读取设置文件
with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_member_join(self,member):
        print(f'{member} join!')
        channel = self.bot.get_channel(int(jdata['Welcome_channel']))
        await channel.send(f'{member} join!')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        print(f'{member} leave!')
        channel = self.bot.get_channel(int(jdata['Leave_channel']))
        await channel.send(f'{member} leave!')
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content=='hi' and msg.author != self.bot.user:
            await msg.channel.send('hi')
async def setup(bot: commands.Bot):
    await bot.add_cog(Event(bot))