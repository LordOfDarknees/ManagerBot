from disnake.ext.commands import Bot, Cog, slash_command
from disnake.errors import Forbidden
from disnake import ApplicationCommandInteraction, Member, Guild
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
        if not await self.kickPermission(interaction.user, interaction.guild):
            await interaction.response.send_message("You are not allowed to do that yk!")
            return
        
        if self.bot.user.id == member.id:
            await interaction.response.send_message("Sir i cant kick myself?")
            return
        
        try:
            member.roles
        except Exception as e:
            await interaction.response.send_message("Member does not exist on this server!")
            print(e)
            return
        
        try:
            await member.kick(reason=reason)
        except Forbidden:
            await interaction.response.send_message("Not possible sir i do not have permission!", ephemeral=True)
        else:
            await interaction.response.send_message(f"Its done sir {member.name} is gone! for now...")
        
    async def kickPermission(self, member: Member, guild: Guild):
        if guild.owner_id == member.id:
            return True
        
        roles = member.roles
        for role in roles:
            if role.permissions.kick_members or role.permissions.administrator:
                return True
        return False

def setup(bot: Bot) -> None:
    bot.add_cog(name(bot))