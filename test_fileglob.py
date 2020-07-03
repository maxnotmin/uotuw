import os, sys

def steam_it():
    stream = os.popen('sh stream_vis.sh')
    output = stream.read()
    return True


steam_it()