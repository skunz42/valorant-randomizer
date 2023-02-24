'''
'''

FILENAME = "config/players.tmp"

def write_players(players):
    '''
    '''
    with open(FILENAME, 'w', encoding='utf-8') as file:
        file.write(players)

def read_players():
    '''
    '''
    read_data = ""
    with open(FILENAME, 'r', encoding='utf-8') as file:
        read_data = file.read()
    return "Players:\n" + read_data

async def send_message(message, msg_str):
    '''
    '''
    print(f"Sending: {msg_str}")
    await message.channel.send(msg_str)
