'''
'''
import shlex

from cmds.msgs.msgs import (get_usage, get_commands, get_help_ow_agents,
                            get_help_players, get_help_get_players, get_players)
from config.cmds_cfg import (PLAYERS_COMMAND, HELP_COMMAND, OVERWATCH_AGENTS_COMMAND,
                             GET_PLAYERS_COMMAND)
from config.write_players import write_players, read_players

async def send_message(message, msg_str):
    print(f"Sending: {msg_str}")
    await message.channel.send(msg_str)

async def handle_unrecognized_cmd(message):
    '''
    '''
    resp = get_usage()
    await send_message(message, resp)

async def handle_help_cmd(message):
    '''
    '''
    resp = get_commands()
    await send_message(message, resp)

async def handle_player_cmd(message, msg_parts):
    '''
    '''
    if len(msg_parts) == 1:
        await handle_help_cmds(message, msg_parts[0])
    else:
        players = "\n".join(msg_parts[1:])
        write_players(players)
        resp = get_players(players)
        await send_message(message, resp)

async def handle_get_players_cmd(message):
    '''
    '''
    resp = read_players()
    await send_message(message, resp)

async def handle_help_cmds(message, cmd):
    '''
    '''
    if cmd.lower() == OVERWATCH_AGENTS_COMMAND:
        resp = get_help_ow_agents()
    elif cmd.lower() == PLAYERS_COMMAND:
        resp = get_help_players()
    elif cmd.lower() == GET_PLAYERS_COMMAND:
        resp = get_help_get_players()
    else:
        resp = get_usage()
    await send_message(message, resp)

async def handle_command(message):
    '''
    '''
    content = message.content
    msg_parts = shlex.split(content)
    print(f"MSG_PARTS: {msg_parts}")

    # just bot prompt
    if len(msg_parts) == 1:
        await handle_unrecognized_cmd(message)
    else:
        # specific command
        spec_cmd = msg_parts[1]
        if spec_cmd.lower() == HELP_COMMAND.lower(): # help
            if len(msg_parts) == 2:
                await handle_help_cmd(message)
            else: # help + other command
                await handle_help_cmds(message, msg_parts[2])
        elif spec_cmd.lower() == PLAYERS_COMMAND.lower(): # set-players
            await handle_player_cmd(message, msg_parts[1:])
        elif spec_cmd.lower() == GET_PLAYERS_COMMAND.lower(): # get-players
            await handle_get_players_cmd(message)
        else: # unrecognized
            await handle_unrecognized_cmd(message)
