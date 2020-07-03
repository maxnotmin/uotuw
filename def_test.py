import os, sys
import time
from dl import loop_pull_vid, move_videos, delete_played_videos, stream_it
from media_sources import recent_video_shows, recent_podcasts
from read_feed import load_feed, get_vid_url, REGEX_PATTERN, BROKENSIM, loop_feed, make_dl_list


if __name__ == "__main__":
    # GET ALL INFO FROM BROKEN RSS

    # Load RSS
    bsfeed = load_feed(the_feed=BROKENSIM)

    list_of_posts = loop_feed(theobj=bsfeed)

    # CREATE FINAL LIST OF URLS TO DOWNLOAD
    fin_dl_list = make_dl_list(list_obj=list_of_posts)

    # DOWNLOAD NEW VIDEOS
    dl_vids = loop_pull_vid(thelist=fin_dl_list)

    # CLEAN OUT OLD VIDS
    delete_played_videos(target_dir='videos')

    # MOVE NEWS VIDEOS
    move_videos(target_dir='videos')

    # END
    print("stream it")

    stream_it()

