'''
'''

import random
from cmds.utils.utils import send_message, read_json_file, read_players_list
from cmds.help.help_cmds import handle_help_cmds
from config.cmds_cfg import OW_JSON_PATH, PLAYERS_CFG_PATH

async def generate_ow_open_queue(message, json_dict, players):
    '''
    '''
    agent_set = set()
    for agent in json_dict["agents"]:
        agent_set.add(agent['name'])

    player_set = set()
    for player in players:
        player_set.add(player)

    message_str = ""
    while len(player_set) > 0:
        player = random.sample(player_set, 1)[0]
        player_set.remove(player)

        agent = random.sample(agent_set, 1)[0]
        agent_set.remove(agent)

        pa_str = f"{player}: {agent}"
        print(pa_str)
        message_str += pa_str
        message_str += "\n"

    await send_message(message, message_str)

async def generate_ow_role_queue(message, json_dict, players):
    '''
    '''
    for agent in json_dict["agents"]:
        print(agent['role'])

    for player in players:
        print(player)

    await send_message(message, "role")

async def handle_ow_agents_cmd(message, msg_parts):
    '''
    '''
    if len(msg_parts) <= 1:
        await handle_help_cmds(message, msg_parts[0])
    else:
        json_dict = read_json_file(OW_JSON_PATH)
        players = read_players_list(PLAYERS_CFG_PATH)
        if msg_parts[1].lower() == "open":
            await generate_ow_open_queue(message, json_dict, players)
        elif msg_parts[1].lower() == "role":
            await generate_ow_role_queue(message, json_dict, players)
        else:
            await handle_help_cmds(message, msg_parts[0])
    return
