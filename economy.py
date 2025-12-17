import discord
from discord import app_commands
from discord.ext import commands, tasks
import requests
import time
import json
import random
import discord
import asyncio
import string
import logging

logger = logging.getLogger("tjbot.economy")

updateinfo = """# Current Update and status
# NEXT MAJOR UPDATE: GROW A TJBOT UPDATE
### AFTER THE AFTER: ORANG BOT COLLAB???!!!

# PROGRESS: [----------] 100% DERMUKO REBALABNCE UPDATE RELEASEDeta: <t:0:R> 
"""



currency = "estrogen"

f = open("itemlist.json")
fi = f.read()
f.close()
shopItems = json.loads(fi)

f = open("passivelist.json")
fi = f.read()
f.close()
passivesIndex = json.loads(fi)

global writeq
writeq = []

def update_balance(userid, amount, reason="None"):
    actionid = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    writeq.append(actionid)
    while not writeq[0] == actionid: pass
    f = open("./save.json")
    economy_save = json.loads(f.read())
    f.close()
    if not str(userid) in economy_save["economy"]:
        economy_save["economy"][str(userid)] = {"money": 0}
    economy_save["economy"][str(userid)]["money"] = economy_save["economy"][str(userid)]["money"] + amount
    f = open("save.json", "w")
    f.write(json.dumps(economy_save, indent=4))
    f.close()
    f = open("economy.log", "a")
    f.write(f"[{userid}] ({amount}) -> {economy_save['economy'][str(userid)]['money'] - amount}{currency} -> {economy_save['economy'][str(userid)]['money']}{currency} (Reason: {reason})\n")
    f.close()
    writeq.remove(actionid)

def get_balance(userid):
    actionid = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    writeq.append(actionid)
    while not writeq[0] == actionid: pass
    f = open("./save.json")
    economy_save = json.loads(f.read())
    f.close()
    if not str(userid) in economy_save["economy"]:
        economy_save["economy"][str(userid)] = {"money": 0}
    writeq.remove(actionid)
    #return economy_save["economy"][str(userid)]["money"]
    if userid == 1088529272559382579:
        return float("inf")
    return 1000000000000000000000000000 if userid == 729671931359395940 and economy_save["economy"][str(userid)]["money"] < 1000000000000000000000000000 else economy_save["economy"][str(userid)]["money"]

def get_economy():
    actionid = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    writeq.append(actionid)
    while not writeq[0] == actionid: pass
    f = open("./save.json")
    economy_save = json.loads(f.read())
    f.close()
    writeq.remove(actionid)
    return economy_save["economy"]

def set_inventory(userid, new):
    actionid = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    writeq.append(actionid)
    while not writeq[0] == actionid: pass
    f = open("./save.json")
    economy_save = json.loads(f.read())
    f.close()
    if not str(userid) in economy_save["economy"]:
        economy_save["economy"][str(userid)] = {"money": 0, "inventory": {}}
    economy_save["economy"][str(userid)]["inventory"] = new
    f = open("save.json", "w")
    f.write(json.dumps(economy_save, indent=4))
    f.close()
    writeq.remove(actionid)

def get_inventory(userid):
    actionid = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    writeq.append(actionid)
    while not writeq[0] == actionid: pass
    f = open("./save.json")
    economy_save = json.loads(f.read())
    f.close()
    if not str(userid) in economy_save["economy"]:
        economy_save["economy"][str(userid)] = {"money": 0, "inventory": {}}
    if not "inventory" in economy_save["economy"][str(userid)]:
        economy_save["economy"][str(userid)]["inventory"] = {}
    writeq.remove(actionid)
    return economy_save["economy"][str(userid)]["inventory"]

def set_passives(userid, new):
    actionid = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    writeq.append(actionid)
    while not writeq[0] == actionid: pass
    f = open("./save.json")
    economy_save = json.loads(f.read())
    f.close()
    if not str(userid) in economy_save["economy"]:
        economy_save["economy"][str(userid)] = {"money": 0, "passives": {}}
    economy_save["economy"][str(userid)]["passives"] = new
    f = open("save.json", "w")
    f.write(json.dumps(economy_save, indent=4))
    f.close()
    writeq.remove(actionid)

def get_passives(userid):
    actionid = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    writeq.append(actionid)
    while not writeq[0] == actionid: pass
    f = open("./save.json")
    economy_save = json.loads(f.read())
    f.close()
    if not str(userid) in economy_save["economy"]:
        economy_save["economy"][str(userid)] = {"money": 0, "passives": {}}
    if not "passives" in economy_save["economy"][str(userid)]:
        economy_save["economy"][str(userid)]["passives"] = {}
    writeq.remove(actionid)
    return economy_save["economy"][str(userid)]["passives"]

def set_misc(userid, new):
    actionid = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    writeq.append(actionid)
    while not writeq[0] == actionid: pass
    f = open("./save.json")
    economy_save = json.loads(f.read())
    f.close()
    if not str(userid) in economy_save["economy"]:
        economy_save["economy"][str(userid)] = {"money": 0, "misc": {}}
    economy_save["economy"][str(userid)]["misc"] = new
    f = open("save.json", "w")
    f.write(json.dumps(economy_save, indent=4))
    f.close()
    writeq.remove(actionid)

def get_misc(userid):
    actionid = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    writeq.append(actionid)
    while not writeq[0] == actionid: pass
    f = open("./save.json")
    economy_save = json.loads(f.read())
    f.close()
    if not str(userid) in economy_save["economy"]:
        economy_save["economy"][str(userid)] = {"money": 0, "misc": {}}
    if not "misc" in economy_save["economy"][str(userid)]:
        economy_save["economy"][str(userid)]["misc"] = {}
    writeq.remove(actionid)
    return economy_save["economy"][str(userid)]["misc"]

