import discord
from discord.ext import commands
import os
import youtube_dl
import asyncio

from .utils import checks
from .utils import mysql


class Audio(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="Show soudbyte commands", description="Show available soudbyte commands", hidden=False)
    async def audio(self, ctx: commands.Context):
        embed = discord.Embed(
            title="Audio Commands", 
            description="All soundbytes cost 20 gaybucks to use.",
            color=discord.Color.blue()
        )

        description = str()

        for command in self.get_commands():
            if command.name == "audio":
                continue

            description += f"**{command.name}** - {command.description}\n"

        embed.add_field(name="\u200b", value=description, inline=False)

        await ctx.send(embed=embed)

    # @commands.command()
    # async def youtube(ctx, *, search):
    #     query_string = parse.urlencode({'search_query': search})
    #     html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    #     # print(html_content.read().decode())
    #     search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    #     print(search_results)
    #     # I will put just the first result, you can loop the response to show more results
    #     await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

    # todo Make this functional as a bot command. How to disconnect?? Don't know how to realize when audio is finished
    
    async def play(self, ctx: commands.Context, url: str, name: str, channel: discord.VoiceChannel, wait: int = 60 * 5):
        checks.is_valid_bet(ctx, ctx.author, 20)

        is_there = os.path.isfile(f"./tracks/{name}")
        if not is_there:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': f'./tracks/{name}',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192'
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            return ctx.send("I'm already playing something. Wait a sec")

        await channel.connect()

        voice.play(discord.FFmpegPCMAudio(source=f"./tracks/{name}"))

        await asyncio.sleep(wait)
        await voice.disconnect()

        mysql.update_balance(ctx.author, 20)

    @commands.command(brief="Soudbyte", description="What are you aiming at?")
    async def aim(self, ctx: commands.Context):
        channel = ctx.guild.voice_channels[0]
        await self.play(ctx, url="https://youtu.be/VoOxzT1ngeM", name="aim.mp3", channel=channel, wait=5)

    @commands.command(brief="Soudbyte", description="It smells like bitch in here.")
    async def bitch(self, ctx: commands.Context):
        channel = ctx.guild.voice_channels[0]
        await self.play(ctx, url="https://youtu.be/ppxmxVhkr7c", name="bitch.mp3", channel=channel, wait=5)

    @commands.command(brief="Soudbyte", description="Lord have mercy.")
    async def bust(self, ctx: commands.Context):
        channel = ctx.guild.voice_channels[0]
        await self.play(ctx, url="https://youtu.be/jzge_j-_PME", name="bust.mp3", channel=channel, wait=5)

    @commands.command(brief="Soudbyte", description="You just have to say that you're fine.")
    async def fine(self, ctx: commands.Context):
        channel = ctx.guild.voice_channels[0]
        await self.play(ctx, url="https://youtu.be/77sS5IuR0Gs", name="fine.mp3", channel=channel, wait=7)

    @commands.command(brief="Soudbyte", description="Plays the 'get your shit together' scene from Rick and Morty.")
    async def morty(self, ctx: commands.Context):
        channel = ctx.guild.voice_channels[0]
        await self.play(ctx, url="https://youtu.be/UYKKQn3WXh0", name="morty.mp3", channel=channel, wait=21)

    @commands.command(brief="Soudbyte", description="Plays audio from the 'It's Wednesday my dudes' scream.")
    async def nut(self, ctx: commands.Context):
        channel = ctx.guild.voice_channels[0]
        await self.play(ctx, url="https://youtu.be/dlRKA1nirrg", name="nut.mp3", channel=channel, wait=4)

    @commands.command(brief="Soudbyte", description="Plays audio from the death sound in Roblox.")
    async def oof(self, ctx: commands.Context):
        channel = ctx.guild.voice_channels[0]
        await self.play(ctx, url="https://youtu.be/3w-2gUSus34", name="oof.mp3", channel=channel, wait=3)

    @commands.command(brief="Soudbyte", description="Plays TikTok sheesh sound.")
    async def sheesh(self, ctx: commands.Context):
        channel = ctx.guild.voice_channels[0]
        await self.play(ctx, url="https://youtu.be/hRj1VyUsVjw", name="sheesh.mp3", channel=channel, wait=13)

    @commands.command(brief="Soudbyte", description="Plays audio from this dude having a real good time while cooking.")
    async def sogood(self, ctx: commands.Context):
        channel = ctx.guild.voice_channels[0]
        await self.play(ctx, url="https://youtu.be/-FrpuPLYnvY", name="sogood.mp3", channel=channel, wait=17)

    @commands.command(brief="Soudbyte", description="Plays audio from the 'Damn, this n\*\*\*\* spitting' meme")
    async def spitting(self, ctx: commands.Context):
        channel = ctx.guild.voice_channels[0]
        await self.play(ctx, url="https://youtu.be/xuLfu0z5_m0", name="spitting.mp3", channel=channel, wait=5)

    @commands.command(brief="Soudbyte", description="Plays audio from the spongebob heckler.")
    async def stinks(self, ctx: commands.Context):
        channel = ctx.guild.voice_channels[0]
        await self.play(ctx, url="https://youtu.be/ppb8A5QqPj8", name="stinks.mp3", channel=channel, wait=4)

    @commands.command(brief="Soudbyte", description="Begone...")
    async def thot(self, ctx: commands.Context):
        channel = ctx.guild.voice_channels[0]
        await self.play(ctx, url="https://youtu.be/tyrKeThaEJM", name="thot.mp3", channel=channel, wait=5)

    @commands.command(brief="Soudbyte", description="Uh oh stinky")
    async def uhoh(self, ctx: commands.Context):
        channel = ctx.guild.voice_channels[0]
        await self.play(ctx, url="https://youtu.be/PJNBJAYFyKE", name="uhoh.mp3", channel=channel, wait=5)

    @commands.command(brief="Soudbyte", description="Plays audio from a guy hitting a real nice yeet.")
    async def yeet(self, ctx: commands.Context):
        channel = ctx.guild.voice_channels[0]
        await self.play(ctx, url="https://youtu.be/won6qew1da4", name="yeet.mp3", channel=channel, wait=7)


async def setup(bot):
    await bot.add_cog(Audio(bot))
