import discord
from redbot.core import commands, Config
from random import randint
import aiohttp
import logging

log = logging.getLogger("Roleplay")
log.setLevel(logging.DEBUG)

console = logging.StreamHandler()

if logging.getLogger("red").isEnabledFor(logging.DEBUG):
    console.setLevel(logging.DEBUG)
else:
    console.setLevel(logging.INFO)
log.addHandler(console)

BaseCog = getattr(commands, "Cog", object)


class Roleplay(BaseCog):
    """Interact with people!"""

    def __init__(self):
        self.config = Config.get_conf(self, identifier=842364413)
        default_global = {
            "hugs": [
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_0.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_1.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_2.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_3.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_4.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_5.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_6.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_7.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_8.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_9.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_10.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_11.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_12.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_13.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_14.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_15.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_16.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_17.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_18.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_19.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_20.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_21.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_22.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_23.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_24.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_25.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_26.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_27.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_28.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_29.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/hug/image_30.gif",
            ],
            "cuddle": [
                "https://cdn.wraithfx.com/cog-assets/roleplay/cuddle/image_0.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/cuddle/image_1.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/cuddle/image_2.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/cuddle/image_3.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/cuddle/image_4.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/cuddle/image_5.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/cuddle/image_6.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/cuddle/image_7.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/cuddle/image_8.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/cuddle/image_9.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/cuddle/image_10.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/cuddle/image_11.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/cuddle/image_12.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/cuddle/image_13.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/cuddle/image_14.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/cuddle/image_15.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/cuddle/image_16.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/cuddle/image_17.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/cuddle/image_18.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/cuddle/image_19.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/cuddle/image_20.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/cuddle/image_21.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/cuddle/image_22.gif",
            ],
            "pat": [
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_0.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_1.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_2.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_3.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_4.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_5.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_6.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_7.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_8.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_9.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_10.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_11.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_12.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_13.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_14.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_15.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_16.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_17.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_18.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_19.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_20.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_21.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_22.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_23.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_24.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_25.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_26.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_27.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_28.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_29.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/pat/image_30.gif",
            ],
            "highfive": [
                "https://cdn.wraithfx.com/cog-assets/roleplay/highfive/image_0.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/highfive/image_1.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/highfive/image_2.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/highfive/image_3.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/highfive/image_4.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/highfive/image_5.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/highfive/image_6.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/highfive/image_7.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/highfive/image_8.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/highfive/image_9.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/highfive/image_10.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/highfive/image_11.gif",
            ],
            "poke": [
                "https://cdn.wraithfx.com/cog-assets/roleplay/poke/image_0.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/poke/image_1.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/poke/image_2.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/poke/image_3.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/poke/image_4.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/poke/image_5.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/poke/image_6.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/poke/image_7.gif",
            ],
            "tickle": [
                "https://cdn.wraithfx.com/cog-assets/roleplay/tickle/image_0.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/tickle/image_1.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/tickle/image_2.gif",
            ],
            "kiss": [
                "https://cdn.wraithfx.com/cog-assets/roleplay/kiss/image_0.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/kiss/image_1.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/kiss/image_2.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/kiss/image_3.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/kiss/image_4.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/kiss/image_5.gif",
            ],
            "lick": [
                "https://cdn.wraithfx.com/cog-assets/roleplay/lick/image_0.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/lick/image_1.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/lick/image_2.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/lick/image_3.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/lick/image_4.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/lick/image_5.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/lick/image_6.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/lick/image_7.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/lick/image_8.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/lick/image_9.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/lick/image_10.gif",
            ],
            "feed": [
                "https://cdn.wraithfx.com/cog-assets/roleplay/feed/image_0.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/feed/image_1.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/feed/image_2.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/feed/image_3.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/feed/image_4.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/feed/image_5.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/feed/image_6.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/feed/image_7.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/feed/image_8.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/feed/image_9.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/feed/image_10.gif",
            ],
            "smug": [
                "https://cdn.wraithfx.com/cog-assets/roleplay/smug/image_0.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/smug/image_1.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/smug/image_2.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/smug/image_3.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/smug/image_4.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/smug/image_5.gif",
            ],
            "kill": [
                "https://cdn.wraithfx.com/cog-assets/roleplay/kill/image_0.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/kill/image_1.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/kill/image_2.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/kill/image_3.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/kill/image_4.gif",
            ],
            "slap": [
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_0.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_1.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_2.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_3.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_4.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_5.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_6.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_7.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_8.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_9.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_10.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_11.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_12.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_13.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_14.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_15.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_16.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_17.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_18.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_19.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_20.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_21.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_22.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_23.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_24.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_25.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_26.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_27.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_28.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_29.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_30.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_31.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_32.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_33.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/slap/image_34.gif",
            ],
            "punch": [
                "https://cdn.wraithfx.com/cog-assets/roleplay/punch/image_0.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/punch/image_1.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/punch/image_2.gif",
                "https://cdn.wraithfx.com/cog-assets/roleplay/punch/image_3.gif",
            ],
        }
        self.config.register_global(**default_global)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def hugs(self, ctx, *, user: discord.Member):
        """Hugs a user."""

        author = ctx.message.author
        images = await self.config.hugs()

        nekos = await self.fetch_nekos_life(ctx, "hug")
        images.extend(nekos)

        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} hugs {user.mention}**"
        embed.set_footer(text="https://github.com/wraithfx/redbot-wraith")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def cuddle(self, ctx, *, user: discord.Member):
        """Cuddles a user."""

        author = ctx.message.author
        images = await self.config.cuddle()

        nekos = await self.fetch_nekos_life(ctx, "cuddle")
        images.extend(nekos)

        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} cuddles {user.mention}**"
        embed.set_footer(text="https://github.com/wraithfx/redbot-wraith")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def kiss(self, ctx, *, user: discord.Member):
        """Kisses a user."""

        author = ctx.message.author
        images = await self.config.kiss()

        nekos = await self.fetch_nekos_life(ctx, "kiss")
        images.extend(nekos)

        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} kisses {user.mention}**"
        embed.set_footer(text="https://github.com/wraithfx/redbot-wraith")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def slap(self, ctx, *, user: discord.Member):
        """Slaps a user."""

        author = ctx.message.author
        images = await self.config.slap()

        nekos = await self.fetch_nekos_life(ctx, "slap")
        images.extend(nekos)

        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} slaps {user.mention}**"
        embed.set_footer(text="https://github.com/wraithfx/redbot-wraith")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def pat(self, ctx, *, user: discord.Member):
        """Pats a user."""

        author = ctx.message.author
        images = await self.config.pat()

        nekos = await self.fetch_nekos_life(ctx, "pat")
        images.extend(nekos)

        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} pats {user.mention}**"
        embed.set_footer(text="https://github.com/wraithfx/redbot-wraith")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def lick(self, ctx, *, user: discord.Member):
        """Licks a user."""

        author = ctx.message.author
        images = await self.config.lick()
        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} licks {user.mention}**"
        embed.set_footer(text="https://github.com/wraithfx/redbot-wraith")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def highfive(self, ctx, *, user: discord.Member):
        """High-fives a user."""

        author = ctx.message.author
        images = await self.config.highfive()
        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} high-fives {user.mention}**"
        embed.set_footer(text="https://github.com/wraithfx/redbot-wraith")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def feed(self, ctx, *, user: discord.Member):
        """Feeds a user."""

        author = ctx.message.author
        images = await self.config.feed()

        nekos = await self.fetch_nekos_life(ctx, "feed")
        images.extend(nekos)

        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} feeds {user.mention}**"
        embed.set_footer(text="https://github.com/wraithfx/redbot-wraith")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def tickle(self, ctx, *, user: discord.Member):
        """Tickles a user."""

        author = ctx.message.author
        images = await self.config.tickle()

        nekos = await self.fetch_nekos_life(ctx, "tickle")
        images.extend(nekos)

        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} tickles {user.mention}**"
        embed.set_footer(text="https://github.com/wraithfx/redbot-wraith")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def poke(self, ctx, *, user: discord.Member):
        """Pokes a user."""

        author = ctx.message.author
        images = await self.config.poke()

        nekos = await self.fetch_nekos_life(ctx, "poke")
        images.extend(nekos)

        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} pokes {user.mention}**"
        embed.set_footer(text="https://github.com/wraithfx/redbot-wraith")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def smug(self, ctx):
        """Be smug towards a user."""

        author = ctx.message.author
        images = await self.config.smug()

        smug = await self.fetch_nekos_life(ctx, "smug")
        images.extend(smug)

        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} is smug**"
        embed.set_footer(text="https://github.com/wraithfx/redbot-wraith")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)
       
    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def kill(self, ctx, *, user: discord.Member):
        """Kills a user."""

        author = ctx.message.author
        images = await self.config.kill()
        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} kills {user.mention}**"
        embed.set_footer(text="https://github.com/wraithfx/redbot-wraith")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def punch(self, ctx, *, user: discord.Member):
        """Punches a user."""

        author = ctx.message.author
        images = await self.config.punch()
        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} punches {user.mention}**"
        embed.set_footer(text="https://github.com/wraithfx/redbot-wraith")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    async def fetch_nekos_life(self, ctx, rp_action):

        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.nekos.dev/api/v3/images/sfw/gif/{rp_action}/?count=20") as resp:
                try:
                    content = await resp.json(content_type=None)
                except (ValueError, aiohttp.ContentTypeError) as ex:
                    log.debug("Pruned by exception, error below:")
                    log.debug(ex)
                    return []

        if content["data"]["status"]["code"] == 200:
            return content["data"]["response"]["urls"]
