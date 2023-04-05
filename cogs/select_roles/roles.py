import os

import discord
from discord import app_commands
from discord.ext import commands

class RoleMenuButton(discord.ui.Button):
    def __init__(self, text, buttonStyle, mode):
        super().__init__(label=text, style=buttonStyle)
        self.mode = mode

class RoleMenuView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(RoleMenuButton("Role1", discord.ButtonStyle.primary, 0))

class roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="create_role", description="Create a Role")
    @app_commands.checks.has_role("Discord Manager" or "Master")
    async def create_role(self, interaction: discord.Interaction, role_name: str):
        await interaction.response.send_message("Create a role with this command!")
        print(role_name)

    @app_commands.command(name="new_role_menu", description="Create a new Role Menu")
    @app_commands.checks.has_role("Discord Manager" or "Master")
    async def new_role_menu(self, interaction: discord.Interaction):
        await interaction.response.send_message("role_menu")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(roles(bot), guild=discord.Object(id = os.getenv("GUILD-ID")))

