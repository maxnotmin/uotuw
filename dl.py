#!/usr/bin/python3.6
import os, sys, time, datetime, subprocess


AB_PATH = os.path.abspath(__file__)
CUR_DIR = os.getcwd()
timestr = time.strftime("%Y%m%d-%H%M%S")
now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# GET ALL RECENT SHOWS


recent_shows = [
    'https://youtu.be/mTgQuGGTUXQ',
    'https://youtu.be/qZv5Mw6I6Wk',
    'https://youtu.be/lSdb_fOsi7U',
    'https://youtu.be/usIJ_5UEjqU',
    'https://youtu.be/XJBjrSQm_NI',
    ''
]

'''
def loop_pull_vid(thelist=[]):


    for vid in thelist:
        #python /usr/local/bin/youtube-dl
        process = subprocess.Popen(['python /usr/local/bin/youtube-dl', '{url}'.format(url=vid)],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        #print(stdout.decode('utf-8'))
'''

def loop_pull_vid(thelist=[]):


    for vid in thelist:
        #python /usr/local/bin/youtube-dl
        stream = os.popen('python /usr/local/bin/youtube-dl {url}'.format(url=vid))
        output = stream.read()




loop_pull_vid(thelist=recent_shows)

