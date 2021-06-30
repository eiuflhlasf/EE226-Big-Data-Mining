import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


import networkx as nx

G_tmp = nx.read_edgelist('../input/google-web-graph/web-Google.txt', create_using = nx.DiGraph)
print(nx.info(G_tmp))

c = sorted(nx.weakly_connected_components(G_tmp), key=len, reverse=True)
wcc_set = c[0]
G = G_tmp.subgraph(wcc_set)
print(nx.info(G))


# Your code here, you can add cells if necessary
def pagerank(graph, damping_factor=0.85, max_iterations=100, \
             min_delta=0.00001):
    nodes = graph.nodes()
    graph_size = len(nodes)
    if graph_size == 0:
        return {}
    
    init_value=1/graph_size
    #初始化每个页面的pagerank值为1/n
    pagerank = dict.fromkeys(nodes, init_value)
    print ('This is NO.0 iteration')
    for j,(k,v) in enumerate(pagerank.items()):
        print({k:v},end="")
        print ('\n')
        if j==10:
            break

    for i in range(max_iterations):
        diff = 0 #total difference compared to last iteraction
        # computes each node PageRank based on inbound links
        for node in nodes:
            rank = (1.0-damping_factor)/graph_size
            for referring_page in nx.neighbors(graph,node):
                length=len(list(nx.neighbors(graph,referring_page)))
                rank += damping_factor * pagerank[referring_page] / length

        
        
            diff += abs(pagerank[node] - rank)
            pagerank[node] = rank

        print ('This is NO.%s iteration' % (i+1))
        for j,(k,v) in enumerate(pagerank.items()):
            print({k:v},end="")
            print ('\n')
            if j==10:
                break
        
        print ('\n')
        
        #stop if PageRank has converged
        if diff < min_delta:
            break

return pagerank

pagerank(G)


