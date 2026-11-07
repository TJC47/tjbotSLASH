import discord
from discord import app_commands
from discord.ext import commands
import time
import json
import discord
import logging
import redis
import math
from economy import ezread, to_ordinal

logger = logging.getLogger("tjbot.leveling")


r = redis.Redis(host='localhost', port=6379, decode_responses=True)



with open("levelconfig.json") as f:
    config = json.loads(f.read())

GROWTH_RATE = config.get("growth_rate")
BASE_XP = config.get("base_xp")
XP_PER_VALID_MESSAGE = config.get("xp_per_valid_message")
SPAM_XP_DEDUCTION = config.get("spam_xp_deduction")
VALID_MESSAGE_TIME = config.get("valid_message_time")
XP_PER_RECEIVED_REACTION = config.get("xp_per_received_reaction")
POINTS_PER_LEVEL = config.get("points_per_level")


with open("xpitemlist.json") as f:
    xpShopItems = json.loads(f.read())

def get_xp_for_level(level: int) -> int:
    return int(BASE_XP * (GROWTH_RATE ** level - 1) / (GROWTH_RATE - 1))

def get_level_for_xp(xp: int) -> int:
    return max(0, int(math.log1p(xp * (GROWTH_RATE - 1) / BASE_XP) / math.log(GROWTH_RATE)))

def give_item(userid: int, item: str) -> bool:
    return False # TODO: ADD THIS!!!

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
    def __init__(self, xp: int, level: int, eligible_messages_sent: int, total_messages_sent: int, last_eligible_message_timestamp: float, local_xp: int, local_xp_for_next_level: int, message_reactions_received: int, message_reactions_given: int, total_points_earned: int, points_spent: int):
        self.xp = xp
        self.level = level
        self.eligible_messages_sent = eligible_messages_sent
        self.total_messages_sent = total_messages_sent
        self.last_eligible_message_timestamp = last_eligible_message_timestamp
        self.local_xp = local_xp
        self.local_xp_for_next_level = local_xp_for_next_level
        self.local_xp_progress = local_xp / local_xp_for_next_level
        self.eligible_ineligible_ratio = eligible_messages_sent / (total_messages_sent + 1)
        self.message_reactions_received = message_reactions_received
        self.message_reactions_given = message_reactions_given
        self.total_points_earned = total_points_earned
        self.points_spent = points_spent
        self.points = total_points_earned - points_spent

def get_level_user(userid: int) -> LevelUser:
    eligible_messages_sent = int(r.get(f"tjbot:levels:{userid}:eligible_messages_sent") or 0)
    total_messages_sent =  int(r.get(f"tjbot:levels:{userid}:total_messages_sent") or 0)
    last_eligible_message_timestamp =  float(r.get(f"tjbot:levels:{userid}:last_eligible_message_timestamp") or 0)
    message_reactions_received = int(r.get(f"tjbot:levels:{userid}:message_reactions_received") or 0)
    message_reactions_given = int(r.get(f"tjbot:levels:{userid}:message_reactions_given") or 0)
    points_spent = int(r.get(f"tjbot:levels:{userid}:points_spent") or 0)

    eligible_ineligible_ratio = eligible_messages_sent / (total_messages_sent + 1)

    xp = eligible_messages_sent * XP_PER_VALID_MESSAGE # xp from valid messages
    xp += message_reactions_received * XP_PER_RECEIVED_REACTION # xp from receiving reactions
    xp -= message_reactions_given * XP_PER_RECEIVED_REACTION # deducting xp when reacting (fairness), thinking about removing this or keeping it I'm not sure
    xp -= (total_messages_sent-eligible_messages_sent) * SPAM_XP_DEDUCTION # deducting xp from spammed messages
    xp *= 1 + eligible_ineligible_ratio # xp multiplier
    xp = round(xp) # final round

    level = get_level_for_xp(xp)

    r.zadd("tjbot:xp_leaderboard", {str(userid): xp})

    local_xp = xp - get_xp_for_level(level)
    local_xp_for_next_level = get_xp_for_level(level + 1) - get_xp_for_level(level)

    total_points_earned = level * POINTS_PER_LEVEL # 4 points every level

    return LevelUser(
        xp,
        level,
        eligible_messages_sent,
        total_messages_sent,
        last_eligible_message_timestamp,
        local_xp,
        local_xp_for_next_level,
        message_reactions_received,
        message_reactions_given,
        total_points_earned,
        points_spent
    )

