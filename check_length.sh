dura_samp=960000
for i in `find ./mobilPhone_data/en_3s -name '*.wav'`;do
#   echo $i
#   echo ${i##*/} 
    duration=`soxi $i | awk '{print $5}' | sed -n '6p'  `
    if [ $duration -ge  $dura_samp ];then
        echo $duration
        echo $i
    fi
done
