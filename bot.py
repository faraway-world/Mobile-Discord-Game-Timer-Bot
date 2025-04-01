import discord
from discord.ext import commands
import asyncio

# Set up bot intents
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Game name variable (Change this to any game)
game_name = "Blacksouls 2"  

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")  

    # Set custom status
    activity = discord.Game(name=game_name)
    await bot.change_presence(activity=activity)

    # Optional: Update status every minute
    counter = 0
    while True:
        counter += 1
        new_status = discord.Game(name=f"{game_name} - {counter} min")
        await bot.change_presence(activity=new_status)
        await asyncio.sleep(60)  # Update every minute

# Run the bot (Replace 'YOUR_BOT_TOKEN' with your actual bot token))
bot.run("YOUR_BOT_TOKEN")
