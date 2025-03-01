import discord
from discord import app_commands
from discord.ext import commands
import requests
import time
import json
import random
import discord
from discord.ext import commands
from discord import app_commands
from discord.ext import tasks
import asyncio
from threading import Thread
import hashlib
import base64
from enum import Enum

class EvalModal(discord.ui.Modal, title='Eval this shit'):
        prompt = discord.ui.TextInput(
            label='Eval this shit',
            style=discord.TextStyle.long,
            placeholder='TOKEN',
            required=True,
            max_length=500,
        )

        async def on_submit(self, interaction: discord.Interaction):
            if interaction.user.name == "tjc472":
                output = str(eval(self.prompt.value))
            else:
                output = "idk i dont want to rn"
            await interaction.response.send_message(content=output)



class Dev(commands.Cog):
    def __init__(self, bot: commands.Bot) :
        self.bot = bot





    @app_commands.command(description="Developer utilities and debug :3")
    @app_commands.describe(
        prompt='dev prompt following the tjdev standard'
    )
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def dev(self, interaction: discord.Interaction, prompt: str):
        await interaction.response.send_message(content=f"-# {interaction.user.name}({interaction.user.nick})\n-# Devutils\n<a:loading2:1296923111177850931>`Please wait... Running checks...`")#, ephemeral=True)
        if True: #interaction.user.name == "tjc472":
            if prompt == "q":
                await interaction.edit_original_response(content=f"-# {interaction.user.name}({interaction.user.nick})\n-# Devutils\n-# Message search\n-# Random quote:\n<a:loading2:1296923111177850931>`Please wait... Searching logs...`")
                f = open("log.txt")
                quotes = f.read()
                f.close()
                quotes = quotes.split("\n")
                f = open("quoteblacklist.txt")
                quoteblacklist = f.read()
                f.close()
                quoteblacklist = quoteblacklist.split("\n")
                search = True
                searchattempts = 0
                while search:
                    try:
                        quote = random.choice(quotes)
                        quoteduser = quote.split(": ")[0]
                        quotedmessage = quote.split(": ")[1].replace("@everyone", "").replace("@here", "").replace("[lb]", "\n")
                        if quoteduser.split("(", 1)[0] in quoteblacklist:
                            search = True
                        else:
                            search = False
                    except:
                        pass
                    searchattempts = searchattempts + 1
                    if searchattempts > 50000000:
                        search = False
                        quotedmessage = "`No Quote found(Timed out)`"
                        quoteduser = "`Error`"
                    if searchattempts == 10000000:
                        await interaction.edit_original_response(content=f"-# {interaction.user.name}({interaction.user.nick})\n-# Devutils\n-# Message search\n-# Random quote:\n<a:loading2:1296923111177850931>`Please wait... Searching logs... 10000000 Messages Searched`")
                    if searchattempts == 20000000:
                        await interaction.edit_original_response(content=f"-# {interaction.user.name}({interaction.user.nick})\n-# Devutils\n-# Message search\n-# Random quote:\n<a:loading2:1296923111177850931>`Please wait... Searching logs... 20000000 Messages Searched`")
                    if searchattempts == 30000000:
                        await interaction.edit_original_response(content=f"-# {interaction.user.name}({interaction.user.nick})\n-# Devutils\n-# Message search\n-# Random quote:\n<a:loading2:1296923111177850931>`Please wait... Searching logs... 30000000 Messages Searched`")
                    if searchattempts == 40000000:
                        await interaction.edit_original_response(content=f"-# {interaction.user.name}({interaction.user.nick})\n-# Devutils\n-# Message search\n-# Random quote:\n<a:loading2:1296923111177850931>`Please wait... Searching logs... 40000000 Messages Searched Cancelling soon...`")
                await interaction.edit_original_response(content=f"-# Devutils\n-# Message search\n-# Quote from {quoteduser}:\n{quotedmessage}")
            elif prompt.startswith("s="):
                searchterm = prompt.split("s=", 1)[1]
                f = open("log.txt")
                quotes = f.read()
                f.close()
                quotes = quotes.split("\n")
                results = []
                for message in quotes:
                    if searchterm in message:
                        results.append(message)
                resultamount = len(results)
                results = []
                cancel = False
                for message in quotes:
                    if searchterm in message:
                        results.append(message)
                    if len(results) > 9:
                        break
                    output = ""
                    for result in results:
                        output = output + "```" + result + "```"
                    if len(output) > 2000:
                        cancel = True
                        break
                output = ""
                for result in results:
                    output = output + "```" + result + "```"
                if len(results) == 0:
                    output = "\nNothing found"
                if not cancel:
                    await interaction.edit_original_response(content=f"-# {interaction.user.name}({interaction.user.nick})\n-# Devutils\n-# Message search\n`{resultamount} Results:`\n{output}")
                else:
                    await interaction.edit_original_response(content=f"-# {interaction.user.name}({interaction.user.nick})\n-# Devutils\n-# Message search\n`{resultamount} Potential Results`\nOutput too long for message.")
            else:
                if prompt.startswith("m="):
                    requestlogchannel = self.bot.get_channel(1326278694200676396)
                    searchterm = prompt.split("m=", 1)[1]
                    await requestlogchannel.send(searchterm)
                    await interaction.edit_original_response(content=f"-# {interaction.user.name}({interaction.user.nick})\n-# Devutils\nSent Message successfully")
                else:
                    if prompt == "penis":
                        await interaction.edit_original_response(content=f"-# {interaction.user.name}({interaction.user.nick})\n-# Devutils\nThe penis game has (not) been activated")
                    else:
                        await interaction.edit_original_response(content=f"-# {interaction.user.name}({interaction.user.nick})\n-# Devutils\n`Invalid Prompt!`\nDid you misspell something?")
        else:
            await interaction.edit_original_response(content=f"-# {interaction.user.name}({interaction.user.nick})\n-# Devutils\n`No permission!`")

    @app_commands.command(description="Developer utilities and debug :3")
    @app_commands.describe(
        prompt='dev prompt following the tjdev standard'
    )
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def eval(self, interaction: discord.Interaction, prompt: str=""):
            if interaction.user.name == "tjc472":
                await interaction.response.send_modal(EvalModal())
            else:
                await interaction.response.send_message(content="idk i dont want to rn")

async def setup(bot: commands.Bot):
    await bot.add_cog(Dev(bot))
