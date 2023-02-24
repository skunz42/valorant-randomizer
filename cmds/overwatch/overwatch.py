'''
'''

from cmds.utils.utils import send_message
from cmds.help.help_cmds import handle_help_cmds

async def handle_ow_agents_cmd(message, msg_parts):
    '''
    '''
    if len(msg_parts) == 1:
        await handle_help_cmds(message, msg_parts[0])
    else:
        await send_message(message, "poop")
    return
