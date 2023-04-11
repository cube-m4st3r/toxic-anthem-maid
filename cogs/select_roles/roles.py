import os
import time

import discord
from discord import app_commands
from discord.ext import commands
from classes.roles import Roles


class RoleMenuSelect(discord.ui.RoleSelect):
    def __init__(self, bot=discord.Client):
        super().__init__(placeholder="Select the roles", min_values=1, max_values=10)
        self.bot = bot

    async def callback(self, interaction: discord.Interaction):

        output = discord.Embed(title="Select your Role")

        roles = Roles()
        for role in self.values:
            roles.set_role_id(role.id)
            roles.set_role_name(role.name)
            roles.set_role_color_code(role.color)
            output.add_field(name=role.mention, value="Role")

        await interaction.message.edit(embed=output, view=None)


class SelectRoleMenuView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(RoleMenuSelect())


class RoleMenuButton(discord.ui.Button):
    def __init__(self, text, buttonStyle, mode):
        super().__init__(label=text, style=buttonStyle)
        self.mode = mode

    async def callback(self, interaction: discord.Interaction):

        if self.mode == 0:
            await interaction.response.send_message("Role1")
        elif self.mode == 1:
            await interaction.response.send_message("Role2")
        elif self.mode == "cancel":
            await interaction.response.send_message("Cancel")


class RoleMenuView(discord.ui.View):
    def __init__(self, roles):
        super().__init__(timeout=None)
        self.roles = roles
        self.add_item(RoleMenuButton("Role1", discord.ButtonStyle.primary, 0))
        self.add_item(RoleMenuButton("Role2", discord.ButtonStyle.primary, 1))
        self.add_item(RoleMenuButton("cancel", discord.ButtonStyle.primary, "cancel"))


class roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="create_role", description="Create a Role")
    @app_commands.checks.has_role("Discord Manager" or "Master")
    async def create_role(self, interaction: discord.Interaction, role_name: str):
        await interaction.response.send_message("Create a role with this command!")

    @app_commands.command(name="delete_role", description="Delete a Role")
    @app_commands.checks.has_role("Discord Manager")
    @app_commands.checks.has_role("Master")
    async def delete_role(self, interaction: discord.Interaction, role_name: str):
        await interaction.respone.send_message("Delete a role with this command!")

    @app_commands.command(name="change_role", description="Change a Role")
    @app_commands.checks.has_role("Discord Manager" or "Master")
    @app_commands.choices(choices=[
        app_commands.Choice(name="Name", value="role_name"),
        app_commands.Choice(name="Color", value="role_color")
    ])
    async def change_role(self, interaction: discord.Interaction, choices: app_commands.Choice[str]):
        await interaction.response.send_message(view=SelectRoleMenuView())


    @app_commands.command(name="new_role_menu", description="Create a new Role Menu")
    @app_commands.checks.has_role("Discord Manager" or "Master")
    async def new_role_menu(self, interaction: discord.Interaction):
        await interaction.response.send_message(content="role_menu", view=SelectRoleMenuView())


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(roles(bot), guild=discord.Object(id=os.getenv("GUILD-ID")))
