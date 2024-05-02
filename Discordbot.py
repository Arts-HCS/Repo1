import discord
from discord.ext import commands
import random
import os 
import requests

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="/",intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("-----------------")

def get_duck_image():
    url = "https://random-d.uk/api/random"
    get = requests.get(url, timeout=10)
    data = get.json()
    return data["url"]

@bot.command()
async def duck(ctx):
    img = get_duck_image()
    await ctx.send(img)

@bot.command()
async def meme(ctx):
    memes_list = os.listdir("Images")
    meme = random.choice(memes_list)
    with open(f"Images/{meme}","rb") as f: 
        to_send = discord.File(f)
        
    await ctx.send(file=to_send)

@bot.command()
async def animal(ctx):
    with open("Animals/meme5.jpg","rb") as g:
        foto = discord.File(g)
    await ctx.send(file=foto)
    

bot.run('TOKEN')
