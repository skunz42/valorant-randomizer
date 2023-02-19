FILENAME = "config/players.tmp"

def write_players(players):
    with open(FILENAME, 'w') as f:
        f.write(players)

def read_players():
    read_data = ""
    with open(FILENAME, 'r') as f:
        read_data = f.read()
    return "Players:\n" + read_data
