import calendar
import datetime
import os
import random

from discord.ext import commands
from time import sleep

TOKEN = ''

bot = commands.Bot(command_prefix = ':p ')

@bot.event
async def on_ready():
    print("Connected to Discord")

@bot.command(name = 'roast', help = 'List of cool one liners')
async def roast(ctx):
    roasts = [
        "You're so ugly, if you had a penny for every ugly person you saw, you would be a millionare by looking at the mirror",
        "If I had a quarter for everytime you said something smart, I would be broke for life.",
        "It's better to let someone think you are an Idiot than to open your mouth and prove it.",
        "I don't engage in mental combat with the unarmed.",
        "Your life can't be a joke cuz jokes have meaning.",
        "Light travels faster than sound which is why you seemed bright until you spoke.",
        "You bring everyone so much joy...... when you leave the server.",
        "I thought of you today. It reminded me to take out the trash.",
        "You are like a cloud. When you disappear it’s a beautiful day.",
        "You just might be why the middle finger was invented in the first place.",
        "Somebody you’ll go far.... and I really hope you stay there.",
        "You have an entire life to be an idiot. Why not take today off?",
        "You're as useless as the digits after 3.14",
        "I'd like to kick you in the teeth, but why should I improve your looks?"
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
        "https://cdn.discordapp.com/emojis/810713916828024862.png?v=1",
        "https://cdn.discordapp.com/emojis/810706622405935185.png?v=1",
        "https://cdn.discordapp.com/emojis/810706991294578708.png?v=1",
        "https://cdn.discordapp.com/emojis/810707421127114753.png?v=1",
        "https://cdn.discordapp.com/emojis/810707675389100063.png?v=1",
        "https://cdn.discordapp.com/emojis/811294790196133958.png?v=1",
        "https://cdn.discordapp.com/emojis/811527061319581696.png?v=1",
        "https://cdn.discordapp.com/emojis/811527536445882369.png?v=1",
        "https://cdn.discordapp.com/emojis/811527601054941184.png?v=1",
        "https://cdn.discordapp.com/emojis/811527647355207682.png?v=1",
        "https://cdn.discordapp.com/emojis/811529018843070524.png?v=1"
    ]

    await ctx.send(random.choice(stickers))

bot.run(TOKEN)
