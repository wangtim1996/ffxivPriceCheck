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


@bot.command(name='version')
async def versionCheck(context):
    await context.send("0.30")

@bot.command(name='bicolor')
async def bicolor(context):
    result = get_best_bicolor()
    response = ""
    for x in range(min(5, len(result))):
        response_line = f"{x+1}: {result[x].name} (marketboard: {result[x].price}) [value: {result[x].value}]\n"
        response += response_line
        # response += str(x+1) + ": " + str(result[x].name)\
        #     + " (marketboard: " + str(result[x].price) + " gil | value: " + str(result[x].value) + ")\n"

    await context.send(response)

@bot.command(name='aphorism')
async def aphorism(context):
    result = get_best_aphorism()
    response = ""
    for x in range(min(5, len(result))):
        response_line = f"{x+1}: {result[x].name} (marketboard: {result[x].price}) [value: {result[x].value}]\n"
        response += response_line

    await context.send(response)


@bot.command(name='help')
async def aphorism(context):
    response = "!bicolor - best bicolor gemstone item to sell\n"
    response += "!aphorism - best material to sell on marketboard\n"
    await context.send(response)


bot.run(TOKEN)
