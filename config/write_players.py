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
