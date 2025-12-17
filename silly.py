import discord
from discord import app_commands
from discord.ext import commands
import requests
import time
import json
import random
import discord
from discord.ext import tasks
import asyncio
from threading import Thread
import logging

logger = logging.getLogger("tjbot.silly")


meaninglist = [
    "lasanga",
    "ovo bolovo",
    "it means gay",
    "it means you're cute :3",
    ":poop:",
    "transgender",
    "[REDACTED]",
    "the silly commands cog",
    "atarctica",
    "https://fish.tjcsucht.net",
    ":fish:",
    "kam is homosexual",
    "oh no! the cdc virus removed the answer!",
    "anyways meow",
    "cat",
    ":cat:",
    ":cat2:",
    "youre not straight",
    "youre cool",
    ":baby:",
    "fan"
]


class Silly(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @app_commands.command(description = "Calculates how much of a furry you are! :3")
    @app_commands.allowed_installs(guilds = True, users = True)
    @app_commands.allowed_contexts(guilds = True, dms = True, private_channels = True)
    async def furry(self, interaction: discord.Interaction):
        await interaction.response.send_message(content=f"-# {interaction.user.name}({interaction.user.nick})\nyou are " + str(random.randint(0,100)) + "% a furry.")

    @app_commands.command(description = "Calculates how cool you are! :3")
    @app_commands.allowed_installs(guilds = True, users = True)
    @app_commands.allowed_contexts(guilds = True, dms = True, private_channels = True)
    async def cool(self, interaction: discord.Interaction):
        await interaction.response.send_message(content = f"-# {interaction.user.name}({interaction.user.nick})\nyou are " + str(random.randint(0,100)) + "% cool.")


    @app_commands.command(description="Detects if someone is lying! :3")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def liedetector(self, interaction: discord.Interaction):
        await interaction.response.send_message(content=f"-# The suspected user is lying with a chance of 100%")


    @app_commands.command(description="Rates a media! :3")
    @app_commands.describe(
        link='link of media',
        doesitcontaindragons='does it contain dragons?'
    )
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def ratemedia(self, interaction: discord.Interaction, link: str, doesitcontaindragons: bool):
        doesithave = "Doesn't contain dragons."
        rating = "Bad. No dergs. 3:"
        if doesitcontaindragons:
            doesithave = "Contains dragons :3"
            rating = "I like :3. Has dergs in it :3."
        await interaction.response.send_message(content=f"-# Rating of media {link}\n-# {doesithave}\nRating: `{rating}`")

    @app_commands.command(description="Sends a pretty dragon picture :3")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def dragon(self, interaction: discord.Interaction):
        medialist = ["https://cdn.discordapp.com/attachments/1268366668384440352/1296478069644857456/daily-wof-n-6-is-for-moonwatcher-because-book-6-lol-v0-posa9i0vrqrd1.png?ex=67126ecb&is=67111d4b&hm=8120b56b35ad3efb51a3f386810bdd86474aad24ad7fbee46f2c6d4a3c710303&", "https://cdn.discordapp.com/attachments/1292684751135572129/1295454647988785203/Screenshot_2024-09-28_010620.png?ex=67120168&is=6710afe8&hm=ec5b8c4d1c634e6eb9a53351ef8ca4fe6bceb05744e9280fc0875a8f8e06d146&", "https://cdn.discordapp.com/attachments/1292684751135572129/1295454648270061680/Screenshot_2024-09-28_010632.png?ex=67120168&is=6710afe8&hm=74f790133c4c1cb2d1b4acaa4afeada331bd325adb4f0f1d4311b353f166eed6&", "https://cdn.discordapp.com/attachments/1292684751135572129/1295454648546623580/Screenshot_2024-09-28_010636.png?ex=67120168&is=6710afe8&hm=3da7381c75fc64e0a61578fab0319d4f44a34757a245eaeb918971010a98099f&", "https://cdn.discordapp.com/attachments/1292684751135572129/1295454648810995784/Screenshot_2024-09-28_010642.png?ex=67120168&is=6710afe8&hm=03cfbc24966ea8432ce7c97af5441b3822bb0eb1938822689508afdd6a05cb9a&", "https://cdn.discordapp.com/attachments/1292684751135572129/1295454649293213707/Screenshot_2024-09-26_224025.png?ex=67120168&is=6710afe8&hm=dea568bc9f61cf8b0c0bf97a174632ca179b306775959d47d41f4960553ed048&", "https://cdn.discordapp.com/attachments/1292684751135572129/1295829796785356921/356820797_820021332821117_4782542855209346236_n.png?ex=67120d4a&is=6710bbca&hm=ea44dcf5b71c89e4e7d187353b2c403508bcbc0faed0ca6ef00ed627ec8cbced&", "https://cdn.discordapp.com/attachments/755132919202316409/1296847095210184725/Dragon_kisser.jpg?ex=671a5df9&is=67190c79&hm=a924044678cac0f620abb5f834285f5e03d098b1a460e0e9f020da4b2f1534e1&"]
        await interaction.response.send_message(content=f"-# {interaction.user.name}({interaction.user.nick})\n-# Random dragon:\n{random.choice(medialist)}")

    @app_commands.command(description="Sends a message :3")
    @app_commands.describe(
        message='content of message'
    )
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def say(self, interaction: discord.Interaction, message: str):
        await interaction.response.send_message(content=f"{message}")

    @app_commands.command(description="Pop the bubbles! :3")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def bubblewrap(self, interaction: discord.Interaction):
        await interaction.response.send_message(content=f"""Bubble wrap!
|| o |||| o |||| o |||| o |||| o |||| o |||| o |||| o ||
|| o |||| o |||| o |||| o |||| o |||| o |||| o |||| o ||
|| o |||| o |||| o |||| o |||| o |||| o |||| o |||| o ||
|| o |||| o |||| o |||| o |||| o |||| o |||| o |||| o ||
|| o |||| o |||| o |||| o |||| o |||| o |||| o |||| o ||
|| o |||| o |||| o |||| o |||| o |||| o |||| o |||| o ||""")


    @app_commands.command(description="leb :3")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def leb(self, interaction: discord.Interaction):
        await interaction.response.send_message(content=f"""It's spelled L-R-B!!!!!!!!!""")

    @app_commands.command(description="Checks if someone uses fooycord :3")
    @app_commands.describe(
        user='the id of the user'
    )
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def fooycord(self, interaction: discord.Interaction, user: discord.User):
        uses = "USER IS IN FOOYCORD DATABASE"
        userid = user.id
        if userid == 1015031565950140457:
            result = "Status: Fooycord owner"
        elif userid == 1045761412489809975:
            result = "Status: Fooycord official partner"
        elif userid == 978053871270248508:
            result = "Status: Fooycord + user"
        elif userid == 998995432132853891:
            result = "Status: Banned from fooycord for making spyware"
            uses = "USER IS BANNED FROM FOOYCORD"
        elif userid == 940959889126219856:
            result = "Status: Banned from fooycord for violating fooycord tos"
            uses = "USER IS BANNED FROM FOOYCORD"
        else:
            result = "Status: Not a fooycord user"
            uses = "USER DOES NOT USE FOOYCORD"
        await interaction.response.send_message(content="-# OFFICIAL fooycord checker\n-# Result for <@"+str(userid)+">:\n"+uses+"\n"+result)



    @app_commands.command(description="say hewwo to someone :3")
    @app_commands.describe(
        user='person to say hewwo to'
    )
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def hewwo(self, interaction: discord.Interaction, user: discord.User=None):
        disclaimer = ""
        if interaction.user.id == 1273790168129601558:
            disclaimer = " hi moonstar im just riding amas meat trust"
        if user:
            hewwotosay = user.name
            if user.nick:
                hewwotosay=user.nick
            if user.id == 1155392571569356880:
                hewwotosay = "ama"
            if user.id == 1045761412489809975:
                hewwotosay = "tjc"
            if user.id == 1261732994755072031:
                hewwotosay = "chat"
        else:
            hewwotosay = "chat"
        thing = f"hewwo {hewwotosay} :3333{disclaimer}"
        await interaction.response.send_message(content=thing)

    @app_commands.command(description="what does your name mean?:3")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def meaning(self, interaction: discord.Interaction):
        thing = random.choice(meaninglist)
        await interaction.response.send_message(content=thing)

    @app_commands.command(description="let fuzzy make your pfp jolly :3")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def jolly(self, interaction: discord.Interaction):
        pfp_url = interaction.user.avatar.url
        await interaction.response.send_message(content=f"<@1088529272559382579> This person wants their pfp to be jolly!!!!!!\n[profile picture]({pfp_url})")

    @app_commands.command(description="tjc ian reboot, only for tjc for obvious reasons :3")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def tjcian_reboot(self, interaction: discord.Interaction):
        if not interaction.user.id == 1045761412489809975:
            interaction.response.send_message(content=f":x: No.")
            return
        await interaction.response.send_message(content=f"<a:loading3:1303768414422040586> Connecting...")
        async def update_message(interaction: discord.Interaction, log: list):
            logfile = ""
            for logmessage in log:
                logfile = f"{logfile}\n{logmessage}"
            await interaction.edit_original_response(content=f"```{logfile}\n```")
        log = []
        log.append("Connected.")
        await update_message(interaction, log)
        log.append("Waiting for cancel timeout...")
        await update_message(interaction, log)
        await asyncio.sleep(10)
        log.append("Shutdown not cancelled by user. Sending `shutdown 0`...")
        await update_message(interaction, log)
        await asyncio.sleep(4)
        log.append("Waiting for shutdown to proceed...")
        await update_message(interaction, log)
        await asyncio.sleep(6)
        log.append("Connection lost. Waiting out timeout.")
        await update_message(interaction, log)
        await asyncio.sleep(12)
        log.append("Sending boot signal...")
        await update_message(interaction, log)
        await asyncio.sleep(2)
        log.append("Connection reestablished.")
        await update_message(interaction, log)
        await asyncio.sleep(1)
        log.append("Waiting for POST...")
        await update_message(interaction, log)
        await asyncio.sleep(7)
        log.append("GRUB loaded!")
        await update_message(interaction, log)
        await asyncio.sleep(7)
        log.append("Proceeding with booting Linux 'linux zen'!")
        await update_message(interaction, log)
        await asyncio.sleep(3)
        log.append("Starting all Systemd services...")
        await update_message(interaction, log)
        await asyncio.sleep(3)
        log.append("Startup succeeded. SDDM has been started. User can login now.")
        await update_message(interaction, log)

    @app_commands.command(description="Uwuwifies a message :3")
    @app_commands.describe(
        message='content of message'
    )
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def uwu(self, interaction: discord.Interaction, message: str):
        output = message.lower().replace("l","w").replace("r", "w").replace("the","da").replace ("i ", "i-i-i ").replace("!","!!").replace(".",".!").replace("?","?!")+" "+random.choice([":3","nyyaaa :333","rawr :3"," ~"])
        await interaction.response.send_message(content=f"{output}")

    @app_commands.command(description="get a quote from old cdc quotes! :3")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def cdcquote(self, interaction: discord.Interaction):
        f = open("/home/tjc/server/tjbotSLASH/cdcquotes.json")
        quotes = f.read()
        f.close()
        quotesj = json.loads(quotes)
        selectedquote = random.choice(quotesj)
        embed = discord.Embed()
        embed.title = "CDC Quotes"
        embed.color = discord.Color.pink()
        embed.add_field(name="Message Author", value=f"""<@{selectedquote["author_id"]}>""", inline=False)
        embed.add_field(name="Message Content", value=f"""{selectedquote["content"]}""", inline=False)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(description="Get annoyage counter statistics :3")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def annoyagecounter(self, interaction: discord.Interaction):
        with open("counter.json", "r") as f:
            counter_file = json.loads(f.read())
        await interaction.response.send_message(content=f"""Counter why does the mod not work: {counter_file["counter_not_work"]}
Counter how to add a thumbnail: {counter_file["counter_how_to_submit"]}
Counter rickrolled: {counter_file["counter_rickrolled"]}""")

async def setup(bot: commands.Bot):
    await bot.add_cog(Silly(bot))