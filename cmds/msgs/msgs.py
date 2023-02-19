from config.cmds_cfg import *

def get_usage():
    resp = ("Usage: `!sb [command-name]`\n"
            "Run `!sb help` for a list of commands\n"
            "Run `!sb help [command]` for help with a specific command")
    return resp

def get_commands():
    resp = ("`ow-agents` - fetches random overwatch agents for the "
            "selected players.\n"
            "`set-players` - sets players for the current session\n"
            "`get-players` - gets the current players")
    return resp

def get_help_ow_agents():
    resp = ("`!sb ow-agents`\n"
            "Returns random Overwatch agents for the current players\n"
            "args - None")
    return resp

def get_help_players():
    resp = ("`!sb set-players`\n"
            "Sets the current players\n"
            "args - list of names\n"
            "Ex. `!sb set-players Alice Bob \"Billy Jean\"`")
    return resp

def get_help_get_players():
    resp = ("`!sb get-players`\n"
            "Gets the current players\n"
            "args - None")
    return resp

def get_players(players):
    resp = "Players:\n" + players
    return resp
