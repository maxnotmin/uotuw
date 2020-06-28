import os, sys
from celery import Celery
from celery.schedules import crontab
import time
from dl import loop_pull_vid, move_videos
from media_sources import recent_video_shows, recent_podcasts
from random import randint
import logging
import datetime
from datetime import timedelta


# DIGITAL OCEAN : https://www.digitalocean.com/community/tutorials/how-to-use-celery-with-rabbitmq-to-queue-tasks-on-an-ubuntu-vps

# RUN with Supervior
# Get PID: ps -ef | grep supervisord
# Kill: kill -s SIGTERM <PID>


# USING python SuperVisor: https://medium.com/@MicroPyramid/celery-with-supervisor-12522ec397ed


AB_PATH = os.path.abspath(__file__)
CUR_DIR = os.getcwd()

# HOW TO RUN THESE TASKS
# celery worker --loglevel=info -A the_schedule --beat

#backend can be DataBase Connetion
app = Celery('tasks', backend='amqp', broker='amqp://localhost//')

# Another way to kickoff tasks
"""
app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-monday-morning': {
        'task': 'tasks.add',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
        'args': (16, 16),
    },
}
"""




@app.task
def test(string):
    return string[::-1]

@app.task
def delete_videos():
    pass

@app.task
def gather_vid_urls():
    pass

@app.task
def download_videos():
    pass

@app.task
def check_stream():
    pass

@app.task
def run_stream():
    # FileGlobLivestream opt/videos dlive -glob "*.mkv" -shuffle -loop
    pass

@app.task
def print_loc():
    mr_ab = str(AB_PATH)
    mr_cur = str(CUR_DIR)
    fin_str = "AB: {the_ab} | CUR: {the_cur}".format(the_ab=mr_ab, the_cur=mr)
    return fin_str

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

@app.task
def make_dir():
    num_name = random_with_N_digits(n=4)
    stream = os.popen('touch {file}.txt'.format(file=num_name))



CELERYBEAT_SCHEDULE = {
    'GET_PATHS': {
        'task': 'tasks.print_loc',
        'schedule': timedelta(seconds=10),
    },
}




"""
@app.on_after_configure.connect
def all_tasks(sender, **kwargs):
    print("STARTING CONFING IT's READING")
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(5.0, print_loc.s, name='PRINT RUN LOC')
    sender.add_periodic_task(10, test('hello').s, name='test hello')
    logging.info(msg="CUR DIR: {}".format(CUR_DIR))
    logging.info(msg="AB DIR: {}".format(AB_PATH))


    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )
"""
