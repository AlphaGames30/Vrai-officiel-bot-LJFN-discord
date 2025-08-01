import discord

token ='DISCORD_TOKEN'

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
      return
    elif message.content == "bonjour":
     await message.channel.send("bonjour, c'est le bot ca va?")

@client.event
async def on_message_delete(message: discord.Message):
   await message.channel.send(f"{message.author.name} + ' a supprimé un message")

@client.event
async def on_ready():
  print('le bot est pret')
                              
client.run(token=token)
