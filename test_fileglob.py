import os, sys

def stream_it():
    try:
        stream = os.popen('sh stream_vids.sh')
        print("STREAMING :")
        return True
    except Exception as e:
        print("FileGlob ERROR: ", str(e))


stream_it()