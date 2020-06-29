from celery.task import task
from random import randint
import os

AB_PATH = os.path.abspath(__file__)
CUR_DIR = os.getcwd()

@task
def test(string):
    return string[::-1]

@task
def delete_videos():
    pass

@task
def gather_vid_urls():
    pass

@task
def download_videos():
    pass

@task
def check_stream():
    pass

@task
def run_stream():
    # FileGlobLivestream opt/videos dlive -glob "*.mkv" -shuffle -loop
    pass

@task
def print_loc():
    mr_ab = str(AB_PATH)
    mr_cur = str(CUR_DIR)
    fin_str = "AB: {the_ab} | CUR: {the_cur}".format(the_ab=mr_ab, the_cur=mr_cur)
    print("FIN PRINT: ", fin_str)
    return fin_str

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

@task
def make_dir():
    num_name = random_with_N_digits(n=4)
    stream = os.popen('touch {file}.txt'.format(file=num_name))
