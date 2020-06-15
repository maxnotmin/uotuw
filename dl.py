#!/usr/bin/python3.6
import os, sys, time, datetime, subprocess
import shutil


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
    """
    """


    for vid in thelist:
        try:
            #python /usr/local/bin/youtube-dl
            stream = os.popen('python /usr/local/bin/youtube-dl {url}'.format(url=vid))
            output = stream.read()
        except Exception as e:
            print("Could not download video: ", str(e))


def move_videos():
    target_dir = '/opt/videos'
    cur_dir = CUR_DIR
    all_files = os.listdir(cur_dir)
    print("ALL FILES: ", all_files)
    #MOVE FILE LOOP
    try:
        for file in all_files:
            if file.endswith('.mkv') or file.endswith('.mp4'):
                tmp_path = os.path.join(test_target, file)
                print("FOUND FILE", tmp_path)
                shutil.move(file, tmp_path)
        return True
    except Exception as e:
        print("Video File Move Error: ", str(e))





move_videos()

#loop_pull_vid(thelist=recent_shows)

