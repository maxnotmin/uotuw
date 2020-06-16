#!/usr/bin/python3.6
import os, sys, time, datetime, subprocess
import shutil


AB_PATH = os.path.abspath(__file__)
CUR_DIR = os.getcwd()
timestr = time.strftime("%Y%m%d-%H%M%S")
now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# GET ALL RECENT SHOWS

'''
def loop_pull_vid(thelist=[]):


    for vid in thelist:
        #python /usr/local/bin/youtube-dl
        process = subprocess.Popen(['python /usr/local/bin/youtube-dl', '{url}'.format(url=vid)],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        #print(stdout.decode('utf-8'))
'''


recent_shows = [
    'https://youtu.be/y2QQ2NoDEBI',
    'https://youtu.be/l7gmFKstPzs',
    'https://youtu.be/IRYOSVEbOq8',
    'https://youtu.be/T0-WyO0PCII',
    'https://youtu.be/GcZQ2aOjYRs',
    'https://youtu.be/VGV4gTyJodM',
    'https://youtu.be/fk9nH1LQlFc'

]



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
                tmp_path = os.path.join(target_dir, file)
                print("FOUND FILE", tmp_path)
                shutil.move(file, tmp_path)
        return True
    except Exception as e:
        print("Video File Move Error: ", str(e))


def delete_played_videos():
    target_dir = '/opt/videos'
    try:
        stream = os.popen('rm -r opt/videos/')
        output = stream.read()
    except Exception as e:
        print("Could not Delete All Videos: ", str(e))




loop_pull_vid(thelist=recent_shows)

#move_videos()

