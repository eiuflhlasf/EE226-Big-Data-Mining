!pip install datasketch
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tqdm import tqdm
import csv






from datasketch import MinHash, MinHashLSH


batchsize=100
m=[]
j=0
data=[]
new=[]





with open('../input/coding2/docs_for_lsh.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row[1:-1])
    for i in range(1,len(data)):
        new.append(data[i])
    
    batchsize=len(new)
    
    for i in range(0, batchsize):
        m.append(MinHash(num_perm=32))
        

    for i in range(0, batchsize):
        for d in new[i]:
            m[i].update(d.encode('utf8'))
        print(i)
    # Create LSH index
    lsh = MinHashLSH(threshold=0.8, num_perm=32)
    for i in range(0, batchsize):
        lsh.insert("m%d" % i, m[i])
    result = lsh.query(m[0])
    print("Approximate neighbours with Jaccard similarity > 0.8")
    for i in range(0,30):
        print(result[i])




#print("Estimated Jaccard for data1 and data2 is", m1.jaccard(m2))












