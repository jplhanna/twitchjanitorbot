#cfg.py
HOST = "irc.twitch.tv"              # the Twitch IRC server
PORT = 6667                         # always use port 6667!
NICK = "JanitorBot"            # your Twitch username, lowercase
PASS = "oauth:xxxxxxxxxxxxxxxxxxxx" # your Twitch OAuth token
CHAN = "#chosengamer"                   # the channel you want to join
RATE = (20/30)                      #messages per 30 second
PATT = [] #input bannable messaage patterns here