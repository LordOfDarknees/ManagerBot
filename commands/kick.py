from disnake.ext.commands import Bot, Cog, slash_command
from disnake import ApplicationCommandInteraction, Member
from pathlib import Path # Needed for importing Modules from Siblings folder from parent
from sys import path # Needed for importing Modules from Siblings folder from parent

path_root = Path(__file__).parents[2] # Get the Folder 2 outside of current one
path.append(str(path_root)) # Add the previos found folder to path to be able to import stuff from there

from utilitys.OwnerCheck import Owner

class name(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot
    
    @slash_command(description="Describstion")
    async def name(self, interaction: ApplicationCommandInteraction, member: Member, reason: str = "You dont belong here!"):
        if not self.kickPermission(interaction.user):
            interaction.response.send_message("You are not allowed to do that yk!")
            return
        member.kick(reason)
            
    async def kickPermission(self, member: Member):
        roles = member.roles
        for role in roles:
            if role.permissions.kick_members or role.permissions.administrator:
                return True
        return False

def setup(bot: Bot) -> None:
    bot.add_cog(name(bot))