'''
'''

import json
import logging

log = logging.getLogger(__name__)

def write_players(players, path):
    '''
    '''
    with open(path, 'w', encoding='utf-8') as file:
        log.info("Writing to file: %s", path)
        file.write(players)
        log.info("Wrote: %s", players)

def read_players(path):
    '''
    '''
    read_data = ""
    with open(path, 'r', encoding='utf-8') as file:
        log.info("Reading from file: %s", path)
        read_data = file.read()
        log.info("Read: %s", read_data)
    return "Players:\n" + read_data

def read_players_list(path):
    '''
    '''
    with open(path, 'r', encoding='utf-8') as file:
        log.info("Reading from file: %s", path)
        lines = [line.rstrip() for line in file]
        log.info("Read: %s", lines)
    return lines

def read_json_file(path):
    '''
    '''
    json_dict = {}
    with open(path, encoding='utf-8') as json_file:
        log.info("Reading from file: %s", path)
        json_dict = json.load(json_file)

    return json_dict

async def send_message(message, msg_str):
    '''
    '''
    log.info("Sending: %s", msg_str)
    await message.channel.send(msg_str)
