from .roleplay import Roleplay

async def setup(bot):
    rp = Roleplay()
    await bot.add_cog(rp)