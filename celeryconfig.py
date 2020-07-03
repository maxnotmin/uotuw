CELERY_IMPORTS = ('tasks')
CELERY_IGNORE_RESULT = False
BROKER_HOST = "127.0.0.1" #IP address of the server running RabbitMQ and Celery
BROKER_PORT = 5672
BROKER_URL = 'amqp://'

from datetime import timedelta


# RUN: celery worker -l info --beat --detach
#Kill Process:>
#>  ps aux|grep 'celery woker'
#> sudo kill -9 <process id>

CELERYBEAT_SCHEDULE = {
    'test detacted': {
        'task': 'tasks.make_dir',
        'schedule': timedelta(seconds=10),
    },
}