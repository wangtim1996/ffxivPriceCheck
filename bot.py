# bot.py
import os
from dotenv import load_dotenv

from discord.ext import commands

from marketboard import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='bicolor')
async def bicolor(context):
    result = get_best_bicolor()
    response = ""
    for x in range(min(5, len(result))):
        response += str(x+1) + ": " + str(result[x][1]) + " (" + str(result[x][0]) + ")\n"

    await context.send(response)

bot.run(TOKEN)