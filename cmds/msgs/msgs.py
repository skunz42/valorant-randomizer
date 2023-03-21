'''
'''

from config.cmds_cfg import (SET_PLAYERS_COMMAND, HELP_COMMAND, OVERWATCH_AGENTS_COMMAND, GET_PLAYERS_COMMAND)

def get_usage():
    '''
    '''
    resp = ("Usage: `!sb [command-name]`\n"
            f"Run `!sb {HELP_COMMAND}` for a list of commands\n"
            f"Run `!sb {HELP_COMMAND} [command]` for help with a specific command")
    return resp

def get_commands():
    '''
    '''
    resp = (f"`{OVERWATCH_AGENTS_COMMAND}` - fetches random overwatch "
            "agents for the selected players.\n"
            f"`{SET_PLAYERS_COMMAND}` - sets players for the current session\n"
            f"`{GET_PLAYERS_COMMAND}` - gets the current players")
    return resp

def get_help_ow_agents():
    '''
    '''
    resp = (f"`!sb {OVERWATCH_AGENTS_COMMAND}`\n"
            "Returns random Overwatch agents for the current players\n"
            "args - open/role")
    return resp

def get_help_players():
    '''
    '''
    resp = (f"`!sb {SET_PLAYERS_COMMAND}`\n"
            "Sets the current players\n"
            "args - list of names\n"
            "Ex. `!sb set-players Alice Bob \"Billy Jean\"`")
    return resp

def get_help_get_players():
    '''
    '''
    resp = (f"`!sb {GET_PLAYERS_COMMAND}`\n"
            "Gets the current players\n"
            "args - None")
    return resp

def get_players(players):
    '''
    '''
    resp = "Players:\n" + players
    return resp