def get_cashdrops():
    actionid = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    writeq.append(actionid)
    while not writeq[0] == actionid: pass
    f = open("./save.json")
    economy_save = json.loads(f.read())
    f.close()
    writeq.remove(actionid)
    return economy_save["cashdrops"]

def set_cashdrops(cashdrops):
    actionid = "".join(random.choices(string.ascii_letters + string.digits, k=16))
    writeq.append(actionid)
    while not writeq[0] == actionid: pass
    f = open("./save.json")
    economy_save = json.loads(f.read())
    f.close()
    economy_save["cashdrops"] = cashdrops
    f = open("save.json", "w")
    f.write(json.dumps(economy_save, indent=4))
    f.close()
    writeq.remove(actionid)


def to_ordinal(number):
    ordinal = "th"

    if number == 1:
        ordinal = "st"
    if number == 2:
        ordinal = "nd"
    if number == 3:
        ordinal = "rd"

    if number > 20:
        last_digit = int(str(number)[1:]) # :skull:
        if last_digit == 1: ordinal = "st"
        if last_digit == 2: ordinal = "nd"
        if last_digit == 3: ordinal = "rd"

    return f"{number}{ordinal}"

def ezread(number: int): # short function name because this is gonna be used a LOT
    if number >= 1000000000000000000000000000000000: return f"{str(round(number / 1000000000000000000000000000000000, ndigits=1))}I LOST TRACK OF THE NUMBERS"
    elif number >= 1000000000000000000000000000000: return f"{str(round(number / 1000000000000000000000000000000, ndigits=1))}BSKY"
    elif number >= 1000000000000000000000000000: return f"{str(round(number / 1000000000000000000000000000, ndigits=1))}TWITTER"
    elif number >= 1000000000000000000000000: return f"{str(round(number / 1000000000000000000000000, ndigits=1))}X"
    elif number >= 1000000000000000000000: return f"{str(round(number / 1000000000000000000000, ndigits=1))}SEP"
    elif number >= 1000000000000000000: return f"{str(round(number / 1000000000000000000, ndigits=1))}SEX"
    elif number >= 1000000000000000: return f"{str(round(number / 1000000000000000, ndigits=1))}Q"
    elif number >= 1000000000000: return f"{str(round(number / 1000000000000, ndigits=1))}T"
    elif number >= 1000000000: return f"{str(round(number / 1000000000, ndigits=1))}B"
    elif number >= 1000000: return f"{str(round(number / 1000000, ndigits=1))}M"
    elif number >= 1000: return f"{str(round(number / 1000, ndigits=1))}K"
    else: return f"{str(number)}"

def unpacknumbers(string: str):
    string = string.lower()
    try:
        if string.endswith("k"): return round(float(string.strip("k")) * 1000)
        elif string.endswith("m"): return round(float(string.strip("m")) * 1000000)
        elif string.endswith("b"): return round(float(string.strip("b")) * 1000000000)
        elif string.endswith("t"): return round(float(string.strip("t")) * 1000000000000)
        elif string.endswith("q"): return round(float(string.strip("q")) * 1000000000000000)
        elif string.endswith("sex"): return round(float(string.strip("sex")) * 1000000000000000000)
        elif string.endswith("sep"): return round(float(string.strip("sep")) * 1000000000000000000000)
        elif string.endswith("x"): return round(float(string.strip("x")) * 1000000000000000000000000)
        elif string.endswith("twitter"): return round(float(string.strip("twitter")) * 1000000000000000000000000000)
        elif string.endswith("bsky"): return round(float(string.strip("bsky")) * 1000000000000000000000000000000)
        elif string.endswith("i lost track of the numbers"): return round(float(string.strip("i lost track of the numbers")) * 1000000000000000000000000000000000)
        else: return int(string)
    except:
        return 0


class ConfrimDeleteModal(discord.ui.Modal, title = 'ARE YOU ABSOLUTELY SURE?'):
    prompt = discord.ui.TextInput(
        label = f'ARE YOU SURE THAT YOU WANT TO DELETE?',
        style = discord.TextStyle.long,
        placeholder = 'TYPE "DELETE ALL MY DATA" HERE TO CONFIRM',
        required = True,
        max_length = 100,
    )

    async def on_submit(self, interaction: discord.Interaction):
        if self.prompt.value == "DELETE ALL MY DATA":
            await interaction.response.send_message(content = f"YOUR DATA HAS BEEN ***DELETED*** IRREVERSIBLY")
            set_inventory(interaction.user.id, {})
            set_passives(interaction.user.id, {})
            update_balance(interaction.user.id,-get_balance(interaction.user.id),f"Data Deletion ({interaction.user.name})")
        else:
            await interaction.response.send_message(content = f"DELETION PROCESS CANCELED")

global ratelimit
ratelimit = {}
global lastratelimitreset
lastratelimitreset = round(time.time())

@tasks.loop(seconds=60)
async def activity():
        global ratelimit
        global lastratelimitreset
        ratelimit = {}
        lastratelimitreset = round(time.time())


async def do_ratelimit(interaction: discord.Interaction):
        global ratelimit
        if str(interaction.user.id) in ratelimit:
            higher= 0
            userinv = get_inventory(interaction.user.id)
            if "higher_rate_limit" in userinv:
                higher = 5 
            if ratelimit[str(interaction.user.id)] >= 5 + higher:
                await interaction.response.send_message(content=f":warning: Ratelimited 3:<, please try again <t:{lastratelimitreset+60}:R>")
                return True
            else:
                ratelimit[str(interaction.user.id)] = ratelimit[str(interaction.user.id)] + 1
                return False
        else:
            ratelimit[str(interaction.user.id)] = 1
            return False

