import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.members = True

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def massdm(ctx, *, message):
    if ctx.author.guild_permissions.administrator: 
        members = ctx.guild.members
        for member in members:
            try:
                if member != bot.user and not member.bot:  
                    await member.send(message)
                    await ctx.send(f'Message sent to {member.name}')
                    await asyncio.sleep(1)  # Sleep to avoid rate limit
            except discord.HTTPException as e:
                await ctx.send(f'Error sending message to {member.name}: {str(e)}')
        await ctx.send('Mass DM completed.')
    else:
        await ctx.send('You do not have permission to use this command.')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send(f'An error occurred: {str(error)}')

# Run the bot
bot.run('TOKEN')
