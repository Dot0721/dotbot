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

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=discord.Intents.all()
        )

    async def on_ready(self):
        await self.change_presence(status=discord.Status.online, activity=discord.Game("Python"))
        synced = await self.tree.sync()
        print(f"已同步 {len(synced)} 個指令。")
        print(f"{self.user} 上線了!")

    async def setup_hook(self):
        for filename in os.listdir("./cog"):
            if filename.endswith(".py") and filename != "__init__.py":
                try:
                    await self.load_extension(f"cog.{filename[:-3]}")
                    print(f"Successfully loaded extension: cog.{filename[:-3]}")
                except Exception as e:
                    print(f"Failed to load extension cog.{filename[:-3]}. Exception: {e}")

bot = MyBot()
@bot.command()
async def load(ctx, extension):
    try:
        await bot.load_extension(f'cog.{extension}')
        await ctx.send(f'Loading {extension} done')
    except Exception as e:
        await ctx.send(f'Failed to load extension {extension}. Exception: {e}')

@bot.command()
async def unload(ctx, extension):
    try:
        await bot.unload_extension(f'cog.{extension}')
        await ctx.send(f'Unloading {extension} done')
    except Exception as e:
        await ctx.send(f'Failed to unload extension {extension}. Exception: {e}')

@bot.command()
async def reload(ctx, extension):
    try:
        await bot.reload_extension(f'cog.{extension}')
        await ctx.send(f'Reloading {extension} done')
    except Exception as e:
        await ctx.send(f'Failed to reload extension {extension}. Exception: {e}')
if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
