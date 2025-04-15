import discord
from discord import app_commands
from discord.ext import commands
import requests
import time
import json
import random
import discord
import asyncio

currency = "estrogen"

def update_balance(userid, amount):
    f = open("./save.json")
    economy_save = json.loads(f.read())
    f.close()
    if not str(userid) in economy_save["economy"]:
        economy_save["economy"][str(userid)] = {"money": 0}
    economy_save["economy"][str(userid)]["money"] = economy_save["economy"][str(userid)]["money"] + amount
    f = open("save.json", "w")
    f.write(json.dumps(economy_save, indent=4))
    f.close()

def get_balance(userid):
    f = open("./save.json")
    economy_save = json.loads(f.read())
    f.close()
    if not str(userid) in economy_save["economy"]:
        economy_save["economy"][str(userid)] = {"money": 0}
    return economy_save["economy"][str(userid)]["money"]

class Economy(commands.Cog):
    def __init__(self, bot: commands.Bot) :
        self.bot = bot


    @app_commands.command(description="All or nothing (not rigged) :3")
    @app_commands.describe(
        amount='how much to gamble'
    )
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def gambling(self, interaction: discord.Interaction, amount: int):
        userbalance = get_balance(interaction.user.id)
        userbalance_before = get_balance(interaction.user.id)
        if not userbalance < amount:

            await interaction.response.send_message(content=f"Let's go gambling!")
            try:
                await asyncio.sleep(1)
                rig = round(userbalance / 100)
                if rig > 5:
                    rig = 5
                if random.randint(1, 1 + rig) == 1:
                    moneydiff = amount + random.randint(0, amount)
                    update_balance(interaction.user.id, moneydiff)
                    userbalance_after = get_balance(interaction.user.id)
                    await interaction.edit_original_response(content=f"You won `{moneydiff}{currency}`!\n-# WOHOOO!!!!\n-# `{userbalance_before}{currency} -> {userbalance_after}{currency}`")
                else:
                    moneydiff = amount
                    update_balance(interaction.user.id, 0 - moneydiff)
                    userbalance_after = get_balance(interaction.user.id)
                    await interaction.edit_original_response(content=f"You lost `{moneydiff}{currency}`!\n-# `{userbalance_before}{currency} -> {userbalance_after}{currency}`")
            except:
                await interaction.edit_original_response(content=f"there was an error with the database")
        else:
            await interaction.response.send_message(content=f"You dont have enough money for this `({userbalance}{currency} < {amount}{currency})`")


    @app_commands.command(description="check someones or your balance :3")
    @app_commands.describe(
        user='person to check balance'
    )
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def balance(self, interaction: discord.Interaction, user: discord.User=None):
        if user:
            userbalance = get_balance(user.id)
            haha = ""
            if userbalance <= 0:
                haha = "\n-# theyre broke asf lmao"
            await interaction.response.send_message(content=f"Balance of {user.mention}: `{userbalance}{currency}`{haha}")
        else:
            userbalance = get_balance(interaction.user.id)
            haha = ""
            if userbalance <= 0:
                haha = "\n-# youre broke asf lmao"
            await interaction.response.send_message(content=f"Your balance: `{userbalance}{currency}`{haha}")

    @app_commands.command(description="Why work in real life when you can do it virtually? :3")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def work(self, interaction: discord.Interaction):
        userbalance_before = get_balance(interaction.user.id)
        random_money = random.randint(0, 15)
        update_balance(interaction.user.id, random_money)
        wife = ""
        if random.randint(1,100) == 1 and userbalance_before > 105:
            wifetheftamount = random.randint(95,105)
            wife = f", but your wife went to buy groceries and took `{wifetheftamount}€` without asking you"
            update_balance(interaction.user.id, 0 - wifetheftamount)
        userbalance_after = get_balance(interaction.user.id)
        await interaction.response.send_message(content=f"You went to work and got `{random_money}{currency}`{wife}\n-# `{userbalance_before}{currency} -> {userbalance_after}{currency}`")


    @app_commands.command(description="Attempt a crime(high risk high reward) :3")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def crime(self, interaction: discord.Interaction):
        userbalance = get_balance(interaction.user.id)
        userbalance_before = get_balance(interaction.user.id)
        if not userbalance < 0:
            await interaction.response.send_message(content=f"Committing Crime...")
            try:
                await asyncio.sleep(5)
                if random.randint(1, 5) == 1:
                    moneydiff = random.randint(30, 150)
                    update_balance(interaction.user.id, moneydiff)
                    userbalance_after = get_balance(interaction.user.id)
                    await interaction.edit_original_response(content=f"You successfully managed to commit a crime and got `{moneydiff}{currency}`!\n-# `{userbalance_before}{currency} -> {userbalance_after}{currency}`")
                else:
                    moneydiff = random.randint(30, 100)
                    update_balance(interaction.user.id, 0 - moneydiff)
                    userbalance_after = get_balance(interaction.user.id)
                    await interaction.edit_original_response(content=f"You got caught and have been fined `{moneydiff}{currency}`!\n-# `{userbalance_before}{currency} -> {userbalance_after}{currency}`")
            except:
                await interaction.edit_original_response(content=f"there was an error with the database")
        else:
            await interaction.response.send_message(content=f"You can't commit a crime because you are under arrest! Work to pay off your debt and get released (You have `{userbalance}{currency}`)")



    @app_commands.command(description="steal from someone :3")
    @app_commands.describe(
        user='person to steal from'
    )
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def steal(self, interaction: discord.Interaction, user: discord.User):
        if user.id == interaction.user.id:
            await interaction.response.send_message(content=f"You can't steal from yourself :bruh:")
            return
        stealeebalance_before = get_balance(user.id)
        if stealeebalance_before < 200:
            await interaction.response.send_message(content=f"You can't steal from them because they dont have enough money! `({stealeebalance_before}{currency} < 200{currency})`")
            return
        userbalance_before = get_balance(interaction.user.id)
        randmax = stealeebalance_before/10
        if randmax > 200:
            randmax = 200
        if randmax < 10:
            randmax = 10
        stealamount = random.randint(0, round(randmax))
        update_balance(user.id, -stealamount)
        update_balance(interaction.user.id, stealamount)
        stealeebalance_after = get_balance(user.id)
        userbalance_after = get_balance(interaction.user.id)
        await interaction.response.send_message(content=f"You successfully stole `{stealamount}{currency}` from {user.mention}!\n-# `{interaction.user.name} {userbalance_before}{currency} -> {userbalance_after}{currency}`\n-# `{user.name} {stealeebalance_before}{currency} -> {stealeebalance_after}{currency}`")


    @app_commands.command(description="give currency to someone :3")
    @app_commands.describe(
        user='person to give currency to',
        amount='amount of currency to give'
    )
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def pay(self, interaction: discord.Interaction, user: discord.User, amount: int):
        if user.id == interaction.user.id:
            await interaction.response.send_message(content=f"You can't pay yourself :bruh:")
            return
        if amount < 0:
            await interaction.response.send_message(content=f"That's not how money works(Atleast in this case Tax evasion is something different)")
            return
        payeebalance_before = get_balance(user.id)
        userbalance_before = get_balance(interaction.user.id)
        if userbalance_before < amount:
            await interaction.response.send_message(content=f"You dont have enough money for this `({userbalance_before}{currency} < {amount}{currency})`")
            return
        update_balance(interaction.user.id, -amount)
        update_balance(user.id, amount)
        payeebalance_after = get_balance(user.id)
        userbalance_after = get_balance(interaction.user.id)
        await interaction.response.send_message(content=f"You successfully paid `{amount}{currency}` to {user.mention}!\n-# `{interaction.user.name} {userbalance_before}{currency} -> {userbalance_after}{currency}`\n-# `{user.name} {payeebalance_before}{currency} -> {payeebalance_after}{currency}`")

async def setup(bot: commands.Bot):
    await bot.add_cog(Economy(bot))
