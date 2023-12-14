from disnake import Intents, Status, Game
from disnake.ext.commands import Bot
from configparser import ConfigParser
from sqlite3 import connect
from config.configChecker import Check
import os

Check() # Check if Ini File is not existand or corrupt

# Get Config
config_path = "config.ini" # config directory
config = ConfigParser() # Initiate the Config Parser
config.read(config_path) # Reading in the config


# Setup Database
host = config.get("Bot", "database")
con = connect(host)
cur = con.cursor()


# Get Values from Config
prefix = config.get("Bot", "prefix")
bot_token = config.get("Bot", "token")


# Bot Setup
guildIds = [1088215576507318424]
intents = Intents.default()
intents.reactions = True
intents.message_content = True
bot = Bot(command_prefix=prefix, intents=intents, test_guilds=guildIds)

# 408313404202418186 Alastor
bot.owner_ids = [408313404202418186]

# Design
underscores =   "____________________________________________________________________________________"
scores =        "---------------------------------------"
scores2 =       "-----------------------------------------------------------------------------------------"

# On startup of the bot
@bot.event
async def on_ready():
    print("Im on im on where is my Cofee?!")
    game = Game("Online")
    await bot.change_presence(status=Status.online)
    await bot.change_presence(activity=game)
    print(scores2)
    print(f"{scores} Bot Started {scores}")
    print(scores2)
    print(f"Name: {bot.user.name}")
    print(f"Discriminator: {bot.user.discriminator}")
    print(f"Displayname: {bot.user.display_name}")
    print(f"Global Name: {bot.user.global_name}")
    try:
        print(f"Avatar URL: {bot.user.avatar.url}")
    except AttributeError:
        print("Avatar URL: None")
    

for filename in os.listdir("./commands"):
    if filename.endswith(".py"):
        file = filename[:-3]
        bot.load_extension(f"commands.{file}")
        print(f"{file} Loaded!")

if __name__ == "__main__":
    bot.run(bot_token)
 