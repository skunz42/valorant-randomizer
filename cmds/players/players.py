'''
'''

from cmds.msgs.msgs import get_players
from cmds.utils.utils import send_message, write_players, read_players
from cmds.help.help_cmds import handle_help_cmds
from config.cmds_cfg import PLAYERS_CFG_PATH

async def handle_set_players_cmd(message, msg_parts):
    '''
    '''
    if len(msg_parts) == 1:
        await handle_help_cmds(message, msg_parts[0])
    else:
        players = "\n".join(msg_parts[1:])
        write_players(players, PLAYERS_CFG_PATH)
        resp = get_players(players)
        await send_message(message, resp)

async def handle_get_players_cmd(message):
    '''
    '''
    resp = read_players(PLAYERS_CFG_PATH)
    await send_message(message, resp)