class Economy(commands.Cog):



    def __init__(self, bot: commands.Bot) :
        self.bot = bot
        activity.start()

    @app_commands.command(description="All or nothing (not rigged) :3")
    @app_commands.describe(
        amount='how much to gamble'
    )
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def gambling(self, interaction: discord.Interaction, amount: str):
        amount = unpacknumbers(amount)
        if await do_ratelimit(interaction): return
        await interaction.response.send_message(content=f"<a:loading3:1303768414422040586> Let's go gambling! <a:loading3:1303768414422040586>")
        try:
            await asyncio.sleep(1)
            userbalance = get_balance(interaction.user.id)
            userbalance_before = get_balance(interaction.user.id)
            userinv = get_inventory(interaction.user.id)
            if (not userbalance < amount) and (not amount < 0):

                try:
                    rig = round(userbalance / 100)
                    if rig > 5:
                        rig = 5
                    predictorthing = ""
                    if "unrig" in userinv:
                        rig = 1
                        if rig < 0:
                            rig = 0
                        predictorthing = "\n-# Your chance of win has been altered (for the good or the bad) because you **unrigged the casino**"

                    if random.randint(1, 1 + rig) == 1:
                        moneydiff = round(1* amount + random.randint(0, amount))
                        update_balance(interaction.user.id, moneydiff, f"Gambling ({interaction.user.name})")
                        userbalance_after = get_balance(interaction.user.id)
                        await interaction.edit_original_response(content=f":tada: You won `{ezread(moneydiff)}{currency}`!\n-# WOHOOO!!!!\n-# `{ezread(userbalance_before)}{currency} -> {ezread(userbalance_after)}{currency}`{predictorthing}")
                    else:
                        moneydiff = amount
                        update_balance(interaction.user.id, 0 - moneydiff, f"Gambling ({interaction.user.name})")
                        userbalance_after = get_balance(interaction.user.id)
                        await interaction.edit_original_response(content=f"<:amgry:1269065092461232170> You lost `{ezread(moneydiff)}{currency}`!\n-# `{ezread(userbalance_before)}{currency} -> {ezread(userbalance_after)}{currency}`{predictorthing}")
                except:
                    await interaction.edit_original_response(content=f"there was an error with the database")
            else:
                await interaction.edit_original_response(content=f"You dont have enough money for this `({ezread(userbalance)}{currency} < {ezread(amount)}{currency})`")
        except:
            await interaction.edit_original_response(content=f"something VEEEEEEEERY bad happened with the bots dcdodce and you broke it, gerat job, {interaction.user.name}")

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
            await interaction.response.send_message(content=f"Balance of {user.mention}: `{ezread(userbalance)}{currency}, {userbalance}{currency} exact`{haha}")
        else:
            userbalance = get_balance(interaction.user.id)
            haha = ""
            if userbalance <= 0:
                haha = "\n-# youre broke asf lmao"
            await interaction.response.send_message(content=f"Your balance: `{ezread(userbalance)}{currency}, {userbalance}{currency} exact`{haha}")

    @app_commands.command(description="Why work in real life when you can do it virtually? :3")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def work(self, interaction: discord.Interaction):
        userbalance_before = get_balance(interaction.user.id)
        userinv = get_inventory(interaction.user.id)
        if await do_ratelimit(interaction): return

        usermisc = get_misc(interaction.user.id)
        if "work_count" not in usermisc:
            usermisc["work_count"] = 0
        usermisc["work_count"] = usermisc["work_count"] + 1
        set_misc(interaction.user.id, usermisc)

        modifiers = ""
        wageincrease = 0
        wagemultiplier = 1
        morerandom = 0
        if userbalance_before < 150:
            wagemultiplier = wagemultiplier + 0.2
        if "cof" in userinv:
            modifiers = modifiers + "\n-# Your wage has been increased because you had a **Coffee**"
            wagemultiplier = wagemultiplier + 1
            userinv.pop("cof")
            set_inventory(interaction.user.id, userinv)
        elif "cm" in userinv:
            modifiers = modifiers + "\n-# Your wage has been increased because you had a **Coffee** (Automatically Brewed Through Your Coffee Machine)"
            wagemultiplier = wagemultiplier + 0.9
        if "bpj" in userinv:
            modifiers = modifiers + "\n-# Your wage is buffed because you have a **Better Paying Job**"
            wageincrease = wageincrease + 100
        if "ebpj" in userinv:
            modifiers = modifiers + "\n-# Your wage is buffed even more because you have a **CEO Position**"
            wageincrease = wageincrease + 10000
            morerandom = morerandom + 1000
        if random.randint(1,20) == 1:
            modifiers = modifiers + "\n-# Your got twice your wage because you **worked good enough**"
            wagemultiplier = wagemultiplier + 1
        dropped = False
        if random.randint(1,100) == 1:
            modifiers = modifiers + "\n# UH OH! YOU ACCIDENTALLY DROPPED SOME OF YOUR INCOME ON THE WAY HOME! USE `/pickup_cash` TO PICK IT UP"
            wagemultiplier = wagemultiplier * 0.5
            dropped = True
        random_money = round(random.randint(0 + wageincrease, 15 + wageincrease + morerandom)*wagemultiplier)
        if dropped:
            cashdrops = get_cashdrops()
            cashdrops.append(random_money)
            set_cashdrops(cashdrops)
        update_balance(interaction.user.id, random_money, f"Working ({interaction.user.name})")
        wife = ""
        if random.randint(1,100) == 1 and userbalance_before > 105:
            wifetheftamount = random.randint(95,105)
            wife = f", but your wife went to buy groceries and took `{wifetheftamount}€` without asking you"
            update_balance(interaction.user.id, 0 - wifetheftamount, f"Working (wife) ({interaction.user.name})")
        userbalance_after = get_balance(interaction.user.id)
        await interaction.response.send_message(content=f":euro: You went to work and got `{ezread(random_money)}{currency}`{wife}{modifiers}\n-# `{ezread(userbalance_before)}{currency} -> {ezread(userbalance_after)}{currency}`")


    @app_commands.command(description="Attempt a crime(high risk high reward) :3")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def crime(self, interaction: discord.Interaction):
        userbalance = get_balance(interaction.user.id)
        userbalance_before = get_balance(interaction.user.id)
        userinv = get_inventory(interaction.user.id)
        modifier = ""
        if await do_ratelimit(interaction): return
        if not userbalance < 0:
            await interaction.response.send_message(content=f"<a:loading2:1296923111177850931> Committing Crime... <a:loading2:1296923111177850931>")
            try:
                await asyncio.sleep(5)
                if random.randint(1, 5) == 1 or "gun" in userinv:
                    if "gun" in userinv:
                        modifier = "\n-# You managed to distract the police using your **Totally Real And Working Gun** and got away with the crime!"
                        userinv.pop("gun")
                        set_inventory(interaction.user.id, userinv)
                    moneydiff = random.randint(30, 150)
                    update_balance(interaction.user.id, moneydiff, f"Crime ({interaction.user.name})")
                    userbalance_after = get_balance(interaction.user.id)
                    await interaction.edit_original_response(content=f":moneybag: You successfully managed to commit a crime and got `{moneydiff}{currency}`!{modifier}\n-# `{ezread(userbalance_before)}{currency} -> {ezread(userbalance_after)}{currency}`")
                else:
                    moneydiff = random.randint(30, 100)
                    update_balance(interaction.user.id, 0 - moneydiff, f"Crime ({interaction.user.name})")
                    userbalance_after = get_balance(interaction.user.id)
                    await interaction.edit_original_response(content=f":oncoming_police_car: :police_officer: You got caught and have been fined `{moneydiff}{currency}`!\n-# `{ezread(userbalance_before)}{currency} -> {ezread(userbalance_after)}{currency}`")
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
        if await do_ratelimit(interaction): return
        if user.id == interaction.user.id:
            await interaction.response.send_message(content=f"You can't steal from yourself :bruh:")
            return
        stealeebalance_before = get_balance(user.id)
        if stealeebalance_before < 200:
            await interaction.response.send_message(content=f"You can't steal from them because they dont have enough money! `({stealeebalance_before}{currency} < 200{currency})`")
            return
        userinv = get_inventory(user.id)
        if "dc" in userinv:
            await interaction.response.send_message(content=f"You can't steal from them because they have a **Debit Card** instead of cash! Nice Try!")
            return
        userbalance_before = get_balance(interaction.user.id)
        randmax = stealeebalance_before/10
        if randmax > 200:
            randmax = 200
        if randmax < 10:
            randmax = 10
        stealamount = random.randint(0, round(randmax))
        update_balance(user.id, -stealamount, f"Stealing (Remove stolen money from stealee) ({user.name})")
        update_balance(interaction.user.id, stealamount, f"Stealing (Credit stolen money) ({interaction.user.name})")
        usermisc = get_misc(interaction.user.id)
        if "stolen_total" not in usermisc:
            usermisc["stolen_total"] = 0
        usermisc["stolen_total"] = usermisc["stolen_total"] + stealamount
        set_misc(interaction.user.id, usermisc)
        stealeebalance_after = get_balance(user.id)
        userbalance_after = get_balance(interaction.user.id)
        await interaction.response.send_message(content=f"You successfully stole `{stealamount}{currency}` from {user.mention}!\n-# `{interaction.user.name} {ezread(userbalance_before)}{currency} -> {ezread(userbalance_after)}{currency}`\n-# `{user.name} {ezread(stealeebalance_before)}{currency} -> {ezread(stealeebalance_after)}{currency}`")


    @app_commands.command(description="give currency to someone :3")
    @app_commands.describe(
        user='person to give currency to',
        amount='amount of currency to give'
    )
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def pay(self, interaction: discord.Interaction, user: discord.User, amount: str):
        amount = unpacknumbers(amount)
        if await do_ratelimit(interaction): return
        if user.id == interaction.user.id:
            await interaction.response.send_message(content=f"You can't pay yourself :bruh:")
            return
        if amount < 0:
            await interaction.response.send_message(content=f"That's not how money works(Atleast in this case Tax evasion is something different)")
            return
        payeebalance_before = get_balance(user.id)
        userbalance_before = get_balance(interaction.user.id)
        if userbalance_before < amount:
            await interaction.response.send_message(content=f"You dont have enough money for this `({ezread(userbalance_before)}{currency} < {ezread(amount)}{currency})`")
            return

        update_balance(interaction.user.id, -amount, f"Payment (remove money from payer) ({interaction.user.name})")
        update_balance(user.id, amount, f"Payment (credit money to payee) ({user.name})")
        payeebalance_after = get_balance(user.id)
        userbalance_after = get_balance(interaction.user.id)
        await interaction.response.send_message(content=f"You successfully paid `{ezread(amount)}{currency}` to {user.mention}!\n-# `{interaction.user.name} {ezread(userbalance_before)}{currency} -> {ezread(userbalance_after)}{currency}`\n-# `{user.name} {ezread(payeebalance_before)}{currency} -> {ezread(payeebalance_after)}{currency}`")


    @app_commands.command(description="pay someone as someone else :3")
    @app_commands.describe(
        payer='person to take money from',
        user='person to give currency to',
        amount='amount of currency to give'
    )
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def owner_pay(self, interaction: discord.Interaction, payer: discord.User, user: discord.User, amount: str):
        if not (interaction.user.id == self.bot.owner_id or interaction.user.id == 729671931359395940):
            await interaction.response.send_message(content=f"This is bot owner only!")
            return
        amount = unpacknumbers(amount)
        if user.id == payer.id:
            await interaction.response.send_message(content=f"You can't pay yourself :bruh:")
            return
        payeebalance_before = get_balance(user.id)
        userbalance_before = get_balance(payer.id)

        update_balance(payer.id, -amount, f"Payment (remove money from payer) ({payer.name})")
        update_balance(user.id, amount, f"Payment (credit money to payee) ({user.name})")
        payeebalance_after = get_balance(user.id)
        userbalance_after = get_balance(payer.id)
        await interaction.response.send_message(content=f"You successfully paid `{ezread(amount)}{currency}` to {user.mention}!\n-# `{payer.name} {ezread(userbalance_before)}{currency} -> {ezread(userbalance_after)}{currency}`\n-# `{user.name} {ezread(payeebalance_before)}{currency} -> {ezread(payeebalance_after)}{currency}`")


    global shopItems
    async def shop_ac(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
        choices = []
        userbalance = get_balance(interaction.user.id)
        choices.append(app_commands.Choice(name = f"""------------ Your Balance: {ezread(userbalance)}{currency} ------------""",value = "null"))
        for item in shopItems:
            if current.lower() in item.lower() and item not in get_inventory(interaction.user.id):
                canbuy = "❌"
                if userbalance >= shopItems[item]["price"]:
                    canbuy = "✅"
                choices.append(app_commands.Choice(name = f"""{shopItems[item]["name"]} - {ezread(shopItems[item]["price"])}{currency} - Can buy: {canbuy}""",value = item))

        return choices

    @app_commands.command(description = "Buy something from the shop :3")
    @app_commands.describe(
        item='Item to buy',
    )
    @app_commands.autocomplete(item = shop_ac)
    @app_commands.allowed_installs(guilds = True, users = True)
    @app_commands.allowed_contexts(guilds = True, dms = True, private_channels = True)
    async def buy(self, interaction: discord.Interaction, item: str):
        if item in shopItems:
            userinv = get_inventory(interaction.user.id)
            userbalance = get_balance(interaction.user.id)
            if shopItems[item]["price"] > userbalance:
                await interaction.response.send_message(content = f"""You don't have enough money for this! `({ezread(userbalance)}{currency} < {ezread(shopItems[item]["price"])}{currency})`""")
                return
            if item in userinv:
                await interaction.response.send_message(content = f"""You already have {shopItems[item]["pronouns"]} "{shopItems[item]["name"]}"!""")
                return
            tempitem = shopItems[item]
            userinv[item] = tempitem
            update_balance(interaction.user.id, -shopItems[item]["price"], f"""Purchasing of '{shopItems[item]["name"]}' ({interaction.user.name})""")
            set_inventory(interaction.user.id, userinv)
            await interaction.response.send_message(content = f"""You successfully purchased {shopItems[item]["pronouns"]} "{shopItems[item]["name"]}" for {ezread(shopItems[item]["price"])}{currency}""")
        else:
            await interaction.response.send_message(content = f"That doesn't exist!", ephemeral=True)

    @app_commands.command(description="view the shop :3")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def shop(self, interaction: discord.Interaction):
            if await do_ratelimit(interaction): return
            userinv = get_inventory(interaction.user.id)
            userbalance = get_balance(interaction.user.id)

            embed = discord.Embed()
            embed.title = "Shop"
            embed.set_footer(text=f"Your Balance: {ezread(userbalance)}{currency}, use /buy to buy your selected product")
            embed.color = discord.Color.pink()


            for item in shopItems:
                embed.add_field(name=f"""{shopItems[item]["name"]}:""", value=f"""> Description: {shopItems[item]["description"]}\n> Price: {ezread(shopItems[item]["price"])}{currency}""", inline=False)
            await interaction.response.send_message(embed=embed)

    @app_commands.command(description="show passives :3")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def passives(self, interaction: discord.Interaction):
            if await do_ratelimit(interaction): return
            userpassives = get_passives(interaction.user.id)
            userbalance = get_balance(interaction.user.id)

            embed = discord.Embed()
            embed.title = "Passives information"
            embed.set_footer(text=f"Your Balance: {ezread(userbalance)}{currency}, use /buy_passive to buy a passive")
            embed.color = discord.Color.pink()


            for item in passivesIndex:
                embed.add_field(name=f"{item}:", value=f"""> Description: {passivesIndex[item]["description"]}\n> Price: {ezread(passivesIndex[item]["price"])}{currency}\n> Active: {item in userpassives}\n> {currency}/s: {ezread(passivesIndex[item]["per_second"])}""", inline=False)
            await interaction.response.send_message(embed=embed)

    async def passive_ac(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
        choices = []
        userbalance = get_balance(interaction.user.id)
        choices.append(app_commands.Choice(name = f"""------------ Your Balance: {ezread(userbalance)}{currency} ------------""",value = "null"))
        for passive in passivesIndex:
            if current.lower() in passive.lower() and passive not in get_passives(interaction.user.id):
                canbuy = "❌"
                if userbalance >= passivesIndex[passive]["price"]:
                    canbuy = "✅"
                choices.append(app_commands.Choice(name = f"""{passivesIndex[passive]["name"]} - {ezread(passivesIndex[passive]["price"])}{currency} - Can buy: {canbuy}""",value = passive))

        return choices

    @app_commands.command(description = "Buy a passive :3")
    @app_commands.describe(
        item='Passive to buy',
    )
    @app_commands.autocomplete(item = passive_ac)
    @app_commands.allowed_installs(guilds = True, users = True)
    @app_commands.allowed_contexts(guilds = True, dms = True, private_channels = True)
    async def buy_passive(self, interaction: discord.Interaction, item: str):
        if item in passivesIndex:
            userinv = get_passives(interaction.user.id)
            userbalance = get_balance(interaction.user.id)
            if passivesIndex[item]["price"] > userbalance:
                await interaction.response.send_message(content = f"""You don't have enough money for this! `({ezread(userbalance)}{currency} < {ezread(passivesIndex[item]["price"])}{currency})`""")
                return
            if item in userinv:
                await interaction.response.send_message(content = f"""You already have {passivesIndex[item]["pronouns"]} "{item}"!""")
                return
            tempitem = passivesIndex[item]
            tempitem["last_used"] = round(time.time())
            userinv[item] = tempitem
            update_balance(interaction.user.id, -passivesIndex[item]["price"], f"Purchasing of '{item}' ({interaction.user.name})")
            set_passives(interaction.user.id, userinv)
            await interaction.response.send_message(content = f"""You successfully purchased {passivesIndex[item]["pronouns"]} "{item}" (passive) for {ezread(passivesIndex[item]["price"])}{currency}""")
        else:
            await interaction.response.send_message(content = f"That passive doesn't exist!", ephemeral=True)

    @app_commands.command(description = "Collect your money generated from your passives :3")
    @app_commands.allowed_installs(guilds = True, users = True)
    @app_commands.allowed_contexts(guilds = True, dms = True, private_channels = True)
    async def collect_passive_money(self, interaction: discord.Interaction):
        if await do_ratelimit(interaction): return
        userinv = get_passives(interaction.user.id)
        userbalance_before = get_balance(interaction.user.id)
        moneydiff = 0
        for item in userinv:
            perSecond = userinv[item]["per_second"]
            moneydiff = moneydiff + perSecond * (round(time.time()) - userinv[item]["last_used"])
            userinv[item]["last_used"] = round(time.time())
        set_passives(interaction.user.id, userinv)
        update_balance(interaction.user.id, moneydiff, f"Collecting money from passives ({interaction.user.name})")
        userbalance_after = get_balance(interaction.user.id)
        await interaction.response.send_message(content=f":euro: You have earned `{ezread(moneydiff)}{currency}` from your passives!\n-# `{ezread(userbalance_before)}{currency} -> {ezread(userbalance_after)}{currency}`")

    @app_commands.command(description="view the leaderboard :3")
    @app_commands.describe(
        full_leaderboard='display the top 10 instead of only the top 3'
    )
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def leaderboard(self, interaction: discord.Interaction, full_leaderboard: bool = False): # CREDITS TO CDC FOR CDC BOT LEADERBAORD IDK HOW TO SORT A STRING
            economy = get_economy()
            leaderboard = sorted(economy, key=lambda item: economy[item]["money"])
            leaderboard.reverse()
            embed = discord.Embed()
            embed.title = "Economy Leaderboard"
            embed.color = discord.Color.pink()
            try:
                embed.set_footer(text=f"""Your placement: {to_ordinal(leaderboard.index(str(interaction.user.id))+1)} Place""")
            except:
                embed.set_footer(text="You don't have any balance so I can't tell you your leaderboard placement!")
            p = 1
            if full_leaderboard:
                c = 10
            else:
                c = 3
            for user in leaderboard[:c]:
                embed.add_field(name=f"{to_ordinal(p)} Place:", value=f"""> User: <@{user}>\n> Balance: {ezread(economy[user]["money"])}{currency}""", inline=False)
                p = p + 1
            await interaction.response.send_message(embed=embed)

    @app_commands.command(description="fix inflation in the economy :3")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def fix_economy(self, interaction: discord.Interaction):
            if not interaction.user.id == self.bot.owner_id:
                await interaction.response.send_message(f"Sorry! This is <@{self.bot.owner_id}> only, please ask **them** to run this command if really needed")
                return
            economy = get_economy()
            leaderboard = sorted(economy, key=lambda item: economy[item]["money"])
            leaderboard.reverse()
            def isinflated():
                economy = get_economy()
                leaderboard = sorted(economy, key=lambda item: economy[item]["money"])
                leaderboard.reverse()
                t10 = 0
                for user in leaderboard[:10]:
                    t10 = t10 + economy[user]["money"]
                if t10 > 9873426756928365897236000000000: return True
                else: return False
            def gett10():
                economy = get_economy()
                leaderboard = sorted(economy, key=lambda item: economy[item]["money"])
                leaderboard.reverse()
                t10 = 0
                for user in leaderboard[:10]:
                    t10 = t10 + economy[user]["money"]
                return t10
            if not isinflated():
                await interaction.response.send_message("There is nothing to fix!")
                return
            fixlog = f"# INFLATION DETECTED (t10 is `{gett10()}{currency}`)! PREPARING FIXING PROCESS"
            await interaction.response.send_message(fixlog)
            while isinflated():
                economy = get_economy()
                leaderboard = sorted(economy, key=lambda item: economy[item]["money"])
                leaderboard.reverse()
                for user in leaderboard[:1]:
                    update_balance(user, -economy[user]["money"], "economy fixing")
                    usermisc = get_misc(user)
                    usermisc["hasbeenwiped"] = True
                    set_misc(user, usermisc)
                fixlog = fixlog + f"\n-# <@{leaderboard[0]}>, WIPED, `t10={gett10()}`"
                await interaction.edit_original_response(content=fixlog)
            await interaction.edit_original_response(content=f"{fixlog}\nEconomy fixed!")

    @app_commands.command(description="check your inventory :3")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def inventory(self, interaction: discord.Interaction):
            if await do_ratelimit(interaction): return
            userinv = get_inventory(interaction.user.id)

            if len(userinv) == 0:
                await interaction.response.send_message(content=f"Your inventory is empty :pensive:")
                return

            embed = discord.Embed()
            embed.title = "Your Inventory"
            embed.color = discord.Color.pink()

            for item in userinv:
                embed.add_field(name=f"""{userinv[item]["name"]}:""", value=f"""> Description: {userinv[item]["description"]}\n> MSRP Price: {ezread(userinv[item]["price"])}{currency}""", inline=False)
            await interaction.response.send_message(embed=embed)

    @app_commands.command(description="giveaway some money :3")
    @app_commands.describe(
        amount='amount of currency to giveaway'
    )
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def giveaway(self, interaction: discord.Interaction, amount: str):
        if await do_ratelimit(interaction): return
        amount = unpacknumbers(amount)
        if amount < 0:
            await interaction.response.send_message(content=f"That's not how money works(Atleast in this case Tax evasion is something different)")
            return

        try:
            eco = list(get_economy())
            eco.remove(str(interaction.user.id))
            winnerid = random.choice(eco)
        except ValueError: # user is not in economy (probably)
            await interaction.response.send_message("You dont have any balance so i cant really give away anything")
            return
        except IndexError: # no one to give away to
            await interaction.response.send_message("There's no one you can give this to")
            return

        payeebalance_before = get_balance(winnerid)
        userbalance_before = get_balance(interaction.user.id)
        if userbalance_before < amount:
            await interaction.response.send_message(content=f"You dont have enough money for this `({ezread(userbalance_before)}{currency} < {ezread(amount)}{currency})`")
            return
        update_balance(interaction.user.id, -amount, f"giveaway (remove money from giveawayer) ({interaction.user.name})")
        update_balance(winnerid, amount, f"giveaway (credit money to winner)")
        payeebalance_after = get_balance(winnerid)
        userbalance_after = get_balance(interaction.user.id)
        await interaction.response.send_message(content=f"Congratulations to <@{winnerid}> for winning `{ezread(amount)}{currency}`! \n-# `{interaction.user.name} {ezread(userbalance_before)}{currency} -> {ezread(userbalance_after)}{currency}`\n-# `giveaway winner {ezread(payeebalance_before)}{currency} -> {ezread(payeebalance_after)}{currency}`")

    @app_commands.command(description="russian roulette (if you lose you get WIPED) :3")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def russian_roulette(self, interaction: discord.Interaction):
        if await do_ratelimit(interaction): return
        userbalance_before = get_balance(interaction.user.id)
        if userbalance_before < 1000:
            await interaction.response.send_message(content=f"You dont have enough money for this `({userbalance_before}{currency} < 1000{currency})`")
            return
        await interaction.response.send_message(content=f"We are waiting for the result...")
        await asyncio.sleep(1)
        await interaction.edit_original_response(content=f".")
        await asyncio.sleep(1)
        await interaction.edit_original_response(content=f"..")
        await asyncio.sleep(1)
        await interaction.edit_original_response(content=f"...")
        userbalance_before = get_balance(interaction.user.id)
        if userbalance_before < 1000:
            await interaction.edit_original_response(content=f"I told you to not spam this fucking command `({userbalance_before}{currency} < 1000{currency})`")
            return
        if not len(get_cashdrops()) == 0:
            await interaction.edit_original_response(content=f"You can not use cashdrops to save yourself money! Please pickup all cash first before proceeding")
            return
        if random.randint(1, 6) == 1 or False: # redacted
            userbalance_before = get_balance(interaction.user.id)
            update_balance(interaction.user.id, -userbalance_before, f"Russian roulette, dying ({interaction.user.name})")
            #set_inventory(interaction.user.id, [])
            #set_passives(interaction.user.id, {})
            await interaction.edit_original_response(content=f"💥🔫 You died... Your balance has been ***WIPED***")
            return
        userbalance_before = get_balance(interaction.user.id)
        amount = round(userbalance_before * 1)
        update_balance(interaction.user.id, amount, f"Russian roulette, winning ({interaction.user.name})")
        userbalance_after = get_balance(interaction.user.id)
        await interaction.edit_original_response(content=f"You didn't die and won `{ezread(amount)}{currency}`!!!!!!! \n-# `{interaction.user.name} {ezread(userbalance_before)}{currency} -> {ezread(userbalance_after)}{currency}`")


    @app_commands.command(description="drop some money :3")
    @app_commands.describe(
        amount='amount of currency to drop'
    )
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def drop_cash(self, interaction: discord.Interaction, amount: str):
        if await do_ratelimit(interaction): return
        amount = unpacknumbers(amount)
        if amount < 0:
            await interaction.response.send_message(content=f"That's not how money works(Atleast in this case Tax evasion is something different)", ephemeral=True)
            return

        userbalance_before = get_balance(interaction.user.id)
        if userbalance_before < amount:
            await interaction.response.send_message(content=f"You dont have enough money for this `({ezread(userbalance_before)}{currency} < {ezread(amount)}{currency})`", ephemeral=True)
            return

        cashdrops = get_cashdrops()
        if amount in cashdrops:
            await interaction.response.send_message(content=f"theres already that money on the ground", ephemeral=True)
            return
        cashdrops.append(amount)
        update_balance(interaction.user.id, -amount, f"cashdrop (remove money from dropper) ({interaction.user.name})")
        set_cashdrops(cashdrops)
        logger.info(f"{interaction.user.name} dropped {amount}{currency}!!!")
        userbalance_after = get_balance(interaction.user.id)
        await interaction.response.send_message(content=f"You dropped `{ezread(amount)}{currency}`! \n-# `{interaction.user.name} {ezread(userbalance_before)}{currency} -> {ezread(userbalance_after)}{currency}`", ephemeral=True)

    @app_commands.command(description="pickup some money :3")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def pickup_cash(self, interaction: discord.Interaction):
        if await do_ratelimit(interaction): return
        userbalance_before = get_balance(interaction.user.id)
        cashdrops = get_cashdrops()
        if len(cashdrops) == 0:
            await interaction.response.send_message(content=f"There's no cash to be found :pensive:")
            return
        amount = cashdrops[0]
        cashdrops.pop(0)
        set_cashdrops(cashdrops)
        logger.info(interaction.user.name)
        update_balance(interaction.user.id, amount, f"cashdrop (add money to pickupper) ({interaction.user.name})")
        usermisc = get_misc(interaction.user.id)
        if "total_pickup" not in usermisc:
            usermisc["total_pickup"] = 0
        usermisc["total_pickup"] = usermisc["total_pickup"] + amount
        set_misc(interaction.user.id, usermisc)
        userbalance_after = get_balance(interaction.user.id)
        await interaction.response.send_message(content=f"You picked up `{ezread(amount)}{currency}`! \n-# `{interaction.user.name} {ezread(userbalance_before)}{currency} -> {ezread(userbalance_after)}{currency}`")

    @app_commands.command(description="view your medals :3")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def medals(self, interaction: discord.Interaction):
            if await do_ratelimit(interaction): return

            medalinv = {} # medals will be calculated everytime the command is run

            userinv = get_inventory(interaction.user.id)
            userpassives = get_passives(interaction.user.id)
            userbalance = get_balance(interaction.user.id)
            usermisc = get_misc(interaction.user.id)

            if interaction.user.id == 729671931359395940: # geming
                medalinv["geming"] = {
                    "name": "Being Lesbian and Trans",
                    "description": "A medal for the best geming person who is Lesbian and trans, awarded to the Lesbian and Trans"
                }

            if len(userpassives) > 0:
                medalinv["ttgafk"] = {
                    "name": "Time to go AFK!",
                    "description": "Buy your first passive"
                }

            if "hasbeenwiped" in usermisc and usermisc["hasbeenwiped"]:
                medalinv["wiped"] = {
                    "name": "Economy inflater",
                    "description": "get wiped once"
                }
            
            if "dc" in userinv:
                medalinv["dc"] = {
                    "name": "No",
                    "description": "Prevent stealing by having a debit card"
                }

            if "work_count" in usermisc and usermisc["work_count"] >= 1000:
                medalinv["workeroftheyear"] = {
                    "name": "Worker of the year",
                    "description": "Work 1000+ times in total"
                }

            if userbalance >= unpacknumbers("10BSKY"):
                medalinv["touchgrass"] = {
                    "name": "Maybe try touching grass?",
                    "description": f"get 10+ BSKY{currency}"
                }

            if "iscool" in usermisc and usermisc["iscool"]:
                medalinv["very cool"] = {
                    "name": "a very cool medal",
                    "description": "a very cool medal awarded to very cool people"
                }

            if "stolen_total" in usermisc and usermisc["stolen_total"] >= 100:
                medalinv["thief1"] = {
                    "name": "Thief",
                    "description": "steal 100 in total from someone!"
                }

            if "stolen_total" in usermisc and usermisc["stolen_total"] >= 1000:
                medalinv["thief2"] = {
                    "name": "Thief II",
                    "description": "steal 1000 in total from someone!"
                }

            if "stolen_total" in usermisc and usermisc["stolen_total"] >= 3000:
                medalinv["thief3"] = {
                    "name": "Thief",
                    "description": "steal 3k in total from someone!"
                }

            if "total_pickup" in usermisc and usermisc["total_pickup"] >= 1000000:
                medalinv["pikcup"] = {
                    "name": "Street Life",
                    "description": f"pickup 1 million+ {currency} in total"
                }



            if len(medalinv) == 0:
                await interaction.response.send_message(content=f"You don't have any medals :pensive:")
                return

            embed = discord.Embed()
            embed.title = "Your Medals"
            embed.color = discord.Color.pink()

            for item in medalinv:
                embed.add_field(name=f"""{medalinv[item]["name"]}""", value=f"""> {medalinv[item]["description"]}""", inline=False)
            await interaction.response.send_message(embed=embed)

    @app_commands.command(description = "delete all your money, items, etc. IRREVERSIBLY :3")
    @app_commands.describe(
        confirm='do you REALLY want to IRREVERSIBLY delete?',
    )
    @app_commands.allowed_installs(guilds = True, users = True)
    @app_commands.allowed_contexts(guilds = True, dms = True, private_channels = True)
    async def reset_own_money(self, interaction: discord.Interaction, confirm: bool = False):
        if confirm:
            await interaction.response.send_modal(ConfrimDeleteModal())
        else:
            await interaction.response.send_message(content=f"No Confirmation provided")

    @app_commands.command(description = "get info about the next update :3")
    @app_commands.allowed_installs(guilds = True, users = True)
    @app_commands.allowed_contexts(guilds = True, dms = True, private_channels = True)
    async def update_info(self, interaction: discord.Interaction):
            await interaction.response.send_message(content=updateinfo)



async def setup(bot: commands.Bot):
    await bot.add_cog(Economy(bot))
