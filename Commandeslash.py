import discord
from discord.ext import commands

token='MTM0NTM0Mjg5MjUwMzIwNzk5Nw.GrRxdB.cnNTwEeh1ZkupgfyB74bRRoux51gwKKguwF9tQ'

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

bot.tree.command()
async def multiplication(interaction: discord.Interaction, nombre1: int, nombre2: int):
  await interaction.response.send_message(f' {nombre1} X {nombre2} = {nombre1 * nombre2}')

bot.tree.command(name="youtube" , description=  "envoie un lien vers la chaine youtube alpha_mine0285")
async def youtube(interaction: discord.Interaction):
  await interaction.response.send_message("https://youtube.com/@play-zrfix.fortblilx?si=7rXbE_3NwV0SI3ZP")

bot.tree.command(name="ticketsetup", description= "envoie un message pour crée un ticket")
async def ticketsetup(interaction: discord.Interaction):
  await interaction.response.send_message("Cliquez sur le bouton pour crée un ticket")
  await interaction.response.send_message(view=TicketView())
  await interaction.response.send_message("ticket crée")

class TicketView(discord.ui.View):
  @discord.ui.button(label="Créer un ticket",
style=discord.ButtonStyle.primary,
emoji="🎫")
  async def ticket(self, interaction: discord.Interaction, button:
  discord.ui.Button):
    await interaction.response.send_message("ticket crée", ephemeral=True)
    await interaction.user.send("votre ticket a était crée !")
    await interaction.user.send(view=CloseTicketView())

class CloseTicketView(discord.ui.View):
  @discord.ui.button(label="Fermé le ticket",
style=discord.ButtonStyle.primary,
emoji="🔒")
  async def close_ticket(self, interaction: discord.Interaction, button):
   await interaction.response.send_message("ticket férmé", ephemeral=True)

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
