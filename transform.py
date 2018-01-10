
fout = open('/data5/yhqiu/yhqiu_data3/wav_langID/chi1/wav','r').readlines()
#line=fout.readlines()
for each in fout:
    print each
    ./voice_transformto16 each 
