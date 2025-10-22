import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot connecté en tant que {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong 🏓")

bot.run(os.getenv("DISCORD_TOKEN"))
