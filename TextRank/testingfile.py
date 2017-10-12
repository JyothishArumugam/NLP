# -*- coding: utf-8 -*-

"""
Created on Wed Oct 11 19:10:35 2017

@author: jyothish
"""
import os
import main
import io
import json
path='datasets/'
filelist=[]
filenames=os.listdir(path)
sourcelist=[x for x in filenames if x.endswith('.abstr')]
unconroled=[x for x in filenames if x.endswith('.uncontr')]
controlled=[x for x in filenames if x.endswith('.contr')]
phrase1,phrase2={},{}

##creating the keylists by our methods
for i in sourcelist:
    res1,res2=main.extract_phrases(path+i)
    phrase1.update({i.split('.')[0]:res1})
    phrase2.update({i.split('.')[0]:res2})
    with io.open('phrase1.json', 'w', encoding='utf8') as outfile:
        phra1 = json.dumps(phrase1,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
        outfile.write(phra1)
    with io.open('phrase2.json', 'w', encoding='utf8') as outfile:
        phra2 = json.dumps(phrase2,
                  indent=4, sort_keys=True,
                  separators=(',', ': '), ensure_ascii=False)
        outfile.write(phra2)
        
##create a json object of the user given keywords
#==============================================================================
# controlist={}
# for j in controlled:
#     keys=open(path+j).read().split()
#     controlist.update({j.split('.')[0]:keys})
#     with io.open('user_controled.json','w',encoding='utf8')as outfile:
#         control=json.dumps(controlist, indent=4,sort_keys=True,separators=(',',':'),ensure_ascii=False)
#         outfile.write(control)
# uncontrolist={}
# for j in unconroled:
#     keys=open(path+j).read().split()
#     controlist.update({j.split('.')[0]:keys})
#     with io.open('user_uncontroled.json','w',encoding='utf8')as outfile:
#         control=json.dumps(controlist, indent=4,sort_keys=True,separators=(',',':'),ensure_ascii=False)
#         outfile.write(control)
#     
#==============================================================================
##calculating the error measures and factors
with open('phrase1.json') as data_file:
    ouresults1 = json.load(data_file)
with open('phrase2.json') as datafile:
    ouresults2 = json.load(datafile)
with open('user_controled.json') as userdata:
    controlled_check=json.load(userdata)
with open('user_uncontroled.json') as userdata:
    uncontrolled_check=json.load(userdata)






def metric(result,check):
    precison={}
    recall={}
    fmeasure={}
    for i in result.keys():
        list1=result[i]
        list_=check[i]
        list2=[x.strip(';') for x in list_]
        b,s=len(list1),len(list2)
        if b>s:
            bigd=list1
            smalld=list2
        else:
            bigd=list2
            smalld=list1
        similars=[x for x in  smalld if x in bigd] 
        
        if len(list1)>0:
            precison.update({i:len(similars)/len(list1)})
            recall.update({i:len(similars)/len(list2)})
        else:
            recall.update({i:0})
            precison.update({i:0})
    
    for i in precison.keys():
        if precison[i]+recall[i]>0:
            fm=(2*precison[i]*recall[i])/(precison[i]+recall[i])
            fmeasure.update({i:fm})
        else:
            fmeasure.update({i:0})
            
            
            
    return precison,recall,fmeasure        
    




precision_score,recall_score,fmeaseure=metric(ouresults2,controlled_check)
fm=str(sum(fmeaseure.values())/1000)
pm=str(sum(precision_score.values())/1000)
rm=str(sum(recall_score.values())/1000)
with open('Result.txt','w')as ts:
    
    ts.write('F-Measure score:'+fm+'\n')
    ts.write('Precision score:'+pm+'\n')
    ts.write('Recall score:'+rm+'\n')



print('F-Measure score:',sum(fmeaseure.values())/1000)
print('Precision score:',sum(precision_score.values())/1000)
print('Recall score:',sum(recall_score.values())/1000)



