import discord
import random 
from discord.ext import commands
import os

class GamesCog(commands.Cog):
  def __init__(self, bot):
        self.bot = bot

  @commands.command(name='lancedée', description= 'lance un dée et recoit    un chiffre aléatoire') 
  async def roll(self, ctx):
     await ctx.send(random.randint(1,6))

  @commands.command()
  async def pileouface(self, ctx, sr):
   result = random.choice(['pile', 'face'])
   await ctx.send(f'Le résulta est:  {result} ')

async def setup(bot):
    await bot.add_cog(GamesCog(bot))




