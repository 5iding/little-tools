##check the utt's sampling rate



dura_samp=16000
for i in `find ./mobilPhone_data/en_3s -name '*.wav'`;do
#   echo $i
#   echo ${i##*/} 
    duration=`soxi $i | awk '{print $4}' | sed -n '4p'  `
    if [ $duration -ge  $dura_samp ];then
        echo $duration
        echo $i
    fi
done
