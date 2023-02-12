import os
import sys
import discord
from dotenv import load_dotenv
from cmds.handle_cmds import handle_command

NUM_CMD_ARGS = 1
players = []
BASE_COMMAND = "!sb"

if len(sys.argv) != NUM_CMD_ARGS+1:
    print("Please enter in the form: python bot.py <Server Name>")
    sys.exit(1)

load_dotenv()
TOKEN = os.getenv('DISC_VAL_TOKEN')
SERVER = sys.argv[1]

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == SERVER:
            print(f"{client.user} has connected to Discord!")
            print(f"Chilling on {client.guilds[0]}")
            return

    print(f"Couldn't find the server {SERVER} in the bot's server list.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(message.content)

    if message.content.startswith(BASE_COMMAND):
        handle_command(message.content)
    elif message.content.lower() == "hewwo":
        await message.channel.send("uwu :3")

if __name__ == "__main__":
    client.run(TOKEN)