import discord
from discord.ext import commands
import json,asyncio,datetime
import random
with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
class Time(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bot = bot
        self.channel = None
        self.bg_task = self.bot.loop.create_task(self.interval())
    '''async def interval(self):
        await self.bot.wait_until_ready()
        self.channel = self.bot.get_channel(int(jdata['set_time_channel']))
        while not self.bot.is_closed():
            await self.channel.send("I'm working!!!")
            await asyncio.sleep(5)'''
    async def time_task(self):
        await self.bot.wait_until_ready()
        self.channel = self.bot.get_channel(int(jdata['set_time_channel']))
        while not self.bot.is_closed():
            pass
    async def set_time(self,ctx,time):
        jdata['time'] =time
        with open('setting.json', mode='w', encoding='utf8') as jfile:
            json.dump(jdata,jfile,indent=4)
async def setup(bot: commands.Bot):
    await bot.add_cog(Time(bot))