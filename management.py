import discord
from discord import app_commands
from discord.ext import commands
import requests
import time
import json
import random
import discord
import logging
import asyncio
import aiohttp
import urllib.request
import subprocess
import os
import redis
import string



logger = logging.getLogger("tjbot.management")



r = redis.Redis(host='localhost', port=6379, decode_responses=True)

class Management(commands.GroupCog, group_name="management"):
    def __init__(self, bot: commands.Bot) :
        self.bot = bot

    @app_commands.command(description="open tjbot dashboard :3")
    @app_commands.allowed_installs(guilds=True, users=False)
    @app_commands.allowed_contexts(guilds=True, dms=False, private_channels=False)
    async def dashboard(self, interaction: discord.Interaction):
        if not interaction.user.guild_permissions.manage_guild and not await self.bot.is_owner(interaction.user):
            await interaction.response.send_message(content="You need the `manage server` permission to access the TJBot dashboard!")
            return
        await interaction.response.defer(ephemeral=True)

        code = "".join(random.choices(string.ascii_letters + string.digits, k=6))

        code_info = {
            "server_id": interaction.guild.id,
            "server_name": interaction.guild.name,
            "user_id": interaction.user.id,
            "user_name": interaction.user.name,
            "created_time": time.time(),
            "roles": list(r.name for r in interaction.guild.roles)
        }
        
        logger.debug(code_info)

        r.set(f"tjbot:dashboard:management_code:{code}", json.dumps(code_info), ex=3600)

        embed = discord.Embed()
        embed.title = "Dashboard"
        embed.add_field(name="How to access", value="Click [this](https://tjcsucht.net/tjbot_login) link to open the dashboard website.", inline=False)
        embed.add_field(name="Your management code", value=f"```text\n{code}```\n-# Do **NOT** share this code with ***ANYONE***, as this code gives permission to edit **ALL** TJBot settings for this server.", inline=False)
        embed.set_footer(text=f"@{interaction.user.name}", icon_url=interaction.user.avatar.url)
        embed.color = discord.Colour.from_rgb(54, 206, 54)
        await interaction.edit_original_response(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Management(bot))