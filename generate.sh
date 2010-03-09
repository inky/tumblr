#!/bin/bash
set -e

EXTERNAL=/Volumes/Cerberus
LOGS="$EXTERNAL/data/log/irssi/freenode/#tumblrs/"
CACHE="$EXTERNAL/cache/pisg"
PISG="$HOME/local/src/pisg/0.72/pisg"
OPTS="-co $PWD/tumblrs.cfg -ch '#tumblrs' -f irssi --cfg CacheDir=$CACHE --dir $LOGS"
RSYNCOPTS="-az"
y=$(date +%Y); m=$(date +%m); d=$(date +%d)

[ -z $EXTERNAL/data ] && exit
if [ "$1" = "--cron" ]; then
    OPTS="$OPTS -s"
    RSYNCOPTS="$RSYNCOPTS -q"
else
    RSYNCOPTS="$RSYNCOPTS -v --progress"
fi

rm -rf output
mkdir -p $CACHE output/$y/$m
chmod -R 755 output

if [ $(date +%u) = 2 ]; then
    $PISG $OPTS -nf -1 -o output/alltime.html
fi
$PISG $OPTS -o output/index.html

f="output/$y/$m/$d.html"
cp output/index.html $f
chmod 644 output/*.html $f

if [ "$1" = "-u" ] || [ "$1" = "--cron" ]; then
    rsync $RSYNCOPTS output/ boxofjunk:domains/tumblr.boxofjunk.ws/html/irc/
fi
