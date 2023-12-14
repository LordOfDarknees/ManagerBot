from disnake.ext.commands import Bot, Cog, slash_command
from disnake import ApplicationCommandInteraction
from pathlib import Path # Needed for importing Modules from Siblings folder from parent
from sys import path # Needed for importing Modules from Siblings folder from parent

path_root = Path(__file__).parents[2] # Get the Folder 2 outside of current one
path.append(str(path_root)) # Add the previos found folder to path to be able to import stuff from there

from utilitys.OwnerCheck import Owner

class multiplecountto(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot
    
    @slash_command(description="Describstion")
    async def multiplecountto(self, interaction: ApplicationCommandInteraction, end: int, start: int = 0):
        await interaction.response.send_message("Okay give me a second im sending all numbers in range")
        num = range(start, end)
        channel = interaction.channel
        for number in num:
            await channel.send(number)
        await interaction.send("Done!")    


def setup(bot: Bot) -> None:
    bot.add_cog(multiplecountto(bot))