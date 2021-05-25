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


pairs1=[]
pairs2=[]


link_prediction=[]
node_prediction=[]
node_label=[]
fake=[]
fake.append(5)

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













df = pd.read_csv("space_data.csv")
df.head()


G = nx.from_pandas_edgelist(df, "source", "target",  create_using=nx.Graph())



def get_randomwalk(node, path_length):
    
    random_walk = [str(node)]
    
    for i in range(path_length-1):
        temp = list(G.neighbors(node))
        temp = list(set(temp) - set(random_walk))
        if len(temp) == 0:
            break
        
        random_node = random.choice(temp)
        random_walk.append(str(random_node))
        node = random_node
    
    return random_walk




# get list of all nodes from the graph
all_nodes = list(G.nodes())

random_walks = []
for n in tqdm(all_nodes):
    for i in range(5):
        random_walks.append(get_randomwalk(n,5))

# count of sequences
print(len(random_walks))





# train skip-gram (word2vec) model
model = Word2Vec(window = 4, sg = 1, hs = 0,
                 negative = 10, # for negative sampling
                 alpha=0.03, min_alpha=0.0007,
                 seed = 14)

model.build_vocab(random_walks, progress_per=2)

model.train(random_walks, total_examples = model.corpus_count, epochs=20, report_delay=1)


links=model.similar_by_word('0')
for link in links:
    print(link[1])


#link prediction
with open('author_pairs_to_pred_with_index.csv','r') as csvfile1:
    next(csvfile1)
    reader = csv.reader(csvfile1)
    for row in reader:
        temp = row[1]
        temp = temp.split(" ")
        if (temp[0].isdigit):
            pairs1.append(temp[0])
        if (temp[1].isdigit):
            pairs2.append(temp[1])



for i in range(len(pairs1)):
    links=model.similar_by_word(str(pairs1[i]))
    for link in links:
        flag=0
        if (link[0]==pairs2[i]) :
            flag=1
            link_prediction.append(link[1])

        if (link[0]!=-1):
            tmp[pairs1[i]]=pairs2[i]

    if (flag==0):
        link_prediction.append(0.5)




with open('submit.csv','w') as csvfile1:
    csvfile1.write("id,label\n")
    k=0
    for item in link_prediction:
        csvfile1.write(str(k)+","+str(item)+"\n")












#node prediction
with open('authors_to_pred.csv','r') as csvfile1:
    next(csvfile1)
    reader = csv.reader(csvfile1)
    for row in reader:
        node_prediction.append(row[0])

#add existing labels
for item in node_prediction:
    for author in authors:
        if (author.author_id==item):
            if (author.label!='100'):
                node_label.append(author)


for i in range(len(node_prediction)):
    flagg=0
    for node_l in node_label:
        if (node_l.author_id==node_prediction[i]):
            flagg=1
            break

    if (flagg==1):
        continue

    links=model.similar_by_word(str(node_prediction[i]))
    for link in links:
        flag=0
        
        if (link[0]!=-1):
            for author in authors:
                if (author.author_id==link[0]):
                    if (author.label!='100'):
                        flag=1
                        node_label.append(author)
                        break

    if (flag==0):
        node_label.append(fake)




with open('submit1.csv','w') as csvfile1:
    csvfile1.write("author_id,labels\n")
    k=0
    for item in node_prediction:
        csvfile1.write(str(item)+",")
        for node_l in node_label[k].label:
            if (node_l.isdigit):
                csvfile1.write(str(node_l)+" ")
        csvfile1.write("\n")
        k=k+1

