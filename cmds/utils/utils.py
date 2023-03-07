'''
'''

import json

def write_players(players, path):
    '''
    '''
    with open(path, 'w', encoding='utf-8') as file:
        file.write(players)

def read_players(path):
    '''
    '''
    read_data = ""
    with open(path, 'r', encoding='utf-8') as file:
        read_data = file.read()
    return "Players:\n" + read_data

def read_players_list(path):
    '''
    '''
    with open(path, 'r', encoding='utf-8') as file:
        lines = [line.rstrip() for line in file]
    return lines

def read_json_file(path):
    '''
    '''

    json_dict = {}
    with open(path, encoding='utf-8') as json_file:
        json_dict = json.load(json_file)

    return json_dict

async def send_message(message, msg_str):
    '''
    '''
    print(f"Sending: {msg_str}")
    await message.channel.send(msg_str)
