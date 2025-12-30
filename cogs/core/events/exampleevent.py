import discord
from discord.ext import commands
import logging

logger = logging.getLogger("Events")

class ExampleEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        # Ignore messages from the bot itself
        if message.author.bot:
            return

        # Example: React to a specific keyword
        if "hello bot" in message.content.lower():
            await message.add_reaction("👋")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """Global Error Handler"""
        if isinstance(error, commands.CommandNotFound):
            return  # Ignore unknown commands
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to do that!", ephemeral=True)
        else:
            logger.error(f"Error in {ctx.command}: {error}")

async def setup(bot):
    await bot.add_cog(ExampleEvents(bot))
