import os

import discord
from discord import app_commands
from discord.ext import commands
from PIL import Image
from io import BytesIO

class wanted(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="wanted", description="Wanted image with user")
    async def wanted_image(self, interaction: discord.Interaction, member: discord.Member=None):

        if member == None:
            member = interaction.user

        wanted = Image.open("cogs/join_event/wanted.jpg")

        data = BytesIO(await member.display_avatar.read())
        pfp = Image.open(data)

        pfp = pfp.resize((900, 900))

        wanted.paste(pfp, (550, 878)) #no float

        wanted.save("cogs/join_event/profile.jpg")

        await interaction.response.send_message(file=discord.File("cogs/join_event/profile.jpg"))

        os.remove("cogs/join_event/profile.jpg")

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(wanted(bot), guild=discord.Object(id=os.getenv("TESTING-GUILD-ID")))