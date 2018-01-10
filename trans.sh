#!/bin/sh

for line in `cat /data5/yhqiu/yhqiu_data3/wav_langID/chi1/wav`;
do
    subdir=`echo $line | awk -F '/' '{print $6}'`
    if [ ! -d tmp/$subdir ];then
        mkdir -p tmp/$subdir
    fi
    ./voice_transformto16 $line tmp/$subdir/${line##*/} ; 
done
