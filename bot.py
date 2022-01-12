# bot.py
import os
from dotenv import load_dotenv

from discord.ext import commands

from marketboard import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Change only the no_category default string
help_command = commands.DefaultHelpCommand(
    no_category = 'Commands'
)

bot = commands.Bot(
    command_prefix='!',
    help_command = help_command)

def filter_channel(context):
    if(context.guild.id == 519366887570800640):
        if(context.channel.id == 883979459785527336):
            return True
        else:
            return False
    elif(context.guild.id == 920867523753291807):
        if(context.channel.id == 920867524327927880):
            return True
        else:
            return False
    else:
        return True


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='version',
             help='Returns current version.')
async def versionCheck(context):
    if(not filter_channel(context)):
        return
    await context.send("0.31")

@bot.command(name='bicolor',
             help='Gets the top 5 best bicolor materials to sell.')
async def bicolor(context):
    if(not filter_channel(context)):
        return
    result = get_best_bicolor()
    response = ""
    for x in range(min(5, len(result))):
        response_line = f"{x+1}: {result[x].name} (marketboard: {result[x].price}) [value: {result[x].value}]\n"
        response += response_line
        # response += str(x+1) + ": " + str(result[x].name)\
        #     + " (marketboard: " + str(result[x].price) + " gil | value: " + str(result[x].value) + ")\n"

    await context.send(response)

@bot.command(name='aphorism',
             help='Gets the top 5 best aphorism materials to sell.')
async def aphorism(context):
    if(not filter_channel(context)):
        return
    result = get_best_aphorism()
    response = ""
    for x in range(min(5, len(result))):
        response_line = f"{x+1}: {result[x].name} (marketboard: {result[x].price}) [value: {result[x].value}]\n"
        response += response_line

    await context.send(response)

bot.run(TOKEN)
