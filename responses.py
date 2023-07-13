import random
from database_handler import *
from sheets import *
import discord
import os
from discord.ext import commands
import requests
import json
import interactions



if not os.path.isfile(f"{os.path.realpath(os.path.dirname(__file__))}/config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open(f"{os.path.realpath(os.path.dirname(__file__))}/config.json") as file:
        config = json.load(file)


url = "https://discord.com/api/v10/applications/1109885462803398666/guilds/" + str(config["guildID"]) + "/commands"

# This is an example CHAT_INPUT or Slash Command, with a type of 1
json = {
    "name": "STATS",
    "type": 1,
    "description": "Get economy stats",
    "options": [
        {
            "name": "player",
            "description": "The player, if you want your stats then leave blank",
            "type": 6,
            "required": False
        }
            ]
        },

# For authorization, you can use either your bot token
headers = {
    "Authorization": "Bot" + config["token"]
}

r = requests.post(url, headers=headers, json=json)

@bot.command(
    name="my_first_command",
    description="This is the first command I made!",
    scope=config["guildID"],
)
async def my_first_command(ctx: interactions.CommandContext):
    await ctx.send("Hi there!")

if __name__ == "__main__":
    main()

"""
def handle_response(message) -> str:
    if message == '/HELP':
        return "LMFAO"

    if message == 'roll':
        return str(random.randint(1, 6))

    if message == '!help':
        return "`This is a help message that you can modify.`"

    #  return 'Yeah, I don\'t know. Try typing "!help".'
"""
