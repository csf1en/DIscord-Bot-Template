import discord
from discord.ext import commands
import os
import logging

logger = logging.getLogger("BotClass")

class UltimateBot(commands.Bot):
    def __init__(self):
        # Initialize with all intents enabled
        intents = discord.Intents.all()
        
        super().__init__(
            command_prefix=commands.when_mentioned_or(os.getenv("PREFIX", "!")),
            intents=intents,
            help_command=None, # Disable default help to build a custom one later
            case_insensitive=True
        )

    async def setup_hook(self):
        """
        This is called automatically when the bot logs in.
        We use it to load extensions and sync slash commands.
        """
        logger.info("--- Starting Setup Hook ---")
        await self.load_extensions()
        
        # Syncing commands to Discord (Global Sync)
        # Note: In production, you should sync only when necessary to avoid rate limits.
        logger.info("Syncing Command Tree...")
        await self.tree.sync() 
        logger.info("Command Tree Synced.")

    async def load_extensions(self):
        """
        Recursively loads all .py files in the 'cogs' directory.
        """
        for root, dirs, files in os.walk("./cogs"):
            for filename in files:
                if filename.endswith(".py") and not filename.startswith("__"):
                    # Construct module path: cogs.core.commands.example
                    relative_path = os.path.relpath(root, ".")
                    module_path = relative_path.replace(os.sep, ".") + "." + filename[:-3]
                    
                    try:
                        await self.load_extension(module_path)
                        logger.info(f"Loaded extension: {module_path}")
                    except Exception as e:
                        logger.error(f"Failed to load extension {module_path}: {e}")

    async def on_ready(self):
        logger.info(f"Logged in as {self.user} (ID: {self.user.id})")
        logger.info("--- Bot is Ready ---")
