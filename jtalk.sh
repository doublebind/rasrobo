#!/bin/sh
tmpfile=/tmp/jtalk.wav
htsvoice="/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice"
#htsvoice="/usr/share/hts-voice/mei/mei_happy.htsvoice"
echo "$1" | open_jtalk \
-x /var/lib/mecab/dic/open-jtalk/naist-jdic \
-m $htsvoice \
-ow $tmpfile && \
aplay --quiet $tmpfile
rm $tmpfile
