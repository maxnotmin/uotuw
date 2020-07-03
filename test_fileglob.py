import os, sys

def steam_it():
    stream = os.popen('FileGlobLivestream videos dlive -glob "*" -shuffle -loop')
    output = stream.read()
    return True