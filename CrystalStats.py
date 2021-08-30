# Plugin author : CristhianCd
# Plugin Version : 1.1
# Created for Crystal Smp 
# Crystal discord :b | https://discord.gg/5DRahHRzWP

import os
import json


stats_path = "server/world/stats/"
usercache_path = "server/usercache.json"


PLUGIN_METADATA = {
    'id': 'crystal_stats',
    'version': '1.1',
    'name': 'Crystal Stats',
    'description': 'Plugin for show stats/scoreboards',
    'author': 'CristhianCd',
    'link': 'https://github.com/CristhianCd/MCDR-CrystalStats'
}


def help(server):
    server.say('''
§5§l-----| Crystal Stats Plugin v1.1 |-----

 §d!!s: §7Show help message
 §d!!s hide: §7Hide scoreboard
 §d!!s show: §7Show scoreboard
 §d!!s §5<class> <target>: §7Create and display scoreboard
 §d!!s rank §5<class> <target>: §7Show rank and total
 §d<class> : §7used, mined, broken, crafted, dropped, picked_up, custom

 §7§lPlugin by CristhianCd <3
 ''')
    
def hideScoreboard(server):
    server.execute("scoreboard objectives setdisplay sidebar")


def removeScoreboard(server):
    server.execute("scoreboard objectives remove CrystalStats")


def displayScoreboard(server):
    server.execute("scoreboard objectives setdisplay sidebar CrystalStats")
    

def statClass(statclass, target):
    global criteria
    if statclass == "used":
        st = "useItem"
        criteria = f"stat.{st}.minecraft.{target}" 
    elif statclass == "mined":
        st = "mineBlock"
        criteria = f"stat.{st}.minecraft.{target}" 
    elif statclass == "broken": 
        st = "breakItem"
        criteria = f"stat.{st}.minecraft.{target}" 
    elif statclass == "killed":
        st = "killEntity"
        criteria = f"stat.{st}.{target}" 
    elif statclass == "crafted":
        st = "craftItem"
        criteria = f"stat.{st}.minecraft.{target}" 
    elif statclass == "dropped":
        st = "drop"
        criteria = f"stat.{st}.minecraft.{target}" 
    elif statclass == "picked_up":
        st = "pickup"
        criteria = f"stat.{st}.minecraft.{target}" 
    elif statclass == "custom":
        criteria = f"stat.{target}" 


def createScoreboard(statclass, target, server):  
    server.execute(f"scoreboard objectives add CrystalStats {criteria} §5{statclass}.§d{target}")

    
# When I stopped being lazy I optimize the zzz code
def getRank(server):
    list = []
    le = []
    orden = []
    with os.scandir(stats_path) as uuids:
        for stats in uuids:
            name = stats.name
            with open(f"{stats_path}{name}") as f:
                jsons = json.load(f)
                if criteria in jsons:
                    l = (jsons[criteria])
                    le.append(name)
                    list.append(l)   
                else:
                    None
    server.say(f"§d{criteria} §5§lTotal : §7§l{sum(list)}\n")
    for (userjson, value) in zip(le, list):
        g = [userjson, value]
        orden.append(g) 
        orden.sort(key = lambda x: x[1], reverse=True)
    for rank, (n, v) in enumerate(orden, 1):
        na = n.replace('.json', '')
        with open(usercache_path) as uuidname:
            usercache = json.load(uuidname)
        users = [x for x in usercache if x["uuid"]==f"{na}"]
        for names in users:
            
            server.say(f'§5§l{rank}# §d§l{names["name"]:>18}             §7§l{v}')
    
            
def on_info(server, info):
    if info.is_player == 1 and info.content.startswith('!!s'):
        
        c = info.content.split()
        cl = len(c)

        if cl == 1:
            help(server)
        elif cl == 2:
            if c[1] == 'hide':
                hideScoreboard(server)  
            elif c[1] == 'show':
                displayScoreboard(server)
            elif c[1] == 'total':
                getRank(server)
            else:
                server.say('Error, use !!s for show plugin help')
        elif cl == 3:
            statclass = c[1]
            target = c[2]
            removeScoreboard(server)
            statClass(statclass, target)
            createScoreboard(statclass, target, server)
            displayScoreboard(server)
        elif cl == 4:
            if c[1] == 'rank':
                statclass = c[2]
                target = c[3] 
                statClass(statclass, target)
                getRank(server)
            else:
                server.say('Error!!')
        else: 
            server.say('Error, use !!s for show plugin help')


def on_player_joined(server, player: str, info):
    server.say(f'§dWelcome §7{player} §dto §7Crystal SMP')
    

def on_load(server, old):
    server.register_help_message('!!s', 'Crystal scoreboards tool')
