import discord
from discord.ext import commands

class ModérationCog(commands.Cog):
  def __init__(self, bot):
        self.bot = bot


  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, user: discord.Member, *, reason=None):
    await user.kick(reason=reason)

async def setup(bot):
    await bot.add_cog(ModérationCog(bot))