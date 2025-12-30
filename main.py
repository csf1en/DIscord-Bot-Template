import asyncio
import os
import logging
from dotenv import load_dotenv
from bot.bot import UltimateBot

# 1. Setup Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)
logger = logging.getLogger("Main")

# 2. Load Environment Variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

async def main():
    # 3. Initialize and Run Bot
    async with UltimateBot() as bot:
        await bot.start(TOKEN)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        logger.info("Bot stopped by user.")
