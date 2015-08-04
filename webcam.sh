#!/bin/sh
PORT="8080"
SIZE="320x240"
FRAMERATE="10"

export LD_LIBRARY_PATH=/usr/local/lib
mjpg_streamer \
-i "input_uvc.so -f $FRAMERATE -r $SIZE -d /dev/video0 -y" \
-o "output_http.so -w /usr/local/www -p $PORT"
