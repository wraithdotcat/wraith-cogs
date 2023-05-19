from redbot.core.bot import Red
from .roleplay import Roleplay

async def setup(bot: Red):
    rp = Roleplay(bot)
    await bot.add_cog(rp)