import discord

token ='DISCORD_TOKEN'

client = discord.Client(intents=discord.Intents.all())

client.run(token=token)
