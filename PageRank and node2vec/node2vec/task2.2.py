


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
barbell_2 = nx.barbell_graph(1000, 50)

n2v = Node2Vec(p = 1, q = 1, d = 2, w=10)
n2v.fit(barbell_2)
embeddings = []
for node in barbell_2.nodes:
    embeddings.append(list(n2v.predict(node)))
# Construct a pandas dataframe with the 2D embeddings from node2vec.
# We can easily divide the nodes into two clusters, and the groudtruth is denoted by distinct colors.
toy_colors = ['red'] * 1025 + ['blue'] * 1025
df = pd.DataFrame(embeddings, columns = ['x', 'y']) # Create pandas dataframe from the list of node embeddings
df.plot.scatter(x = 'x', y = 'y', c = toy_colors)




# A barbell graph for your task 2.2

