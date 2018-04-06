import random
import discord
import asyncio
import secrets
from discord.ext import commands
from discord.ext.commands import Bot
from os import listdir
from os.path import isfile, join

import sys, traceback

headers = {'User-Agent': 'PowerTaxiDiscordBot. Making this to help me learn Python'}
cogs_dir = "cogs"
startup_extensions = [cogs_dir + ".diceroll",cogs_dir + ".george",cogs_dir + ".ffxiv",cogs_dir + ".giantbomb"]
bot = Bot(command_prefix="sb.", description="This is a bot")

@bot.event
async def on_ready():
    print('Should be Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(startup_extensions)
    print('------')

@bot.command(pass_context = True)
async def hello(ctx, *, member : discord.Member = None):
    if member is None:
        await bot.say(ctx.message.author.mention + " I can't say hello to no-one")
        return

    if member.id == "156944642779250688":
        await bot.say(":wave: Bobbin")

    if member.id == "152051434488070145":
        await bot.say(":wave: Something Something I'm ok")

@commands.command()
async def hammertime(self):
    await self.bot.say('https://youtu.be/otCpCn0l4Wo?t=20')

@bot.command(pass_context=True)
async def info(ctx,user: discord.Member):
    embed = discord.Embed(title="{}'s Information".format(user.name),description="Stuff", color=0xff0000)
    embed.add_field(name="Name", value = user.name, inline = True)
    embed.add_field(name="UserID", value = user.id, inline = True)
    embed.add_field(name="Status", value = user.status, inline = True)
    embed.add_field(name="Role", value = user.top_role, inline = True)
    embed.add_field(name="Joined", value = user.joined_at, inline = True)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)
    # await bot.say("User's name is: {}".format(user.name))
    # await bot.say("userID is: {}".format(user.id))
    # await bot.say("User's status is: {}".format(user.status))
    # await bot.say("User's highest role is: {}".format(user.top_role))
    # await bot.say("User joined at: {}".format(user.joined_at))

@bot.command()
async def load(extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))

@bot.command()
async def unload(extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)


@bot.command()
async def test():
    await bot.say("..test..")

@bot.command()
async def tank():
    await bot.say("Things are hitting me! :sob:")

@bot.command()
async def shrug():
    await bot.say("¯\_(ツ)_/¯")

if __name__ == '__main__':
    for extension in [f.replace('.py', '') for f in listdir(cogs_dir) if isfile(join(cogs_dir, f))]:
        try:
            bot.load_extension(cogs_dir + "." + extension)
        except (discord.ClientException, ModuleNotFoundError):
            print(f'Failed to load extension {extension}.')
            traceback.print_exc()

bot.run(secrets.token)
