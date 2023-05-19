import os
import json
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
    """Visualize how you feel about another server member!"""

    def __init__(self):
        self.config = Config.get_conf(self, identifier=842364413)

        absolute_path = os.path.dirname(__file__)
        relative_file = "images.json"
        full_path = os.path.join(absolute_path, relative_file)

        with open(full_path) as file:
            images = json.load(file)

        self.config.register_global(**images)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def hugs(self, ctx, *, user: discord.Member):
        """Hugs a user."""

        author = ctx.message.author
        images = await self.config.hugs()
        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} hugs {user.mention}**"
        embed.set_footer(text="レイス - \"Everything you can imagine is real.\"")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def cuddle(self, ctx, *, user: discord.Member):
        """Cuddles a user."""

        author = ctx.message.author
        images = await self.config.cuddle()
        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} cuddles {user.mention}**"
        embed.set_footer(text="レイス - \"Everything you can imagine is real.\"")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def kiss(self, ctx, *, user: discord.Member):
        """Kisses a user."""

        author = ctx.message.author
        images = await self.config.kiss()
        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} kisses {user.mention}**"
        embed.set_footer(text="レイス - \"Everything you can imagine is real.\"")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def slap(self, ctx, *, user: discord.Member):
        """Slaps a user."""

        author = ctx.message.author
        images = await self.config.slap()
        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} slaps {user.mention}**"
        embed.set_footer(text="レイス - \"Everything you can imagine is real.\"")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def pat(self, ctx, *, user: discord.Member):
        """Pats a user."""

        author = ctx.message.author
        images = await self.config.pat()
        mn = len(images)
        i = randint(0, mn - 1)
        
        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} pats {user.mention}**"
        embed.set_footer(text="レイス - \"Everything you can imagine is real.\"")
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
        embed.set_footer(text="レイス - \"Everything you can imagine is real.\"")
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
        embed.set_footer(text="レイス - \"Everything you can imagine is real.\"")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def feed(self, ctx, *, user: discord.Member):
        """Feeds a user."""

        author = ctx.message.author
        images = await self.config.feed()
        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} feeds {user.mention}**"
        embed.set_footer(text="レイス - \"Everything you can imagine is real.\"")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def tickle(self, ctx, *, user: discord.Member):
        """Tickles a user."""

        author = ctx.message.author
        images = await self.config.tickle()
        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} tickles {user.mention}**"
        embed.set_footer(text="レイス - \"Everything you can imagine is real.\"")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def poke(self, ctx, *, user: discord.Member):
        """Pokes a user."""

        author = ctx.message.author
        images = await self.config.poke()
        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} pokes {user.mention}**"
        embed.set_footer(text="レイス - \"Everything you can imagine is real.\"")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)

    @commands.command()
    @commands.bot_has_permissions(embed_links=True)
    async def smug(self, ctx):
        """Be smug towards a user."""

        author = ctx.message.author
        images = await self.config.smug()
        mn = len(images)
        i = randint(0, mn - 1)

        # Build Embed
        embed = discord.Embed()
        embed.description = f"**{author.mention} is smug**"
        embed.set_footer(text="レイス - \"Everything you can imagine is real.\"")
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
        embed.set_footer(text="レイス - \"Everything you can imagine is real.\"")
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
        embed.set_footer(text="レイス - \"Everything you can imagine is real.\"")
        embed.set_image(url=images[i])
        await ctx.send(embed=embed)