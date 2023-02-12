import shlex

BASE_COMMAND = "!sb"
PLAYERS_COMMAND = "players"
OVERWATCH_AGENTS_COMMAND = "ow-agents"

def handle_players_cmd(msg_parts):
    print("players")
    return

def handle_ow_agents_cmd(msg_parts):
    print("overwatch")
    return

def handle_unrecognized_cmd(msg_parts):
    print("oopsie poopsie")
    return

def handle_command(content):
    msg_parts = shlex.split(content)
    print(msg_parts)

    if len(msg_parts) == 1:
        print_usage()
    else:
        spec_cmd = msg_parts[1]
        if spec_cmd == PLAYERS_COMMAND:
            handle_players_cmd(msg_parts[1:])
        elif spec_cmd == OVERWATCH_AGENTS_COMMAND:
            handle_ow_agents_cmd(msg_parts[1:])
        else:
            handle_unrecognized_cmd(msg_parts[1:])
