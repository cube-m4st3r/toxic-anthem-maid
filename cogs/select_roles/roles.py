import os

import discord
from discord import app_commands
from discord.ext import commands

class roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="create_role", description="Create a Role")
    @app_commands.checks.has_role("Discord Manager" or "Master")
    async def create_role(self, interaction: discord.Interaction, role_name: str):
        await interaction.response.send_message("Create a role with this command!")
        print(role_name)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(roles(bot), guild=discord.Object(id = os.getenv("GUILD-ID")))

