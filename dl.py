#!/usr/bin/python3.6
import os, sys, time, datetime, subprocess
import shutil
import yaml


AB_PATH = os.path.abspath(__file__)
CUR_DIR = os.getcwd()
timestr = time.strftime("%Y%m%d-%H%M%S")
now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def load_yaml_list(target_yaml='vid_config.yaml', the_key='vid_list'):
    """
    This will loaded the URLs form a YAML to get all the most recent shows
    :param target_yaml:
    :return: List
    """
    try:
        with open(target_yaml) as stream:
            the_yaml = yaml.safe_load(stream)
            print("try Load Yaml: ", the_yaml[the_key])
            the_list = the_yaml[the_key]
            if type(the_list) is list:
                return the_list
            else:
                print("List not loaded. Returning empty list")
                return ['']
    except yaml.YAMLError as e:
        print("ERROR Loading Yaml: ", str(e))
        return False



def loop_pull_vid(thelist=[]):
    """
    Loop through a list and download the YouTube Video

    :return boolean
    """
    for vid in thelist:
        #python /usr/local/bin/youtube-dl
        stream = os.popen('python /usr/local/bin/youtube-dl {url}'.format(url=vid))
        print("Downlaoded: ", str(vid))
        output = stream.read()



def move_videos(target_dir='videos'):
    """
    Move the downloaded videos to target folder
    :return: boolean
    """
    cur_dir = CUR_DIR
    all_files = os.listdir(cur_dir)
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
        return False


def delete_played_videos(target_dir='videos'):
    """
    Remove all downloaded videos from target directory
    :return: boolean
    """

    try:
        for file in os.listdir(target_dir):
            if file.endswith('.mkv') or file.endswith('.mp4'):
                stream = os.popen('rm {vid_file}'.format(vid_file=file))
                output = stream.read()
        return True
    except Exception as e:
        print("Could not Delete All Videos: ", str(e))
        return False





