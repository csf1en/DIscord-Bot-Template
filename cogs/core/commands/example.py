import discord
from discord.ext import commands
from discord import app_commands

class ExampleCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.hybrid_command creates both a prefix command and a slash command
    @commands.hybrid_command(name="ping", description="Check the bot's latency.")
    async def ping(self, ctx: commands.Context):
        """Returns the bot latency."""
        latency = round(self.bot.latency * 1000)
        
        embed = discord.Embed(
            title="Pong! 🏓",
            description=f"Latency is **{latency}ms**",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

    @ping.error
    async def ping_error(self, ctx, error):
        """Local error handler for the ping command."""
        await ctx.send(f"An error occurred: {error}")

async def setup(bot):
    await bot.add_cog(ExampleCommands(bot))
