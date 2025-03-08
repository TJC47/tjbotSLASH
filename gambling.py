import discord
from discord import app_commands
from discord.ext import commands
import random
import asyncio
import mariadb

class Gambling(commands.Cog):
    def __init__(self, bot: commands.Bot) :
        self.bot = bot


    @app_commands.command(description="This isnt rigged :3")
    @app_commands.describe(
        amount='how much to gamble',
    )
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def gambling(self, interaction: discord.Interaction, amount: int):
        await interaction.response.send_message(content=f"Let's go gambling!")
        try:
            conn = mariadb.connect(
                host="localhost",
                port=3306,
                user="tjc",
                password="i will NOT commit my hardcoded password"
            )
            await asyncio.sleep(1)
            if random.randint(1,10) ==5:
                await interaction.edit_original_response(content=f"You won {random.randint(1,amount)} trillon buckarroos!!!!\n-# WOHOOO!!!!")
            else:
                await interaction.edit_original_response(content=f"You lost {random.randint(1,amount)} trillon buckarroos!!!!")
            conn.close()
        except:
            await interaction.edit_original_response(content=f"there was an error with the database")

async def setup(bot: commands.Bot):
    await bot.add_cog(Gambling(bot))
