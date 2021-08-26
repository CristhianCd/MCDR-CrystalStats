# Plugin author : CristhianCd
# Plugin Version : 1.0
# Created for Crystal Smp 
# Crystal discord :b | https://discord.gg/5DRahHRzWP


PLUGIN_METADATA = {
    'id': 'crystal_scoreboards',
    'version': '1.0',
    'name': 'Crystal Scoreboards',
    'description': 'Plugin for show scoreboards',
    'author': 'CristhianCd',
    'link': 'https://github.com/CristhianCd/MCDR-CrystalScoreboards'
}


def help(server):
    server.say('''
§5§l-----| Crystal Scoreboard Plugin v1.0 |-----
    
 §d!!s: §7Show help message
 §d!!s hide: §7Hide scoreboard
 §d!!s show: §7Show scoreboard
 §d!!s §5<class> <target>: §7Create scoreboard and display
 §d<class> : §7used, mined, broken, crafted, dropped, custom
 ''')
    
def hideScoreboard(server):
    server.execute("scoreboard objectives setdisplay sidebar")


def removeScoreboard(server):
    server.execute("scoreboard objectives remove CrystalStats")

def displayScoreboard(server):
    server.execute("scoreboard objectives setdisplay sidebar CrystalStats")
    
def createScoreboard(statclass, target, server):
    if statclass == "used":
        a = "useItem"
    elif statclass == "mined":
        a = "mineBlock"
    elif statclass == "broken":
        a = "breakItem"
    elif statclass == "killed":
        a = "killEntity"
        server.execute(f"scoreboard objectives add CrystalStats stat.{a}.{target} §5{statclass}.§d{target}")
    elif statclass == "crafted":
        a = "craftItem"
    elif statclass == "dropped":
        a = "drop"
    elif statclass == "custom":
        server.execute(f"scoreboard objectives add CrystalStats stat.{target} §d{target}")
        displayScoreboard(server)
        
    server.execute(f"scoreboard objectives add CrystalStats stat.{a}.minecraft.{target} §5{statclass}.§d{target}")


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
        elif cl == 3:
            statclass = c[1]
            target = c[2]          
            removeScoreboard(server)
            createScoreboard(statclass, target, server)
            displayScoreboard(server)
        else: 
            server.say('Error, use !!s for show plugin help')
            
            
def on_load(server, old):
    server.register_help_message('!!s', 'Crystal scoreboards tool')