class Leveling(commands.GroupCog, group_name="xp"):
    def __init__(self, bot: commands.Bot) :
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message = await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
        r.incr(f"tjbot:levels:{message.author.id}:message_reactions_received")
        r.incr(f"tjbot:levels:{payload.user_id}:message_reactions_given")


    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        message = await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
        r.decr(f"tjbot:levels:{message.author.id}:message_reactions_received")
        r.decr(f"tjbot:levels:{payload.user_id}:message_reactions_given")

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot: return
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
        await interaction.response.defer()
        if not user: user = interaction.user

        level_info = get_level_user(user.id)

        embed = discord.Embed()
        embed.color = discord.Color.blurple()

        embed.description = f"### {user.mention}'s Level Card"
        embed.add_field(name="Level", value=level_info.level)
        embed.add_field(name="Total XP Earned", value=ezread(level_info.xp))
        embed.add_field(name="Points Available", value=ezread(level_info.points))
        embed.add_field(name="Total Messages Sent", value=ezread(level_info.total_messages_sent), inline=False)
        embed.add_field(name="Total Message Reactions Received", value=ezread(level_info.message_reactions_received))
        embed.add_field(name="Current Progress", value=f"`{progress_bar(level_info.local_xp_progress)}` **{level_info.local_xp_progress*100:.2f}%**\n-# {ezread(level_info.local_xp)}/{ezread(level_info.local_xp_for_next_level)}XP", inline=False)
        embed.add_field(name="XP Boost", value=f"`{progress_bar(level_info.eligible_ineligible_ratio)}` **{level_info.eligible_ineligible_ratio*100:.2f}%**")

        embed.set_footer(text="XP is earned by chatting normally. Spamming messages or attempting to game the system will result in an XP deduction.")

        await interaction.edit_original_response(embed=embed)



    @app_commands.command(description="view the xp shop :3")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def shop(self, interaction: discord.Interaction):
            await interaction.response.defer()
            user = get_level_user(interaction.user.id)


            embed = discord.Embed()
            embed.title = "XP Shop"
            embed.set_footer(text=f"Your Balance: {ezread(user.points)} Points, use /xp buy to buy your selected product")
            embed.color = discord.Color.pink()


            for item in xpShopItems:
                embed.add_field(name=f"""{xpShopItems[item]["name"]}:""", value=f"""> **Description:** {xpShopItems[item]["description"]}\n> **Price:** {ezread(xpShopItems[item]["price"])} Points""", inline=True)
            await interaction.edit_original_response(embed=embed)



    async def shop_ac(self, interaction: discord.Interaction, current: str) -> list[app_commands.Choice[str]]:
        choices = []
        user = get_level_user(interaction.user.id)
        choices.append(app_commands.Choice(name = f"""------------ Your Balance: {ezread(user.points)} Points ------------""",value = "null"))
        for item in xpShopItems:
            if current.lower() in xpShopItems[item].get("name").lower(): # and item not in get_inventory(interaction.user.id):
                canbuy = "❌"
                if user.points >= xpShopItems[item]["price"]:
                    canbuy = "✅"
                choices.append(app_commands.Choice(name = f"""{xpShopItems[item]["name"]} - {ezread(xpShopItems[item]["price"])} Points - Can buy: {canbuy}""", value = item))

        return choices

    @app_commands.command(description = "Buy something from the xp shop :3")
    @app_commands.describe(
        item='Item to buy',
    )
    @app_commands.autocomplete(item = shop_ac)
    @app_commands.allowed_installs(guilds = True, users = True)
    @app_commands.allowed_contexts(guilds = True, dms = True, private_channels = True)
    async def buy(self, interaction: discord.Interaction, item: str):
        await interaction.response.defer()
        if item in xpShopItems:
            user = get_level_user(interaction.user.id)
            if xpShopItems[item]["price"] > user.points:
                await interaction.edit_original_response(content = f"""You can't afford this item!""")
                return
            if not give_item(interaction.user.id, item):
                await interaction.edit_original_response(content = f"""An error occured applying the item to your user account or you already have {xpShopItems[item]["pronouns"]} {xpShopItems[item]["name"]}! Please try again later.""")
                return


            await interaction.edit_original_response(content = f"""You successfully purchased {xpShopItems[item]["pronouns"]} {xpShopItems[item]["name"]}!""")
        else:
            await interaction.edit_original_response(content = f"That item doesn't exist!")

    @app_commands.command(description="view the xp leaderboard :3")
    @app_commands.describe(
        full_leaderboard='display the top 10 instead of only the top 3'
    )
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def leaderboard(self, interaction: discord.Interaction, full_leaderboard: bool = False):
            await interaction.response.defer()
            leaderboard = r.zrevrange("tjbot:xp_leaderboard", 0, 9)
            embed = discord.Embed()
            embed.title = "XP Leaderboard"
            embed.color = discord.Color.pink()
            try:
                embed.set_footer(text=f"""Your placement: {to_ordinal(r.zrevrank("tjbot:xp_leaderboard", str(interaction.user.id))+1)} Place""")
            except:
                embed.set_footer(text="You don't have any XP so I can't tell you your leaderboard placement!")
            p = 1
            if full_leaderboard:
                c = 10
            else:
                c = 3
            for user in leaderboard[:c]:
                level_info = get_level_user(user)
                embed.add_field(name=f"{to_ordinal(p)} Place:", value=f"""> **User:** <@{user}>\n> **XP:** {ezread(level_info.xp)}\n> **Level:** {level_info.level}""", inline=False)
                p = p + 1
            await interaction.edit_original_response(embed=embed)

    @app_commands.command(description="[bot-owner only] force-refresh ALL users in leaderboard, may be VERY slow :3")
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def refresh_leaderboard(self, interaction: discord.Interaction):
            await interaction.response.defer()

            starttime = time.time()

            leaderboard = r.zrevrange("tjbot:xp_leaderboard", 0, -1)

            for user in leaderboard:
                level_info = get_level_user(user) # Fetching the user refreshes the leaderboard placement
                logger.info(f"Refreshed leaderboard placement for '{user}': has {level_info.xp}XP, at level {level_info.level}")
            await interaction.edit_original_response(content=f"Refresh completed in `{time.time()-starttime:.2f}seconds`. Check logs for detailed information.")


async def setup(bot: commands.Bot):
    await bot.add_cog(Leveling(bot))