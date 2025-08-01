import discord
from discord.ext import commands

token='MTM0NTM0Mjg5MjUwMzIwNzk5Nw.GrRxdB.cnNTwEeh1ZkupgfyB74bRRoux51gwKKguwF9tQ'

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.hybrid_command()
async def ping(ctx):
  await ctx.send('pong')

bot.hybrid_command()
async def soustraire (interaction: discord.Interaction, nombre1: int, nombre2: int):
  await interaction.response.send_message(f'la différence entre {nombre1} et {nombre2} est égal a {nombre1 - nombre2}')

bot.hybrid_command()
async def note(ctx, note: str):
  await ctx.send(f"{note} enregistré !")

@bot.event
async def on_ready(): 
 await bot.tree.sync()

bot.run(token=token)
