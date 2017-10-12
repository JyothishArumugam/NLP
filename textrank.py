# -*- coding: utf-8 -*-

"""
Created on Wed Oct 11 13:48:08 2017

@author: jyothish
"""

import networkx as nx
import itertools
import nltk


def graph_building1(nodes,edges):
    """
    Build a graph and give back
    """
    G=nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    return G
def levenshtein_distance(first, second):
    """Return the Levenshtein distance between two strings.
    Based on:
        http://rosettacode.org/wiki/Levenshtein_distance#Python
    """
    if len(first) > len(second):
        first, second = second, first
    distances = range(len(first) + 1)
    for index2, char2 in enumerate(second):
        new_distances = [index2 + 1]
        for index1, char1 in enumerate(first):
            if char1 == char2:
                new_distances.append(distances[index1])
            else:
                new_distances.append(1 + min((distances[index1],
                                             distances[index1 + 1],
                                             new_distances[-1])))
        distances = new_distances
    return distances[-1]
def graph_building2(nodes):
    gr = nx.Graph()
    gr.add_nodes_from(nodes)
    nodePairs = list(itertools.combinations(nodes, 2))

    # add edges to the graph (weighted by Levenshtein distance)
    for pair in nodePairs:
        firstString = pair[0]
        secondString = pair[1]
        levDistance = levenshtein_distance(firstString, secondString)
        gr.add_edge(firstString, secondString, weight=levDistance)

    return gr




def phrase_check(ranked_text2,textlist):
    dealt_with = set([])
    modified_key_phrases =set([])
    i = 0
    j = 1
    while j < len(textlist):
        first,second=textlist[i],textlist[j]
        if first in ranked_text2 and second in ranked_text2:
            dealt_with.add(first)
            dealt_with.add(second)
            modified_key_phrases.add(first+' '+second)
        #print(ranked_text2)
        i=i+1
        j=j+1
    modified_key_phrases=list(modified_key_phrases)
    dealt_with=list(dealt_with)
    ranked_text2=[x for x in ranked_text2 if x not in dealt_with]
    final=modified_key_phrases+ranked_text2
    return final


def extract_keywords(text,hp1):
    #tokenise and annotate with pos tags-----------------------------
    words_tokenized=nltk.word_tokenize(text)
    pos_tagged=nltk.pos_tag(words_tokenized)
    textlist = [x[0] for x in pos_tagged]
    
    #syntactic filter to select particular class of pos tags-------------
    with_noise_desired_words=[x[0] for x in pos_tagged if x[1] in hp1]
    desired_words=set([x for x in with_noise_desired_words if x.isalpha() and len(x)>1])
    
    #graph building----------------------------
    neighbours=nltk.bigrams(words_tokenized)
    graph_cocurence=list(itertools.combinations(desired_words,2))
    edges=set([x for x in graph_cocurence if x in neighbours])
    graph=graph_building1(desired_words,edges)
    graph2=graph_building2(desired_words)
    
    ##rank calculation---------------------------------
    calculated_text_rank1 = nx.pagerank(graph, weight='weight')
    calculated_text_rank2 = nx.pagerank(graph2, weight='weight')
    textranked=sorted(calculated_text_rank1,key=calculated_text_rank1.get,reverse=True)
    textranked2=sorted(calculated_text_rank2,key=calculated_text_rank2.get,reverse=True)
    final1=phrase_check(textranked[:int(len(textranked)/3)],textlist)
    final2=phrase_check(textranked2[:int(len(textranked2)/3)],textlist)
    #textranked=sorted(calculated_text_rank)
    
    
    
    return final1,final2
    
    
