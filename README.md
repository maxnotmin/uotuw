# uotuw
Union of the Unwanted Scripts and Notes


## THE UNION OF THE UNWANTERS

#### Basic Sever Set up
This is will be Dockerized Later

##### STREAMING MEDIA SERVER ON UBUNTU
1. sudo add-apt-repository ppa:mc3man/trusty-media
2. sudo apt-get install ffmpeg
3. sudo apt install python3-pip
4. python3 -m pip install PyLivestream
5. mkdir videos
6. mkdir music
7. sudo apt-get install youtube-dl
8. alias python='python3.6'
9. python /usr/local/bin/youtube-dl
10. Download stuff
11. ffmpeg -i <filename.mp4> <filename.avi>
12: FileGlobLivestream ~/videos dlive -glob "*.mkv" -loop


==== INSTALL SCHEDULER : PYTHON CELERY ===
1. sudo apt-get install install rabbitmq-server