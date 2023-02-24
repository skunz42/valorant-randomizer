'''
'''

from cmds.msgs.msgs import (get_commands, get_usage, get_help_ow_agents, get_help_players,
                            get_help_get_players)
from cmds.utils.utils import send_message
from config.cmds_cfg import (SET_PLAYERS_COMMAND, OVERWATCH_AGENTS_COMMAND, GET_PLAYERS_COMMAND)

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

async def handle_help_cmds(message, cmd):
    '''
    '''
    if cmd.lower() == OVERWATCH_AGENTS_COMMAND:
        resp = get_help_ow_agents()
    elif cmd.lower() == SET_PLAYERS_COMMAND:
        resp = get_help_players()
    elif cmd.lower() == GET_PLAYERS_COMMAND:
        resp = get_help_get_players()
    else:
        resp = get_usage()
    await send_message(message, resp)
