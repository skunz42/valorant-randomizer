import shlex

BASE_COMMAND = "!sb"
PLAYERS_COMMAND = "players"
HELP_COMMAND = "help"
OVERWATCH_AGENTS_COMMAND = "ow-agents"

#def handle_players_cmd(message, msg_parts):
#    print("players")
#    print(msg_parts)
#    return
#
#def handle_ow_agents_cmd(message, msg_parts):
#    print("overwatch")
#    return
#
#def handle_help_cmd(message, msg_parts):
#    return

async def send_message(message, msg_str):
    print(f"Sending: {msg_str}")
    await message.channel.send(msg_str)

async def handle_unrecognized_cmd(message, msg_parts):
    resp = get_usage()
    await send_message(message, resp)
    return

def get_usage():
    resp = ("Usage: `!sb [command-name]`\n"
            "Run `!sb help` for a list of commands")
    return resp

async def handle_command(message):
    content = message.content
    msg_parts = shlex.split(content)
    print(f"MSG_PARTS: {msg_parts}")

    if len(msg_parts) == 1:
        await handle_unrecognized_cmd(message, msg_parts[1:])
    else:
        spec_cmd = msg_parts[1]
#        if spec_cmd == PLAYERS_COMMAND:
#            handle_players_cmd(message, msg_parts[1:])
#        elif spec_cmd == HELP_COMMAND:
#            handle_help_cmd(message, msg_parts[1:])
#        elif spec_cmd == OVERWATCH_AGENTS_COMMAND:
#            handle_ow_agents_cmd(message, msg_parts[1:])
#        else:
#            handle_unrecognized_cmd(message, msg_parts[1:])
