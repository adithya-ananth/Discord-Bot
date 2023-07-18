import random

from discord.ext import commands
from time import sleep

TOKEN = ''

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=':p ', intents=intents)

@bot.event
async def on_ready():
    print("Connected to Discord")

@bot.command(name = 'roast', help = 'List of cool one liners')
async def roast(ctx):
    roasts = [
        
    ]

    response = random.choice(roasts)
    await ctx.send(response)

@bot.command(name = 'toss', help = 'Tosses a coin')
async def toss(ctx):
    await ctx.send("Tossing....")
    sleep(3.5)
    results = ['Heads', 'Tails']
    res = random.choice(results)
    await ctx.send(res)

@bot.command(name = 'sticker', help = 'Get a sticker, duh')
async def stik(ctx):
    stickers = [
        
    ]

    await ctx.send(random.choice(stickers))

bot.run(TOKEN)
