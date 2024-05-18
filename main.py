# Discord Anti-Links Bot Source Code

import discord
from discord.ext import commands

# Intents
intents = discord.Intents.default()
intents.message_content = True  # Enable messages

# Set your bot token here
TOKEN = ''

# Create a bot instance with a specified command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == bot.user:
        return

    # Check if the message contains a link or an invite
    if any(link in message.content for link in ['http://', 'https://', 'discord.gg/']):
        # Delete the message with the link
        await message.delete()
        
        # Kick the user who sent the message
        await message.author.kick(reason="Sending links or invites is not allowed.")

    await bot.process_commands(message)

# Run the bot
bot.run(TOKEN)

