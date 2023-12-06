from disnake import Game, Status
from disnake.ext.commands import Bot, Cog, slash_command, default_member_permissions, param
from disnake import ApplicationCommandInteraction
from time import sleep
from sys import executable, path, argv
from os import execv
from pathlib import Path

path_root = Path(__file__).parents[2]
path.append(str(path_root))

from utilitys.OwnerCheck import Owner

class restart(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot
    
    @slash_command(description="RestartTheBot")
    async def restart(self, interaction: ApplicationCommandInteraction):
        if not await Owner().isOwner(self.bot, interaction.user.id):
            await interaction.response.send_message("You are not a Owner!\nYou are not Permitted to use this command")
            return
        game = Game("Restarting")

        await interaction.response.send_message("Goodbye")
        await self.bot.change_presence(activity=game)
        await self.bot.change_presence(status=Status.offline)
        sleep(1)
        print("restarting..")
        self.restart_bot()

    def restart_bot(self): 
        execv(executable, ['python'] + argv)
        


def setup(bot: Bot) -> None:
    bot.add_cog(restart(bot))