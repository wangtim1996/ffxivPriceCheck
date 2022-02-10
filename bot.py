# bot.py
import os
from dotenv import load_dotenv

import discord
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
    await context.send("0.5")

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


@bot.command(name='poetic',
             help='Gets the top 5 best poetics materials to sell. Items with * are guild seal materials')
async def poetic(context):
    if(not filter_channel(context)):
        return

    result = get_best_poetic()
    response = ""
    for x in range(min(5, len(result))):
        response_line = f"{x+1}: {result[x].name} (marketboard: {result[x].price}) [value: {result[x].value}]\n"
        response += response_line

    response += "(Items with * requires converting poetics to guild seals.)"
    await context.send(response)


@bot.command(name='guildseal',
             help='Gets the top 5 best poetics materials to sell. Items with * are guild seal materials')
async def guildseal(context):
    if(not filter_channel(context)):
        return

    result = get_best_guildseal()

    response = ""
    for x in range(min(5, len(result))):
        response_line = f"{x+1}: {result[x].name} (marketboard: {result[x].price}) [value: {result[x].value}]\n"
        response += response_line

    await context.send(response)

@bot.command(name='poll',
             help='Creates a poll based. Usage: !poll \"option 1\" \"option 2\" etc...')
async def poll(context, *args):
    if not args:
        await context.send("Please add options to your poll.")
        return

    if len(args) == 1:
        await context.send("Add more options to your poll.")
        return

    if len(args) > 16:
        await context.send("Only 16 options max.")
        return

    emote_list = [
        "one"
        , "two"
        , "three"
        , "four"
        , "five"
        , "six"
        , "seven"
        , "eight"
        , "nine"
        , "zero"
        , "regional_indicator_a"
        , "regional_indicator_b"
        , "regional_indicator_c"
        , "regional_indicator_d"
        , "regional_indicator_e"
        , "regional_indicator_f"
    ]

    emoji_list = [
        "1\N{COMBINING ENCLOSING KEYCAP}"
        , "2\N{COMBINING ENCLOSING KEYCAP}"
        , "3\N{COMBINING ENCLOSING KEYCAP}"
        , "4\N{COMBINING ENCLOSING KEYCAP}"
        , "5\N{COMBINING ENCLOSING KEYCAP}"
        , "6\N{COMBINING ENCLOSING KEYCAP}"
        , "7\N{COMBINING ENCLOSING KEYCAP}"
        , "8\N{COMBINING ENCLOSING KEYCAP}"
        , "9\N{COMBINING ENCLOSING KEYCAP}"
        , "0\N{COMBINING ENCLOSING KEYCAP}"
        , "\N{REGIONAL INDICATOR SYMBOL LETTER A}"
        , "\N{REGIONAL INDICATOR SYMBOL LETTER B}"
        , "\N{REGIONAL INDICATOR SYMBOL LETTER C}"
        , "\N{REGIONAL INDICATOR SYMBOL LETTER D}"
        , "\N{REGIONAL INDICATOR SYMBOL LETTER E}"
        , "\N{REGIONAL INDICATOR SYMBOL LETTER F}"
    ]

    response = ""
    for idx, x in enumerate(args):
        emote = emote_list[idx]
        response_line = f":{emote}: - {x}\n"
        response += response_line

    msg = await context.send(response)

    for idx in range(len(args)):
        await msg.add_reaction(emoji_list[idx])

def get_name(s):
    return s.encode('ascii', 'namereplace')

@bot.command(name='emoji',
             help='dev tool')
async def emoji(context, arg):
    await context.send(get_name(arg))



bot.run(TOKEN)
