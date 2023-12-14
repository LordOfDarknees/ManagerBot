from disnake import Embed, Color
from disnake.ext.commands import Bot, Cog, slash_command
from disnake import ApplicationCommandInteraction
from pathlib import Path
from sys import path

path_root = Path(__file__).parents[2]
path.append(str(path_root))

from utils.OwnerCheck import Owner

class bulkclear(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot
    
    @slash_command(description="bulkclears MSGs")
    async def bulkclear(self, interaction: ApplicationCommandInteraction, number:int):
        if not await Owner().isOwner(self.bot, interaction.user.id):
            await interaction.response.send_message("You are not a Owner!\nYou are not Permitted to use this command")
            return
        wip_embed = Embed(title="bulkclear Command", description="Im working on it!\nMay take a while!", color=Color.orange())
        await interaction.response.send_message(embed=wip_embed,ephemeral=True)
        mgs = [] #Empty list to put all the messages in the log
        multiple = []
        #Converting the amount of messages to delete to an integer
        async for x in interaction.channel.history(limit = number):
            mgs.append(x)
        if len(mgs) > 100:
            temp = []
            for entry in mgs:
                if len(temp) == 100:
                    multiple.append(temp)
                    temp = []
                temp.append(entry)
            for entry in multiple:
                await interaction.channel.purge()
        await interaction.channel.purge(limit=number)
                
        done_embed = Embed(title="bulkclear Command", description="Everything is done now!", color=Color.green())
        await interaction.edit_original_response(embed=done_embed)
        


def setup(bot: Bot) -> None:
    bot.add_cog(bulkclear(bot))