import discord

token = "MTM0NTM0Mjg5MjUwMzIwNzk5Nw.GrRxdB.cnNTwEeh1ZkupgfyB74bRRoux51gwKKguwF9tQ"

client = discord.Client(intents=discord.Intents.all())

client.run(token=token)
