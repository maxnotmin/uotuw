import os, sys
import schedule
from celery import Celery
from celery.schedules import crontab
import time
from .dl import loop_pull_vid, move_videos
from .media_sources import recent_video_shows, recent_podcasts



# DIGITAL OCEAN : https://www.digitalocean.com/community/tutorials/how-to-use-celery-with-rabbitmq-to-queue-tasks-on-an-ubuntu-vps

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


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    print("STARTING CONFING IT's READING")
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )


