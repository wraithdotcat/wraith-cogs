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
        default_global = {
            "hugs": [
                "https://i.imgur.com/FPvOYqa.gif",
                "https://i.imgur.com/QKxKEAS.gif",
                "https://i.imgur.com/ORpj4oh.gif",
                "https://i.imgur.com/zgMthmR.gif",
                "https://i.imgur.com/LFvZTXK.gif",
                "https://i.imgur.com/7iU9yKl.gif",
                "https://i.imgur.com/qWs53hx.gif",
                "https://i.imgur.com/cXQBhR8.gif",
                "https://i.imgur.com/jKWwoCP.gif",
                "https://i.imgur.com/QE7beNU.gif",
                "https://i.imgur.com/TPEaz1K.gif",
                "https://i.imgur.com/ERP0QBz.gif",
                "https://i.imgur.com/oXGxjDV.gif",
                "https://i.imgur.com/bgTPAb7.gif",
                "https://i.imgur.com/1UxrDyn.gif",
                "https://i.imgur.com/gaeEk33.gif",
                "https://i.imgur.com/xd9HvFF.gif",
                "https://i.imgur.com/rPF3Oe0.gif",
                "https://i.imgur.com/ClKOoEk.gif",
                "https://i.imgur.com/8CAlNEI.gif",
                "https://i.imgur.com/LNIFLtB.gif",
                "https://i.imgur.com/Y8SDkCb.gif",
                "https://i.imgur.com/QPXwNcA.gif",
                "https://i.imgur.com/HW9gfMz.gif",
                "https://i.imgur.com/Kh1z7qB.gif",
                "https://i.imgur.com/UERNFHD.gif",
                "https://i.imgur.com/z8KhrpB.gif",
                "https://i.imgur.com/fqHt7Gy.gif",
                "https://i.imgur.com/Pr6b9iU.gif",
                "https://i.imgur.com/56o6qlI.gif",
                "https://i.imgur.com/JjAgyfK.gif",
            ],
            "cuddle": [
                "https://i.imgur.com/AoUxZwe.gif",
                "https://i.imgur.com/YDkJ1Zk.gif",
                "https://i.imgur.com/jYOzJUD.gif",
                "https://i.imgur.com/5AKULoB.gif",
                "https://i.imgur.com/JqPgf05.gif",
                "https://i.imgur.com/rwvrqjT.gif",
                "https://i.imgur.com/UcbwNLj.gif",
                "https://i.imgur.com/CInJAGu.gif",
                "https://i.imgur.com/1lX1GCg.gif",
                "https://i.imgur.com/425uAS1.gif",
                "https://i.imgur.com/gupvoLu.gif",
                "https://i.imgur.com/FlZ2x3M.gif",
                "https://i.imgur.com/D00KyVg.gif",
                "https://i.imgur.com/UZ7BVXq.gif",
                "https://i.imgur.com/R78xquZ.gif",
                "https://i.imgur.com/3ZR8Cty.gif",
                "https://i.imgur.com/CJHyJ1m.gif",
                "https://i.imgur.com/0i3lgwE.gif",
                "https://i.imgur.com/sx2O2Cr.gif",
                "https://i.imgur.com/f1Exs7G.gif",
                "https://i.imgur.com/2X8e2b1.gif",
                "https://i.imgur.com/zs4oS0j.gif",
            ],
            "pat": [
                "https://i.imgur.com/Krbwuma.gif",
                "https://i.imgur.com/iHkJYzX.gif",
                "https://i.imgur.com/jFjuATR.gif",
                "https://i.imgur.com/s36dhpY.gif",
                "https://i.imgur.com/4yluT9x.gif",
                "https://i.imgur.com/daD1oDy.gif",
                "https://i.imgur.com/haJAkzh.gif",
                "https://i.imgur.com/Qv3p72M.gif",
                "https://i.imgur.com/smEoqaI.gif",
                "https://i.imgur.com/lkpSbWh.gif",
                "https://i.imgur.com/qtQb40i.gif",
                "https://i.imgur.com/zV0bw2l.gif",
                "https://i.imgur.com/f9nRmte.gif",
                "https://i.imgur.com/0vXbqks.gif",
                "https://i.imgur.com/16Ivt5t.gif",
                "https://i.imgur.com/0kemtyB.gif",
                "https://i.imgur.com/feQa4yA.gif",
                "https://i.imgur.com/JD37S4l.gif",
                "https://i.imgur.com/93IkVQV.gif",
                "https://i.imgur.com/o7zNG88.gif",
                "https://i.imgur.com/jy3AMFH.gif",
                "https://i.imgur.com/gT8lBRI.gif",
                "https://i.imgur.com/1b6h74a.gif",
                "https://i.imgur.com/eJmG6CZ.gif",
                "https://i.imgur.com/8x2tc9W.gif",
                "https://i.imgur.com/4giD9G6.gif",
                "https://i.imgur.com/k1PCssc.gif",
                "https://i.imgur.com/P3n1xdV.gif",
                "https://i.imgur.com/8Uzbd31.gif",
                "https://i.imgur.com/qNEaX3v.gif",
                "https://i.imgur.com/UFuOmuK.gif",
            ],
            "highfive": [
                "https://i.imgur.com/KbU5Pft.gif",
                "https://i.imgur.com/msaAy1n.gif",
                "https://i.imgur.com/3doLDJr.gif",
                "https://i.imgur.com/Nrs9aD2.gif",
                "https://i.imgur.com/eR0UT2B.gif",
                "https://i.imgur.com/yRP8dLA.gif",
                "https://i.imgur.com/XUs5sJW.gif",
                "https://i.imgur.com/jblvzO2.gif",
                "https://i.imgur.com/HIs6iaL.gif",
                "https://i.imgur.com/2hrqVm2.gif",
                "https://i.imgur.com/rH6WPu9.gif",
                "https://i.imgur.com/tct5DZY.gif",
            ],
            "poke": [
                "https://i.imgur.com/QW0DTro.gif",
                "https://i.imgur.com/65DeDmw.gif",
                "https://i.imgur.com/BsvwZ51.gif",
                "https://i.imgur.com/WIXpOBw.gif",
                "https://i.imgur.com/C7YY0Kw.gif",
                "https://i.imgur.com/wK0gTyH.gif",
                "https://i.imgur.com/r9BSt4r.gif",
                "https://i.imgur.com/gr3dZn6.gif",
            ],
            "tickle": [
                "https://i.imgur.com/lfWmiz1.gif",
                "https://i.imgur.com/pd74qBN.gif",
                "https://i.imgur.com/eVzjWLH.gif",
            ],
            "kiss": [
                "https://i.imgur.com/r4iBI92.gif",
                "https://i.imgur.com/G9I8KD6.gif",
                "https://i.imgur.com/iwBcqBe.gif",
                "https://i.imgur.com/0DygwFd.gif",
                "https://i.imgur.com/mZ9RecX.gif",
                "https://i.imgur.com/NIqCpgb.gif",
            ],
            "lick": [
                "https://i.imgur.com/MPZPNai.gif",
                "https://i.imgur.com/jVj7x9S.gif",
                "https://i.imgur.com/aTVHfBu.gif",
                "https://i.imgur.com/UYHypBp.gif",
                "https://i.imgur.com/LkCJ2Xt.gif",
                "https://i.imgur.com/KvhzX8f.gif",
                "https://i.imgur.com/DsBeUy3.gif",
                "https://i.imgur.com/OYoRz58.gif",
                "https://i.imgur.com/NBFtHD4.gif",
                "https://i.imgur.com/q8GDISZ.gif",
                "https://i.imgur.com/q8GDISZ.gif",
            ],
            "feed": [
                "https://i.imgur.com/8Tq7KJL.gif",
                "https://i.imgur.com/i9WaXtI.gif",
                "https://i.imgur.com/1qTADFG.gif",
                "https://i.imgur.com/f7Iu5RS.gif",
                "https://i.imgur.com/rzbXbfZ.gif",
                "https://i.imgur.com/Nlg2x4q.gif",
                "https://i.imgur.com/FrYwLM3.gif",
                "https://i.imgur.com/XgOMoea.gif",
                "https://i.imgur.com/GKo090F.gif",
                "https://i.imgur.com/iJeyFdK.gif",
                "https://i.imgur.com/U5L8E7K.gif",

            ],
            "smug": [
                "https://i.imgur.com/MMOdvqe.gif",
                "https://i.imgur.com/OCK5Ov3.gif",
                "https://i.imgur.com/l0i4eEn.gif",
                "https://i.imgur.com/pnUmJKN.gif",
                "https://i.imgur.com/ApQ1w7Z.gif",
                "https://i.imgur.com/zepBEpi.gif",
            ],
            "kill": [
                "https://i.imgur.com/ieHshhZ.gif",
                "https://i.imgur.com/wfzqB4x.gif",
                "https://i.imgur.com/K0xevPY.gif",
                "https://i.imgur.com/7wBThnE.gif",
            ],
            "slap": [
                "https://i.imgur.com/rKRaycj.gif",
                "https://i.imgur.com/OlBxOml.gif",
                "https://i.imgur.com/6sw5ucL.gif",
                "https://i.imgur.com/Fjnsf0j.gif",
                "https://i.imgur.com/RngQv7u.gif",
                "https://i.imgur.com/SADBEV3.gif",
                "https://i.imgur.com/Ox31Msx.gif",
                "https://i.imgur.com/cDoPe2x.gif",
                "https://i.imgur.com/oAL4wXL.gif",
                "https://i.imgur.com/UFuTW36.gif",
                "https://i.imgur.com/VKBwwhR.gif",
                "https://i.imgur.com/1Yy3zaH.gif",
                "https://i.imgur.com/ZUZfBsi.gif",
                "https://i.imgur.com/48eOb2A.gif",
                "https://i.imgur.com/hTEQFHL.gif",
                "https://i.imgur.com/hzWtwzj.gif",
                "https://i.imgur.com/Mc707zy.gif",
                "https://i.imgur.com/tsM8C6X.gif",
                "https://i.imgur.com/7cawfm0.gif",
                "https://i.imgur.com/XmnjuIq.gif",
                "https://i.imgur.com/CizyEdQ.gif",
                "https://i.imgur.com/GMABVCv.gif",
                "https://i.imgur.com/4wW750X.gif",
                "https://i.imgur.com/4F7Ycdo.gif",
                "https://i.imgur.com/Slv4ihq.gif",
                "https://i.imgur.com/q5o6DB8.gif",
                "https://i.imgur.com/eJSIQ0A.gif",
                "https://i.imgur.com/mzhSHvb.gif",
                "https://i.imgur.com/8XBRbGO.gif",
                "https://i.imgur.com/Kro76dL.gif",
                "https://i.imgur.com/A5abqyF.gif",
                "https://i.imgur.com/K9UEId7.gif",
                "https://i.imgur.com/YaInrP4.gif",
            ],
            "punch": [
                "https://i.imgur.com/92N5CE2.gif",
                "https://i.imgur.com/IFqj65R.gif",
                "https://i.imgur.com/ccurJOw.gif",
                "https://i.imgur.com/xK9xLTJ.gif",
            ],
        }
        self.config.register_global(**default_global)

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
