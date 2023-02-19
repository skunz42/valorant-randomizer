import shlex

BASE_COMMAND = "!sb"
PLAYERS_COMMAND = "players"
HELP_COMMAND = "help"
OVERWATCH_AGENTS_COMMAND = "ow-agents"

def get_usage():
    resp = ("Usage: `!sb [command-name]`\n"
            "Run `!sb help` for a list of commands\n"
            "Run `!sb help [command]` for help with a specific command")
    return resp

def get_commands():
    resp = ("`ow-agents` - fetches random overwatch agents for the "
            "selected players.\n"
            "`players` - sets players for the current session")
    return resp

def get_help_ow_agents():
    resp = ("`!sb ow-agents`\n"
            "Returns random Overwatch agents for the current players\n"
            "args - None")
    return resp

def get_help_players():
    resp = ("`!sb players`\n"
            "Sets the current players\n"
            "args - list of names\n"
            "Ex. `!sb players Alice Bob \"Billy Jean\"`")
    return resp

async def send_message(message, msg_str):
    print(f"Sending: {msg_str}")
    await message.channel.send(msg_str)

async def handle_unrecognized_cmd(message, msg_parts):
    resp = get_usage()
    await send_message(message, resp)
    return

async def handle_help_cmd(message):
    resp = get_commands()
    await send_message(message, resp)
    return

async def handle_help_cmds(message, cmd):
    if cmd.lower() == OVERWATCH_AGENTS_COMMAND:
        resp = get_help_ow_agents()
    elif cmd.lower() == PLAYERS_COMMAND:
        resp = get_help_players()
    else:
        resp = get_usage()
    
    await send_message(message, resp)

async def handle_command(message):
    content = message.content
    msg_parts = shlex.split(content)
    print(f"MSG_PARTS: {msg_parts}")

    if len(msg_parts) == 1:
        await handle_unrecognized_cmd(message, msg_parts[1:])
    else:
        spec_cmd = msg_parts[1]
        if spec_cmd.lower() == HELP_COMMAND.lower():
            if len(msg_parts) == 2:
                await handle_help_cmd(message)
            else:
                await handle_help_cmds(message, msg_parts[2])
        else:
            await handle_unrecognized_cmd(message, msg_parts[1:])
