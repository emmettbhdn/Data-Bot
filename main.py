# Import needed libraries:
from core.src import helperFunctions
import discord
from discord.ext import commands
import os
from core.src.helperFunctions.keep_alive import keep_alive
from core.src.helperFunctions.helperFunctions import *

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Global Variables:

TOKEN = os.getenv("BOT_TOKEN")  # Getting the bot token from the .env file

client = commands.Bot(command_prefix=getPrefix, case_insensitive=True)
client.remove_command('help') # Remove standard help command for custom help command

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


@client.event
async def on_ready():
    print("Bot is ready")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"Early Developement Phase!"))

# Cog Loading Commands:

# Load Cog by Name


@client.command()
async def load(ctx, extension):
    if ctx.author.id == 615608898279309312:
        if extension == "all":
            loadAllCogs()
            await ctx.send("All cogs loaded!")
        else:
            client.load_extension(f'cogs.{extension}')
            await ctx.send(f"Cog `{extension}` loaded!")

# Unload Cog by name


@client.command()
async def unload(ctx, extension):
    if ctx.author.id == 615608898279309312:
        if extension == "all":
            unloadAllCogs()
            await ctx.send("All cogs unloaded!")
        else:
            client.unload_extension(f'cogs.{extension}')
            await ctx.send(f"Cog `{extension}` unloaded!")

# Reload Cog by name (unloading, then loading)


@client.command()
async def reload(ctx, extension):
    if ctx.author.id == 615608898279309312:
        if extension == "all":
            unloadAllCogs()
            loadAllCogs()
            await ctx.send("All cogs reloaded!")
        else:
            client.unload_extension(f'cogs.{extension}')
            client.load_extension(f'cogs.{extension}')
            await ctx.send(f"Cog `{extension}` reloaded!")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Automatic Cog Loading:

# Loading all cogs on startup


def loadAllCogs():
    for filename in os.listdir('./cogs/'):
        if filename.endswith('.py'):
            # Loads the extension by the file name and cuts off the .py at the end
            client.load_extension(f'cogs.{filename[:-3]}')
            print("Cog loaded: " + filename[:-3])
    print("All Systems alive and functional")


def unloadAllCogs():
    for filename in os.listdir('./cogs/'):
        if filename.endswith('.py'):
            # Unloads the extension by the file name and cuts off the .py at the end
            client.unload_extension(f'cogs.{filename[:-3]}')
            print("Cog unloaded: " + filename[:-3])


loadAllCogs()  # Inital load of all cogs on script execution
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Hosting and running the bot:

keep_alive()

# Running the client by its token
client.run(TOKEN)
