import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import to_categorical
from keras.preprocessing import image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tqdm import tqdm
import csv
import networkx as nx
import pandas as pd
import numpy as np
import random
from tqdm import tqdm
from sklearn.decomposition import PCA

import matplotlib.pyplot as plt







from gensim.models import Word2Vec

import warnings
warnings.filterwarnings('ignore')



authors=[]
relations=[]
index_1=[]
index_2=[]


class relation():
    def __init__(self, author_id1, author_id2):
        self.author_id1=author_id1
        self.author_id2=author_id2





class author():
    def __init__(self, author_id, paper_id, label, index):
        self.author_id=author_id
        self.paper_id=paper_id
        self.label=label
        self.index=index
        self.multilabel=[]

i=0

with open('labeled_papers_with_authors.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        authors.append(author(row[0],row[1], row[3],i))
        i=i+1

with open('author_paper_all_with_year.csv','r') as csvfile1:
    reader = pd.read_csv(csvfile1,skiprows=18649)
    for row in reader:
        authors.append(author(row[0],row[1], '100',i))
        i=i+1


with open('paper_reference.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        for author in authors:
            if author.paper_id==row[0]:
                index1=author.index
    
        for author in authors:
            if author.paper_id==row[1]:
                index2=author.index
                relations.append(relation(int(authors[index1].author_id),int(authors[index2].author_id )))


print(relations[1].author_id1)





for i in range (93231):
    flag=1
    for j in relations:
        if (i==j.author_id1) or (i==j.author_id2):
            flag=0
    if flag :
        relations.append(relation(i, -1))
        print(i)










f = open('space_data.csv', 'w')
f.write('source,target\n')
for i in relations:
    print(str(i.author_id1)+',' +str(i.author_id2)+'\n')
    f.write(str(i.author_id1)+',' +str(i.author_id2)+'\n')
f.close()











df = pd.read_csv("space_data.csv")
df.head()


G = nx.from_pandas_edgelist(df, "source", "target",  create_using=nx.Graph())



def get_randomwalk(node, path_length):
    
    random_walk = [node]
    
    for i in range(path_length-1):
        temp = list(G.neighbors(node))
        temp = list(set(temp) - set(random_walk))
        if len(temp) == 0:
            break
        
        random_node = random.choice(temp)
        random_walk.append(random_node)
        node = random_node
    
    return random_walk




# get list of all nodes from the graph
all_nodes = list(G.nodes())

random_walks = []
for n in tqdm(all_nodes):
    for i in range(5):
        random_walks.append(get_randomwalk(n,10))

# count of sequences
print(len(random_walks))





# train skip-gram (word2vec) model
model = Word2Vec(window = 4, sg = 1, hs = 0,
                 negative = 10, # for negative sampling
                 alpha=0.03, min_alpha=0.0007,
                 seed = 14)

model.build_vocab(random_walks, progress_per=2)

model.train(random_walks, total_examples = model.corpus_count, epochs=20, report_delay=1)


model.similar_by_word('0')
