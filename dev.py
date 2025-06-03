import discord
from discord import app_commands
from discord.ext import commands
import requests
import time
import random
import discord
from io import StringIO
from contextlib import redirect_stdout

class EvalModal(discord.ui.Modal, title = 'Eval this shit'):
    prompt = discord.ui.TextInput(
        label = 'Eval this shit',
        style = discord.TextStyle.long,
        placeholder = 'TOKEN',
        required = True,
        max_length = 2000,
    )

    async def on_submit(self, interaction: discord.Interaction):
        if interaction.user.name == "tjc472":
            try:
                output = str(eval(self.prompt.value))
            except:
                output = "what if you read https://www.w3schools.com/python/default.asp"
        else:
            output = "idk i dont want to rn"
        await interaction.response.send_message(content=output)

class ExecModal(discord.ui.Modal, title = 'Exec this shit'):
    prompt = discord.ui.TextInput(
        label = 'Exec this shit',
        style = discord.TextStyle.long,
        placeholder = 'TOKEN(wont work here)',
        required = True,
        max_length = 4000,
    )

    async def on_submit(self, interaction: discord.Interaction):
        if interaction.user.name == "tjc472":
            try:
                f = StringIO()
                with redirect_stdout(f):
                    exec(self.prompt.value, globals())
                output = f.getvalue()
            except:
                output = "what if you read https://www.w3schools.com/python/default.asp"
        else:
            output = "idk i dont want to rn"
        await interaction.response.send_message(content = f"```ansi\n{output}```")




class Dev(commands.Cog):
    def __init__(self, bot: commands.Bot) :
        self.bot = bot





    @app_commands.command(description="Developer utilities and debug :3")
    @app_commands.describe(
        prompt='dev prompt following the tjdev standard'
    )
    @app_commands.allowed_installs(guilds = True, users = True)
    @app_commands.allowed_contexts(guilds = True, dms = True, private_channels = True)
    async def dev(self, interaction: discord.Interaction, prompt: str):
        await interaction.response.send_message(content = f"-# {interaction.user.name}({interaction.user.nick})\n-# Devutils\n<a:loading2:1296923111177850931>`Please wait... Running checks...`")
        if True: #interaction.user.name == "tjc472":
            if prompt == "q":
                await interaction.edit_original_response(content = f"-# {interaction.user.name}({interaction.user.nick})\n-# Devutils\n-# Message search\n-# Random quote:\n<a:loading2:1296923111177850931>`Please wait... Searching logs...`")
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
                await interaction.edit_original_response(content = f"-# Devutils\n-# Message search\n-# Quote from {quoteduser}:\n{quotedmessage}")
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
                    await interaction.edit_original_response(content = f"-# {interaction.user.name}({interaction.user.nick})\n-# Devutils\n-# Message search\n`{resultamount} Results:`\n{output}")
                else:
                    await interaction.edit_original_response(content = f"-# {interaction.user.name}({interaction.user.nick})\n-# Devutils\n-# Message search\n`{resultamount} Potential Results`\nOutput too long for message.")
            else:
                if prompt.startswith("m="):
                    requestlogchannel = self.bot.get_channel(1331091527308673056)
                    searchterm = prompt.split("m=", 1)[1]
                    await requestlogchannel.send(searchterm)
                    await interaction.edit_original_response(content = f"-# {interaction.user.name}({interaction.user.nick})\n-# Devutils\nSent Message successfully")
                else:
                    if prompt == "penis":
                        await interaction.edit_original_response(content = f"-# {interaction.user.name}({interaction.user.nick})\n-# Devutils\nStop the penising")
                    else:
                        await interaction.edit_original_response(content = f"-# {interaction.user.name}({interaction.user.nick})\n-# Devutils\n`Invalid Prompt!`\nDid you misspell something?")
        else:
            await interaction.edit_original_response(content = f"-# {interaction.user.name}({interaction.user.nick})\n-# Devutils\n`No permission!`")

    @app_commands.command(description = "Eval some code :3")
    @app_commands.describe(
        prompt='code to eval(maybe)'
    )
    @app_commands.allowed_installs(guilds = True, users = True)
    @app_commands.allowed_contexts(guilds = True, dms = True, private_channels = True)
    async def eval(self, interaction: discord.Interaction, prompt: str = ""):
        if interaction.user.name == "tjc472":
            await interaction.response.send_modal(EvalModal())
        else:
            if "please" in prompt:
                await interaction.response.send_message(content = "ok you did say please but seriously? im not gonna run some code bruh shut up")
            else:
                   await interaction.response.send_message(content = "if you say please maybe")

    @app_commands.command(description = "Exec some code :3")
    @app_commands.describe(
        prompt='code to exec(maybe)'
    )
    @app_commands.allowed_installs(guilds = True, users = True)
    @app_commands.allowed_contexts(guilds = True, dms = True, private_channels = True)
    async def exec(self, interaction: discord.Interaction, prompt: str = ""):
        if interaction.user.name == "tjc472":
            await interaction.response.send_modal(ExecModal())
        else:
            if "please" in prompt:
                await interaction.response.send_message(content = "ok you did say please but seriously? im not gonna run some code bruh shut up")
            else:
                await interaction.response.send_message(content = "if you say please maybe")


async def setup(bot: commands.Bot):
    await bot.add_cog(Dev(bot))
