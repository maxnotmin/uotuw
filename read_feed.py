import os, sys
import schedule
import feedparser
import time
import ssl
import re

AB_PATH = os.path.abspath(__file__)
CUR_DIR = os.getcwd()
BROKENSIM = 'https://brokensimulation.com/feed/'


def load_feed(the_feed=BROKENSIM):
    """
    This loads the most recent entries from the Target Feed. For Broken Sim, posts 1-12
    :param the_feed:
    :return: list[obj] | JSON
    """

    # Prevents SSL Error
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context
    broken = feedparser.parse(the_feed)
    ent = broken['entries']
    return ent

REGEX_PATTERN = r'(?<=src=")(.*)(?=\?feature)'


def get_vid_url(the_pattern='', the_str=''):
    """
    This finds the EMBEDED VIDEO URL in this Dict : get_text_value = test_feed['content'][0]['value']

    USE: get_vid_url(the_pattern=REGEX_PATTERN , the_str=load_feed['content'][0]['value'])

    :param the_pattern:
    :param the_str:
    :return: str
    """
    try:
        find_url = re.search(pattern=the_pattern, string=the_str)
        if find_url:
            #print("the VID URL: ", find_url.group())
            return find_url.group()
        else:
            print("No Embend Video URL")
            return ""
    except Exception as e:
        print("ERROR FINDING YOUTUBE  EMBED URL")


def loop_feed(theobj=[]):
    """
    Loop over the LOAD RSS Feed from BrokenSim. Should return like 12 posts
    :param theobj:
    :return: list[dict]
    """
    MASTER_LIST = []

    for show in theobj:
        tmp_obj = {
            'name': show['title'],
            'summary': show['summary'],
            'url': get_vid_url(the_pattern=REGEX_PATTERN, the_str=show['content'][0]['value'])
        }
        MASTER_LIST.append(tmp_obj)

    return MASTER_LIST


def make_dl_list(list_obj=[]):
    """
    This returns a list of URL from the RSS Feed
    :param list_obj: list[obj]
    :return: list
    """
    MASTER_LIST = []
    for obj in list_obj:
        tmp_url = obj['url']
        MASTER_LIST.append(tmp_url)
    return MASTER_LIST





