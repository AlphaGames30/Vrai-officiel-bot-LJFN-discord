import discord
from discord.ext import commands

token='MTM0NTM0Mjg5MjUwMzIwNzk5Nw.GbDbdL.u4iWvc61OCM1IqN73Bv6d4Ue9X_byFgHd3y_f0'

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

bot.tree.command()
async def multiplication(interaction: discord.Interaction, nombre1: int, nombre2: int):
  await interaction.response.send_message(f' {nombre1} X {nombre2} = {nombre1 * nombre2}')

@bot.event
async def on_ready():
  print(f' connécté en tant que {bot.user}')
  try:
    synced = await bot.tree.sync()
    print(f"{len(synced)} commandes(s) syncronisé(s)")
  except Exception as e:
    print(e)
  

def main():
   bot.run(token)

if __name__ == '__main__':
  main()