
# -*- coding: utf-8 -*-

"""
Created on Wed Oct 11 13:42:35 2017

@author: jyothish
"""
import textrank
def extract_phrases(filename):
    """Print the keywords to the user"""
    hyper1=['NN', 'JJ', 'NNP']#lexical unit filter
                     #2-10 window size
    with open(filename)as f:
            phrases1,phrases2=textrank.extract_keywords(f.read(),hyper1)
            #print(phrases1)
            #print(phrases2)
    return phrases1,phrases2
#==============================================================================
#     with open(filename+'/my/'+'result1','w')as d:
#         d.write(str(phrases1))
#==============================================================================
#==============================================================================
#     with open(filename+'my/result2','w')as d:
#         d.write(str(phrases2))
#    
#     
#==============================================================================

if __name__ =='__main__':
    extract_phrases('test.txt')