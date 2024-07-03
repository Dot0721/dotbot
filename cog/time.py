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
        self.counter=0
        #self.bg_task_interval = self.bot.loop.create_task(self.interval())
        self.bg_task_time_task = self.bot.loop.create_task(self.time_task())
    '''async def interval(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            with open('setting.json', mode='r', encoding='utf8') as jfile:
                jdata = json.load(jfile)
            self.channel = self.bot.get_channel(int(jdata['set_time_channel']))
            if self.channel:
                await self.channel.send("I'm working!!!")
            await asyncio.sleep(5)'''
    async def time_task(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            now_time = datetime.datetime.now().strftime('%H%M')
            with open('setting.json', mode='r', encoding='utf8') as jfile:
                jdata = json.load(jfile)
            self.channel = self.bot.get_channel(int(jdata['set_time_channel']))
            if self.channel and now_time == jdata['time'] and self.counter==0:
                await self.channel.send('Task Working')
                self.counter=1
            else:
                pass
            await asyncio.sleep(1)

    @commands.command(name='set_time')
    async def set_time(self, ctx, time):
        with open('setting.json', mode='r', encoding='utf8') as jfile:
            jdata = json.load(jfile)
        jdata['time'] = time
        with open('setting.json', mode='w', encoding='utf8') as jfile:
            json.dump(jdata, jfile, indent=4)
        await ctx.send(f'Time has been set to {time}')
        self.counter=0
async def setup(bot: commands.Bot):
    await bot.add_cog(Time(bot))