import enum
import os
import time

import discord
from discord import app_commands
from discord.ext import commands

from classes.button import Button
from classes.menu_embed import Menu_Embed
from classes.roles import Roles
from random import randrange

from database import database as db

tRoles = None

class RoleMenuSelect(discord.ui.RoleSelect):
    def __init__(self, bot=discord.Client):
        super().__init__(placeholder="Select the roles", min_values=1, max_values=10)
        self.bot = bot

    async def callback(self, interaction: discord.Interaction):

        embed = discord.Embed(title="Select your Role")

        while True:
            id = randrange(100)

            if db.check_role_menu_embed(str(id)):
                return
            else:
                embed.set_footer(text=(f"ID: {str(id)}"))
                break

        global tRoles
        tRoles = list()

        buttons = []

        rolemenubutton = RoleMenuButtonView()
        db.insert_menu_embed(id, interaction.message.id, embed.title, embed.description)
        for role in self.values:
            roles = Roles(role.id, role.name)
            if db.check_role(roles.get_role_id()) is False:
                db.insert_role(roles.get_role_id(), roles.get_role_name())
            embed.add_field(name=roles.get_role_name(), value="Role", inline=False)
            db.insert_role_menu_embed(roles.get_role_id(), id, "description")

            role_button = RoleMenuButton(roles.get_role_name(), discord.ButtonStyle.primary, roles.get_role_name())
            rolemenubutton.add_item(role_button)
            button_class = Button(role_button.mode)

            roles.set_role_button(button_class)

            tRoles.append(roles)

        menu_embed = Menu_Embed(id, interaction.message.id, embed.title, embed.description, tRoles)
        menu_roles = menu_embed.get_roles()

        await interaction.response.send_message(embed=embed, view=rolemenubutton)


class RoleDeleteSelect(discord.ui.RoleSelect):
    def __init__(self):
        super().__init__(placeholder="Select the role", min_values=1, max_values=1)

    async def callback(self, interaction: discord.Interaction):

        role = self.values[0]

        await interaction.response.send_message(f"{role}")
        await role.delete()


class RoleChangeSelect(discord.ui.RoleSelect):
    def __init__(self):
        super().__init__(placeholder="Select the role", min_values=1,max_values=1)

    async def callback(self, interaction: discord.Interaction):
        role = self.values[0]
        print(role.id)
        await interaction.response.send_modal(RoleChangeNameModal(role))


class RoleChangeNameModal(discord.ui.Modal):
    def __init__(self, role: discord.Role):
        super().__init__(title=f"Change name of {role.name}")
        self.role = role

    role_name = discord.ui.TextInput(label="Name", style=discord.TextStyle.short, placeholder="Please enter a valid name", required=True)

    async def on_submit(self, interaction: discord.Interaction):

        new_role_name = await self.role.edit(name=self.role_name.value)
        await interaction.response.send_message(content=f"Changed the name of {self.role.name} to {new_role_name.name}")

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
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(RoleMenuSelect())


class RoleMenuButtonView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)


class RoleDeleteView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(RoleDeleteSelect())


class SelectRoleChangeView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(RoleChangeSelect())


class roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name="create_role", description="Create a Role")
    @app_commands.checks.has_role("Discord Manager" or "Master")
    async def create_role(self, interaction: discord.Interaction, role_name: str):
        await interaction.response.send_message("Create a role with this command!")


    @app_commands.command(name="delete_role", description="Delete a Role")
    @app_commands.checks.has_role("Discord Manager")
    async def delete_role(self, interaction: discord.Interaction):
        await interaction.response.send_message(view=RoleDeleteView())


    @app_commands.command(name="change_role", description="Change a Role")
    @app_commands.checks.has_role("Discord Manager" or "Master")
    @app_commands.choices(choices=[
        app_commands.Choice(name="Name", value="role_name"),
        app_commands.Choice(name="Color", value="role_color")
    ])
    async def change_role(self, interaction: discord.Interaction, choices: app_commands.Choice[str]):
        await interaction.response.send_message(view=SelectRoleChangeView())


    @app_commands.command(name="new_role_menu", description="Create a new Role Menu")
    @app_commands.checks.has_role("Discord Manager" or "Master")
    async def new_role_menu(self, interaction: discord.Interaction, text_channel: discord.TextChannel):
        await interaction.response.send_message(view=RoleMenuView())


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(roles(bot), guild=discord.Object(id=os.getenv("GUILD-ID")))
