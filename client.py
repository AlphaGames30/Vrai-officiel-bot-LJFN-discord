import discord

token = "MTM0NTM0Mjg5MjUwMzIwNzk5Nw.GbDbdL.u4iWvc61OCM1IqN73Bv6d4Ue9X_byFgHd3y_f0"

client = discord.Client(intents=discord.Intents.all())

client.run(token=token)