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
import datetime


logger = logging.getLogger("tjbot.tjsapphire")



r = redis.Redis(host='localhost', port=6379, decode_responses=True)

with open("tjsapphire.json") as f:
    config = json.loads(f.read())

CHECKMARKSAPPH = config.get("checkmark")
PROOFVERIFIED = config.get("proofverified")
LOADING = config.get("loading")

actions = {
    "ban": "banned",
    "mute": "muted",
    "warn": "warned",
    "kick": "kicked",
    "unban": "unbanned",
    "unmute": "unmuted",
    "unkick": "unkicked",
    "unwarn": "unwarned",
    "cliff": "thrown off a fucking cliff",
    "torture": "tortured",
    "neck": "got their neck twisted till they fucking died",
    "kill": "killed",
    "explode": "exploded",
    "muta": "mutad",
    "bam": "bammed",
    "warm": "warmed",
    "nuke": "nuked",
    "bigshot": "now has a chance to be a [[BIG SHOT]]",
    "van": "has been thrown in a suspicious van",
    "demote": "demoted", # do NOT run this command on tjc
    "promote": "promoted",
    "smash": "smashed (AS IN DESTROYED YOU PERVERTED FUCK)",
    "cdc": "put in a cdc disk ca- *gets shot*",
    "tropicalmeow": "<a:KingPat:1277609556142456952>ed",
    "dod": "died due to the cause of death", # <------ CREDIT TO MOONSTAR FOR THIS IDEA
    "dieofdeath": "died of death",
    "boop": "booped",
    "bean": "beaned",
    "dermute": "dermuted",
    "dermote": "dermoted",
    "nullscape": """nullsca- 

CBF DETECTED, LOSER!

CLICK BETWEEN FRAMES IS ILLEGITIMATE AND WILL NOT BE ALLOWED FOR USE IN TJBOT. PLEASE DISABLE THE MOD IN ORDER TO CONTINUE PLAYING.
""",
    "mart....slide!": "Mart. The Waterimp: Hi! I am Mart. The Waterimp! I don't know what i should say...",
    "bonk": "bonked",
    "wmoon": "W moon",
    "olck": "Command not found\n> There's no command called `olck`",
    "loink": "zoinks! its the slop content\n-# ZOINK REFERENCE????\n> I VERIFIED THE GOLDEN LET'S GO wait no was that nswish",
    "goog": "<:goog:1445140537911804046>'ed",
    "mediaban": "media banned",
    "tikiphonk": "No.",
    "67": "doot doot six seven'ed",
    "meow": "im a silly little kitty cat :3 mrrp meow nyaa mrow ^_^"
}

cool_people = [1045761412489809975, 998995432132853891, 808528986970783746, 1291086017981317201, 930947671592697876]


class Tjsapphire(commands.Cog):
    def __init__(self, bot: commands.Bot) :
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
            if not message.guild:
                return
            if not int(r.get(f"""tjservices:settings:{message.guild.id}:tjsapphire_enabled""") or "1"):
                return
            prefix = r.get(f"""tjservices:settings:{message.guild.id}:tjsapphire_prefix""") or r"s\!"

            if message.content.startswith(r"st!actions"):
                string1 = ""
                for i in actions:
                    string1 = string1 + f"\n> `s\\!{i}` -> {actions[i]}"
                #await message.reply(f"All Sapphire actions:\n-# Backslash MUST be included for it to register, non inclusion could cause unwanted consequences!{string1}")

            if message.content.startswith(prefix):
                if message.channel.permissions_for(message.author).ban_members or message.author.id in cool_people:
                    actionid = message.content.split(" ")[0].replace(prefix, "")
                    if actionid in actions:
                        action = actions[actionid]
                    else: return
                    await message.add_reaction(LOADING)
                    await asyncio.sleep(3)
                    proof = None
                    duration = "Permanent"
                    if message.reference:
                        ref = await message.channel.fetch_message(message.reference.message_id)
                        usermention = ref.author.mention
                        proof = ref.content
                        reason = message.content.split(" ", 1)[1] if len(message.content.split(" "))>=2 else "No reason provided"
                    else:
                        usermention = message.content.split(' ', 2)[1] if len(message.content.split(" "))>=3 else message.content.split(' ', 1)[1]
                        reason = message.content.split(" ", 2)[2] if len(message.content.split(" "))>=3 else "No reason provided"
                    if ";" in reason:
                        duration = reason.split(";", 1)[0]
                        reason = reason.split(";", 1)[1]
                    if actionid == "demote" and ("1045761412489809975" in usermention or "tjc" in usermention):
                        await message.add_reaction("❌")
                        return
                    embed = discord.Embed()
                    embed.timestamp = datetime.datetime.now()
                    embed.description = f"""{CHECKMARKSAPPH} {usermention} {action}\n> **Reason:** {reason}\n> **Duration:** {duration}\n{f"> {PROOFVERIFIED}**Proof:** {proof} ([Link](https://discord.com/channels/{ref.guild.id}/{ref.channel.id}/{ref.id}))" if proof else ""}"""
                    embed.set_footer(text=f"@{message.author.name}", icon_url=message.author.avatar.url)
                    embed.color = discord.Colour.from_rgb(54, 206, 54)
                    try:
                        await message.delete()
                    except:
                        await message.send(":warning: TJBot does not have the `manage messages` permission needed for this command! Please grant TJBot the permission and try again.")
                        return
                    try:
                        temp_webhook = await message.channel.create_webhook(name="TJBot-temp-webhook")
                    except:
                        await message.channel.send(":warning: TJBot does not have the `create webhooks` permission needed for this command! Please grant TJBot the permission and try again.")
                        return
                    # sapphire pfp: https://de-1.tjcsucht.net/leb/LwB8-37e0fb2dcf8d219aa92bf02f47ea60eb.webp
                    await temp_webhook.send(embed=embed, username="geode sdk" if message.guild.id == 1268365327058599968 else "Sapphire", avatar_url="https://de-1.tjcsucht.net/leb/LwB8-37e0fb2dcf8d219aa92bf02f47ea60eb.webp", wait=True)
                    try:
                        # temp_webhook might not exist if exception raised earlier
                        if 'temp_webhook' in locals() and temp_webhook:
                            await temp_webhook.delete()
                    except :
                        await message.send(":warning: Webhook could not be deleted")

async def setup(bot: commands.Bot):
    await bot.add_cog(Tjsapphire(bot))