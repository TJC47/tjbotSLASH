import discord
from discord import app_commands
from discord.ext import commands
import requests
import time
import json
import random
import discord
import logging

logger = logging.getLogger("tjbot.useful")

class Useful(commands.Cog):
    def __init__(self, bot: commands.Bot) :
        self.bot = bot


    @app_commands.command(description="Gets Account statistics of a Geometry Dash account :3")
    @app_commands.describe(
        username='Username of the GD account'
    )
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def stats(self, interaction: discord.Interaction, username: str):
        await interaction.response.send_message(content=f"-# {username}'s stats\n<a:loading3:1303768414422040586>`Pulling from Robtops servers...`<a:loading3:1303768414422040586>")
        try:
            stats = json.loads(requests.get("http://gdbrowser.com/api/profile/" + username).text)
            output = f"`{stats['stars']} stars, {stats['diamonds']} diamonds, {stats['coins']} coins, {stats['userCoins']} user coins, {stats['demons']} demons beaten and {stats['cp']} creator points.`"
        except:
            output = "`There was an error with Robtops servers!`"
        await interaction.edit_original_response(content=f"-# {username}'s stats\n{output}")

    @app_commands.command(description="Sends a random quote :3")
    @app_commands.allowed_installs(guilds=True, users=True)
    async def quote(self, interaction: discord.Interaction):
        await interaction.response.send_message(content=f"-# {interaction.user.name}({interaction.user.nick})\n-# Random quote:\n<a:loading2:1296923111177850931>`Please wait... Searching logs...`")
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
                await interaction.edit_original_response(content=f"-# {interaction.user.name}({interaction.user.nick})\n-# Random quote:\n<a:loading2:1296923111177850931>`Please wait... Searching logs... 10000000 Messages Searched`")
            if searchattempts == 20000000:
                await interaction.edit_original_response(content=f"-# {interaction.user.name}({interaction.user.nick})\n-# Random quote:\n<a:loading2:1296923111177850931>`Please wait... Searching logs... 20000000 Messages Searched`")
            if searchattempts == 30000000:
                await interaction.edit_original_response(content=f"-# {interaction.user.name}({interaction.user.nick})\n-# Random quote:\n<a:loading2:1296923111177850931>`Please wait... Searching logs... 30000000 Messages Searched`")
            if searchattempts == 40000000:
                await interaction.edit_original_response(content=f"-# {interaction.user.name}({interaction.user.nick})\n-# Random quote:\n<a:loading2:1296923111177850931>`Please wait... Searching logs... 40000000 Messages Searched Cancelling soon...`")
        await interaction.edit_original_response(content=f"-# Quote from {quoteduser}:\n{quotedmessage}")

    @app_commands.command(description="Shortens a link :3")
    @app_commands.describe(
        link='Link to shorten'
    )
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def shortenlink(self, interaction: discord.Interaction, link: str):
        generated = random.randint(1,1000000)
        f = open("/home/tjc/server/tjbot/redirectlist.json")
        redirectlist = json.loads(f.read())
        f.close()
        redirectlist["redirects"][str(generated)] = {"path": link, "creator": interaction.user.name, "creatorid": interaction.user.id} 
        f = open("/home/tjc/server/tjbot/redirectlist.json", "w")
        f.write(json.dumps(redirectlist, indent=4))
        f.close()
        await interaction.response.send_message(content=f"Your link has been shortened! Available under https://de-1.tjcsucht.net/ulink/{generated}")
 



async def setup(bot: commands.Bot):
    await bot.add_cog(Useful(bot))