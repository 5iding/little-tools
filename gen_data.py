import os
import sys
from os.path import join
import os.path

def listFiles(dirpath,suffix): 
        listlines=[]
        files = os.listdir(dirpath)
        for eachfile in files:
                curfile = dirpath + os.sep + eachfile  #os.sep  
                if os.path.isdir(curfile):             #os.path.isdir 
                        for mid in listFiles(curfile,suffix): 
                                listlines.append(mid)
                elif eachfile.endswith(suffix):  
                        listlines.append([dirpath,eachfile])                       
        return listlines

def gentemplist(list):
	list_f = []
        for each in list:
		#print utt
		#utt = each[0].split('/')[3]+'_'+each[1].split('.')[0]
		utt = each[1].split('.')[0]
                #utt = each[0].split('/')[6][5:]+'_'+each[1].split('.')[0]
                path = each[0]+'/'+each[1]
                spk = each[0].split('/')[-1]
                list_f.append([utt,spk,path])
                #print utt+' '+spk+' '+path
        return list_f




def genwavlist(list,filename):
	fout = open(filename,'w')
	for each in list:
		#fout.write(each[0]+' '+each[2]+'\n')
		fout.write(each[2]+'\n')

def genutt2spk(list,filename):
	fout = open(filename,'w')
	list.sort(key=lambda x:x[1])
	for each in list:
		fout.write(each[0]+' '+each[1]+'\n')
		#fout.write(each[1]+'\n')

def gentrials(list,filename):
	fout = open(filename,'w')
	for each in list:
		for eachj in ['cha','eng']:
			fout.write(eachj+' '+each[0])
			if(each[1]==eachj):
				fout.write(' target\n')
			else:
				fout.write(' nontarget\n')


basedir = '/data5/yhqiu/yhqiu_data3/wav_langID/eng_byme'
datalist = listFiles(basedir,'wav')
#print datalist
#trainlist = listFiles(basedir+'Dev','wav')
#testlist = listFiles(basedir+'Test','wav')

devlist_f = gentemplist(datalist)
print devlist_f
genwavlist(devlist_f,'/data5/yhqiu/yhqiu_data3/wav_langID/wav.scp')
genutt2spk(devlist_f,'/data5/yhqiu/yhqiu_data3/wav_langID/utt2spk')
#gentrials(testlist_f,'data/trials/lld_5.trials')


'''
trainlist_f = gentemplist(trainlist)
genwavlist(trainlist_f,'data/train/wav.scp')
genutt2spk(trainlist_f,'data/train/utt2spk')

testlist_f = gentemplist(testlist)
genwavlist(testlist_f,'data/test/wav.scp')
genutt2spk(testlist_f,'data/test/utt2spk')

gentrials(testlist_f,'data/trials/lld_5.trials')
'''
