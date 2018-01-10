## the code use to cut utterance to fixed length one by one from long utt

## the utt must be 16k 16bit wav

## write by qiuyh 

## 08/01/2018


dura=10  #length of you want
file=./1320-WinPhone.wav #the utterance
duration_all=`soxi ${file} | awk '{print $5}' - | sed -n '6p' - `  
tim=$[${duration_all}/160000]
#echo $tim
for (( i=0; i<=${tim}; i++));do
 
    echo $[($i)*($dura)]
    sox $file ${i}.wav trim $[($i)*($dura)] $dura
    
done

