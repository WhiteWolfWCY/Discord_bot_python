# bot.py

import os
import time

import discord
from discord.ext import commands
from dotenv import load_dotenv
import youtube_dl
import os

load_dotenv()
TOKEN = "DISCORD SERVER TOKEN"

bot = commands.Bot(command_prefix='!')

@bot.command(name='ping_user')
async def ping_maciek(ctx):
    for i in range(10):
        time.sleep(0.3)
        await ctx.send('HI <@USER ID> WAKE UP!') 

@bot.command(name='get_lost')
async def get_lost(ctx):
    await ctx.send('Im tired of you. Get lost!') 

@bot.command(name='dm_maciek')
async def dm_maciek(ctx):
    for i in range(10):
        time.sleep(0.3)
        message = "Wanna play league of legends? "
        user = await bot.fetch_user("USERID")
        await user.send(message)

@bot.command(name='dm_rafal')
async def dm_rafal(ctx):
    for i in range(10):
        time.sleep(0.3)
        message = "Wanna play league of legends? "
        user = await bot.fetch_user("USERID")
        await user.send(message)

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, id="<719127151399534622>")
    await bot.add_roles(member, role)

bot.run(TOKEN)