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
import regex
import threading
import math


logger = logging.getLogger("tjbot.leveling")


r = redis.Redis(host='localhost', port=6379, decode_responses=True)

with open("levelconfig.json") as f:
    config = json.loads(f.read())

GROWTH_RATE = config.get("growth_rate")
BASE_XP = config.get("base_xp")
XP_PER_VALID_MESSAGE = config.get("xp_per_valid_message")
SPAM_XP_DEDUCTION = config.get("spam_xp_deduction")
VALID_MESSAGE_TIME = config.get("valid_message_time")

def get_xp_for_level(level: int) -> int:
    return int(BASE_XP * (GROWTH_RATE ** level - 1) / (GROWTH_RATE - 1))

def progress_bar(progress: float, length: int = 20) -> str:
    progress = max(0.0, min(1.0, progress))

    blocks = " ▏▎▍▌▋▊▉"
    total = progress * length

    full_blocks = int(total)
    fractional = round((total - full_blocks) * 8)

    if fractional == 8:
        full_blocks += 1
        fractional = 0

    empty_blocks = length - full_blocks - (fractional > 0)

    return (
        "█" * full_blocks
        + (blocks[fractional] if fractional else "")
        + " " * empty_blocks
    )

class LevelUser:
    def __init__(self, xp: int, level: int, eligible_messages_sent: int, total_messages_sent: int, last_eligible_message_timestamp: float, local_xp: int, local_xp_for_next_level: int):
        self.xp = xp
        self.level = level
        self.eligible_messages_sent = eligible_messages_sent
        self.total_messages_sent = total_messages_sent
        self.last_eligible_message_timestamp = last_eligible_message_timestamp
        self.local_xp = local_xp
        self.local_xp_for_next_level = local_xp_for_next_level
        self.local_xp_progress = local_xp / local_xp_for_next_level

def get_level_user(userid: int) -> LevelUser:
    eligible_messages_sent = int(r.get(f"tjbot:levels:{userid}:eligible_messages_sent") or 0)
    total_messages_sent =  int(r.get(f"tjbot:levels:{userid}:total_messages_sent") or 0)
    last_eligible_message_timestamp =  float(r.get(f"tjbot:levels:{userid}:last_eligible_message_timestamp") or 0)

    xp = (eligible_messages_sent * XP_PER_VALID_MESSAGE) - ((total_messages_sent-eligible_messages_sent) * SPAM_XP_DEDUCTION)

    level = max(0, int(math.log1p(xp * (GROWTH_RATE - 1) / BASE_XP) / math.log(GROWTH_RATE)))

    local_xp = xp - get_xp_for_level(level)
    local_xp_for_next_level = get_xp_for_level(level + 1) - get_xp_for_level(level)

    return LevelUser(
        xp,
        level,
        eligible_messages_sent,
        total_messages_sent,
        last_eligible_message_timestamp,
        local_xp,
        local_xp_for_next_level
    )

class Leveling(commands.Cog):
    def __init__(self, bot: commands.Bot) :
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        user = get_level_user(message.author.id)
        r.incr(f"tjbot:levels:{message.author.id}:total_messages_sent")
        if time.time() - user.last_eligible_message_timestamp > VALID_MESSAGE_TIME:
            r.set(f"tjbot:levels:{message.author.id}:last_eligible_message_timestamp", time.time())
            r.incr(f"tjbot:levels:{message.author.id}:eligible_messages_sent")
        
    @app_commands.command(description="get your level card :3")
    @app_commands.describe(
        user='[optional] what user to get',
    )
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def get_level(self, interaction: discord.Interaction, user: discord.User = None):
        if not user: user = interaction.user

        level_info = get_level_user(user.id)

        embed = discord.Embed()
        embed.color = discord.Color.blurple()

        embed.description = f"### {user.mention}'s Level Card"
        embed.add_field(name="Level", value=level_info.level)
        embed.add_field(name="Total XP Earned", value=level_info.xp)
        embed.add_field(name="Total Messages Sent", value=level_info.total_messages_sent, inline=False)
        embed.add_field(name="Current Progress", value=f"`{progress_bar(level_info.local_xp_progress)}` **{level_info.local_xp_progress*100:.2f}%**\n-# {level_info.local_xp}/{level_info.local_xp_for_next_level}XP", inline=False)

        embed.set_footer(text="XP is earned by chatting normally. Spamming messages or attempting to game the system will result in an XP deduction.")

        await interaction.response.send_message(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Leveling(bot))