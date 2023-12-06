from disnake import Game, Status
from disnake.ext.commands import Bot, Cog, slash_command
from disnake import ApplicationCommandInteraction
from pathlib import Path
from sys import path

path_root = Path(__file__).parents[2]
path.append(str(path_root))

from utilitys.OwnerCheck import Owner

class stop(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot
    
    @slash_command(description="StopTheBot")
    async def stop(self, interaction: ApplicationCommandInteraction):
        if not await Owner().isOwner(self.bot, interaction.user.id):
            await interaction.response.send_message("You are not a Owner!\nYou are not Permitted to use this command")
            return
        game = Game("Offline")

        await interaction.response.send_message("Goodbye")
        await self.bot.change_presence(activity=game)
        await self.bot.change_presence(status=Status.offline)
        await self.bot.close()


def setup(bot: Bot) -> None:
    bot.add_cog(stop(bot))