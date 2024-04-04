
import os

import discord
from dotenv import load_dotenv
from discord.ext import commands
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

custom_messages=[
    "soham ghayal",
    "hello",
    "gg",
    "impressive",
    "gone!!!!",
    
]

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)
   
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!') # type: ignore
    guild=discord.utils.get(client.guilds,id=int(GUILD)) # type: ignore
 
    


@client.command()

async def ping(ctx):
    await ctx.send('Pong!')
    

@client.command()
async def send(ctx):
    
    random_message=random.choice(custom_messages)
    await ctx.send(random_message)

client.run(TOKEN) # type: ignore