


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn


# Libaries for graph processing
import nodevectors
import networkx as nx





import math

class Node2Vec(nodevectors.Node2Vec):
    """
    Parameters
    ----------
    p : float
        p parameter of node2vec
    q : float
        q parameter of node2vec
    d : int
        dimensionality of the embedding vectors
    w : int
        length of each truncated random walk
    """
    def __init__(self, p = 1, q = 1,d = 32, w = 10):
        super().__init__(
                    n_components = d,
                    walklen = w,
                    epochs = 50,
                    return_weight = 1.0 / p,
                    neighbor_weight = 1.0 / q,
                    threads = 0,
                    w2vparams = {'window': 4,
                                'negative': 5, 
                                'iter': 10,
                                'ns_exponent': 0.5,
                                'batch_words': 128})


# A barbell graph for your task 2.1
barbell_1 = nx.barbell_graph(1000, 0)
n2v = Node2Vec(p = 1, q = 1, d = 10, w=10)
n2v.fit(barbell_1)
embeddings = []
for node in barbell_1.nodes:
    embeddings.append(list(n2v.predict(node)))


def f(node_id):
    a=0
    b=0
    tmp=0
    j=0
    c=[]
    res=[]
    for item in embeddings[node_id]:
        a=a+item*item
    
    
    
    for embedding in embeddings:
        j=0
        b=0
        tmp=0
        for i in embedding:
            b=b+i*i
            tmp=tmp+embeddings[node_id][j]*i
            j=j+1
        

        print(tmp)
        result=tmp/math.sqrt(a)*math.sqrt(b)
        res.append(result)

    
    

    return res

test=[]
test=f(5)
for item in test:
    print(item)




