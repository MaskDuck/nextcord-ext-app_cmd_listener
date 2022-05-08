from nextcord.ext import commands

from nextcord import InteractionType

__all__ = ["AppCmdListener"]

class AppCmdListener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_interaction(self, interaction):
        if interaction.type == InteractionType.application_command:
            self.bot.dispatch("application_command", interaction)
    

