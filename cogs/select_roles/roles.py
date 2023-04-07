import os
import time

import discord
from discord import app_commands
from discord.ext import commands


class RoleMenuButton(discord.ui.Button):
    def __init__(self, text, buttonStyle, mode):
        super().__init__(label=text, style=buttonStyle)
        self.mode = mode

    async def callback(self, interaction: discord.Interaction):

        if self.mode == 0:
            await interaction.response.send_message("Role1")
        elif self.mode == 1:
            await interaction.response.send_message("Role2")
        elif self.moode == "cancel":
            await interaction.response.send_message("Cancel")


class RoleMenuView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(RoleMenuButton("Role1", discord.ButtonStyle.primary, 0))
        self.add_item(RoleMenuButton("Role2", discord.ButtonStyle.primary, 1))
        self.add_item(RoleMenuButton("cancel", discord.ButtonStyle.primary, "cancel"))


class RoleMenuSelect(discord.ui.RoleSelect):
    def __init__(self, bot = discord.Client):
        super().__init__(placeholder="Wähle deine gewünschte(n) Rolle(n) aus", min_values=1, max_values=10)
        self.bot = bot
    async def callback(self, interaction: discord.Interaction):
        roles = list()
        for res in self.values:
            roles.append(res.mention)

        message = await interaction.message.edit(content=' '.join(sorted(roles)), view=None)
        messageid = message.id

        guild = interaction.guild
        channel = guild.get_channel(interaction.channel_id)
        msg = await channel.fetch_message(messageid)
        time.sleep(5)
        await msg.edit(content="test")



class SelectRoleMenuView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(RoleMenuSelect())


class roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="create_role", description="Create a Role")
    @app_commands.checks.has_role("Discord Manager" or "Master")
    async def create_role(self, interaction: discord.Interaction, role_name: str):
        await interaction.response.send_message("Create a role with this command!")

    @app_commands.command(name="new_role_menu", description="Create a new Role Menu")
    @app_commands.checks.has_role("Discord Manager" or "Master")
    async def new_role_menu(self, interaction: discord.Interaction):
        await interaction.response.send_message(content="role_menu", view=SelectRoleMenuView())


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(roles(bot), guild=discord.Object(id=os.getenv("GUILD-ID")))
