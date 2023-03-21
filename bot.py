'''
'''
import os
import sys
import logging
import discord
from dotenv import load_dotenv

from config.cmds_cfg import BASE_COMMAND
from cmds.handle_cmds import handle_command

NUM_CMD_ARGS = 1
players = []
LOG_NAME = "strat-bot.log"

if len(sys.argv) != NUM_CMD_ARGS+1:
    print("Please enter in the form: python bot.py <Server Name>")
    sys.exit(1)

# Logging setup
logging.basicConfig(filename=LOG_NAME, filemode='w',
                    format='%(levelname)s: %(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter("%(name)s: %(message)s")
console.setFormatter(formatter)
logging.getLogger().addHandler(console)

logging.info("Loading config data")
load_dotenv()
TOKEN = os.getenv('DISC_VAL_TOKEN')
SERVER = sys.argv[1]

logging.info("Starting Discord Client")
client = discord.Client()

@client.event
async def on_ready():
    '''
    '''
    for guild in client.guilds:
        if guild.name == SERVER:
            logging.info("%s has connected to Discord!", client.user)
            logging.info("Listening on %s", SERVER)
            return

    logging.error("Couldn't find the server %s in the bot's server list.", SERVER)

@client.event
async def on_message(message):
    '''
    '''
    if message.author == client.user:
        return

    logging.info("Message Content: %s", message.content)

    if (len(message.content) >= len(BASE_COMMAND) and
        message.content[:len(BASE_COMMAND)].lower() == BASE_COMMAND):
        await handle_command(message)
    elif message.content.lower() == "hewwo":
        await message.channel.send("uwu :3")

if __name__ == "__main__":
    client.run(TOKEN)
