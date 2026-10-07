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

with open("feedbackwebhook.sensitive") as f:
    FEEDBACK_WEBHOOK_URL = f.read()

logger = logging.getLogger("tjbot.feedback")



r = redis.Redis(host='localhost', port=6379, decode_responses=True)

class Feedback(commands.Cog):
    def __init__(self, bot: commands.Bot) :
        self.bot = bot

    @app_commands.command(description="give feedback to tjbot developers :3")
    @app_commands.describe(
        feedback='what feedback to give',
    )
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def feedback(self, interaction: discord.Interaction, feedback: str):
        await interaction.response.defer()
        feedback_webhook = discord.Webhook.from_url(FEEDBACK_WEBHOOK_URL, client=self.bot)
        embed = discord.Embed()
        embed.title = "Feedback received!"
        embed.add_field(name="Feedback Content", value=feedback, inline=False)
        embed.set_footer(text=f"@{interaction.user.name}", icon_url=interaction.user.avatar.url)
        embed.color = discord.Colour.from_rgb(54, 206, 54)
        await feedback_webhook.send(embed=embed)
        await interaction.edit_original_response(content="Feedback sent!")

async def setup(bot: commands.Bot):
    await bot.add_cog(Feedback(bot))