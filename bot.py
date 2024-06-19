import os
import discord
from discord.ext import commands
import json
import random
with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.default()  # 使用預設的 intents
intents.message_content = True       # 啟用 message_content 意圖以接收訊息內容
intents.members = True


bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    print(f'{member} join!')
    channel = bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    print(f'{member} leave!')
    channel = bot.get_channel(int(jdata['Leave_channel']))
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    latency_ms = int(bot.latency * 1000)
    await ctx.send(f'{latency_ms}(ms)')
@bot.command()
async def 頭像(ctx):
    pic=discord.File(jdata['bot_head'])
    await ctx.send(file=pic)
@bot.command()
async def 圖片(ctx):
    random_pic=random.choice(jdata['pic'])
    pic=discord.File(random_pic)
    await ctx.send(file=pic)
@bot.command()
async def web(ctx):
    random_pic=random.choice(jdata['url_pic'])
    await ctx.send(random_pic)
bot.run(jdata['TOKEN'])
