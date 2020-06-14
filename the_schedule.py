import os, sys
import schedule
from celery import Celery
from celery.schedules import crontab
import time


# DIGITAL OCEAN : https://www.digitalocean.com/community/tutorials/how-to-use-celery-with-rabbitmq-to-queue-tasks-on-an-ubuntu-vps
#backend can be DataBase Connetion
app = Celery('tasks', backend='amqp', broker='amqp://localhost//')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )

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
    pass


