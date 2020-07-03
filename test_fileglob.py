import os, sys

def steam_it():
    stream = os.popen('FileGlobLivestream videos dlive -glob "*"')
    output = stream.read()
    return True


steam_it()