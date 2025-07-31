import discord
from discord.ext import commands

token = 'MTM0NTM0Mjg5MjUwMzIwNzk5Nw.GbDbdL.u4iWvc61OCM1IqN73Bv6d4Ue9X_byFgHd3y_f0'

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

bot.tree.command()
async def hello_world(context):
 await context.send("bonjour tous le monde")

bot.command()
async def decompte (context, delai: int):
  await context.send("départ dans...")
  for i in range(delai, 0, -1):
    await context.send(i)
  await context.send("fin du décompte")

bot.command()
async def répéter(interaction: discord.Interaction, nombre: int, message:
str):
  for _ in range(nombre):
   await interaction.followup.send(message)

if __name__ == '__main__':
    print('Hello World')
bot.run(token=token)