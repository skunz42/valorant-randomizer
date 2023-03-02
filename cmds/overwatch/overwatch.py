'''
'''

from cmds.utils.utils import send_message, read_json_file
from cmds.help.help_cmds import handle_help_cmds
from config.cmds_cfg import OW_JSON_PATH

async def generate_ow_open_queue(message, json_dict):
    '''
    '''
    for agent in json_dict["agents"]:
        print(agent['name'])
    await send_message(message, "open")

async def generate_ow_role_queue(message, json_dict):
    '''
    '''
    for agent in json_dict["agents"]:
        print(agent['role'])
    await send_message(message, "role")

async def handle_ow_agents_cmd(message, msg_parts):
    '''
    '''
    if len(msg_parts) <= 1:
        await handle_help_cmds(message, msg_parts[0])
    else:
        json_dict = read_json_file(OW_JSON_PATH)
        if msg_parts[1].lower() == "open":
            await generate_ow_open_queue(message, json_dict)
        elif msg_parts[1].lower() == "role":
            await generate_ow_role_queue(message, json_dict)
        else:
            await handle_help_cmds(message, msg_parts[0])
    return
