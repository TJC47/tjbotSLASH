import discord
from discord import app_commands
from discord.ext import commands
import discord


class Sapph(commands.Cog):
    def __init__(self, bot: commands.Bot) :
        self.bot = bot




    @app_commands.command(description="Kill someone :3")
    @app_commands.describe(
        killee='person to kill',
        reason='reason'
    )
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def kill(self, interaction: discord.Interaction, killee: discord.User, reason: str='No reason provided'):
        embed = discord.Embed()
        embed.add_field(name=f"<:checkmarksapph:1309669307214598265> @{killee.name} killed", value="\n> **Reason**: " + reason + "\n> **Duration**: Permanent", inline=False)
        embed.set_footer(text="le epically trolled")
        embed.color = discord.Colour.from_rgb(54, 206, 54)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(description="Explode someone :3")
    @app_commands.describe(
        explodee='person to explode',
        reason='reason'
    )
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def explode(self, interaction: discord.Interaction, explodee: discord.User, reason: str='No reason provided'):
        embed = discord.Embed()
        embed.add_field(name=f"<:checkmarksapph:1309669307214598265> {explodee.name} exploded", value="\n> **Reason**: " + reason + "\n> **Duration**: Permanent", inline=False)
        embed.set_footer(text="le epically trolled")
        embed.color = discord.Colour.from_rgb(54, 206, 54)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(description="Hug someone :3")
    @app_commands.describe(
        hugee='person to hug',
        reason='reason'
    )
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def hug(self, interaction: discord.Interaction, hugee: discord.User, reason: str='No reason provided'):
        embed = discord.Embed()
        embed.add_field(name=f"<:checkmarksapph:1309669307214598265> @{hugee.name} hugged", value="\n> **Reason**: " + reason + "\n> **Duration**: mrowww :3", inline=False)
        embed.set_footer(text="prrrr :3")
        embed.color = discord.Colour.from_rgb(54, 206, 54)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(description="Newgen someone :3")
    @app_commands.describe(
        newgenee='person to newgen',
        reason='reason'
    )
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def newgen(self, interaction: discord.Interaction, newgenee: discord.User, reason: str='No reason provided'):
        embed = discord.Embed()
        embed.add_field(name=f"<:checkmarksapph:1309669307214598265> @{newgenee.name} is a newgen", value="\n> **Reason**: " + reason + "\n> **Duration**: Permanent", inline=False)
        embed.set_footer(text="le epically trolled")
        embed.color = discord.Colour.from_rgb(54, 206, 54)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(description="Whatever you want someone :3")
    @app_commands.describe(
        actionee='person to whatever you want',
        action='what to do in the past tense something',
        reason='reason',
        duration='duration'
    )
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def customaction(self, interaction: discord.Interaction, actionee: discord.User, action: str, reason: str='No reason provided', duration: str='Permanent'):
        embed = discord.Embed()
        embed.add_field(name=f"<:checkmarksapph:1309669307214598265> @{actionee.name} {action}", value="\n> **Reason**: " + reason + "\n> **Duration**: " + duration, inline=False)
        embed.set_footer(text="le epically trolled")
        embed.color = discord.Colour.from_rgb(54, 206, 54)
        await interaction.response.send_message(embed=embed)



async def setup(bot: commands.Bot):
    await bot.add_cog(Sapph(bot))