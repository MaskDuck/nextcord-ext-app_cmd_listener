from nextcord.ext import commands
from nextcord.ext import app_cmd_listener

bot = commands.Bot(command_prefix="$")

bot.add_cog(app_cmd_listener.AppCmdListener(bot))

@bot.event
async def on_application_command(self, interaction):
    print("Hello world")

bot.run("token here")
