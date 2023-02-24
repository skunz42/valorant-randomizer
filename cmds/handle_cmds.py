'''
'''
import shlex

from cmds.help.help_cmds import (handle_help_cmds, handle_unrecognized_cmd, handle_help_cmd)
from cmds.players.players import (handle_set_players_cmd, handle_get_players_cmd)
from cmds.overwatch.overwatch import handle_ow_agents_cmd
from config.cmds_cfg import (SET_PLAYERS_COMMAND, HELP_COMMAND, OVERWATCH_AGENTS_COMMAND, GET_PLAYERS_COMMAND)

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
        elif spec_cmd.lower() == SET_PLAYERS_COMMAND.lower(): # set-players
            await handle_set_players_cmd(message, msg_parts[1:])
        elif spec_cmd.lower() == GET_PLAYERS_COMMAND.lower(): # get-players
            await handle_get_players_cmd(message)
        elif spec_cmd.lower() == OVERWATCH_AGENTS_COMMAND.lower():
            await handle_ow_agents_cmd(message, msg_parts[1:])
        else: # unrecognized
            await handle_unrecognized_cmd(message)
