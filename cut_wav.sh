## cut utt to fixed lenght, if the length is not enough move it to tmp

## coding by qiuyh

##09/01/2018
date
file=./wav
dir=./test_3s_
dura=3
dura_samp=48000
for i in `cat $file`;do
    pice=`echo $i | cut -d '/' -f5- `
#    echo ${pice%/*}
    if [ ! -d $dir/${pice%/*} ];then
        mkdir -p $dir/${pice%/*}
    fi
#   echo ${i##*/} 
    sox $i $dir/$pice trim 0.1 $dura
    duration=`soxi $dir/$pice | awk '{print $5}' - | sed -n '6p' - `
    if [ $duration -ne $dura_samp ];then
        echo $i
        echo $duration
        mv $dir/$pice ./tmp_
    fi
done
date
