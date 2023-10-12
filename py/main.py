import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='>', intents=intents)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run('MTE1Mjg2MjUzNjY5ODQyOTUwMQ.GJtz63.zedyXNGbXElmwauZwznXSxj8RaYpLPu2-HahKA')