!pip install pyspark
import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-11-openjdk-amd64"

# Import required packages
from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark import SparkContext
import pandas as pd

# Create the Spark Session
spark = SparkSession.builder.getOrCreate()

# The optional settings are shown below.

# spark = SparkSession.builder\
#         .master("local[4]")\
#         .appName("pyspark_study")\
#         .config("spark.driver.memory","1g")\
#         .config("spark.executor.memory","1g")\
#         .config("spark.executor.cores","2")\
#         .config("spark.cores.max","5")\
#         .getOrCreate()

# Create the Spark Context
sc = spark.sparkContext


#Task 1
#Count the number of each word
inputdata = sc.textFile("../input/wikipedia-sentences/wikisent2.txt")
output = inputdata.flatMap(lambda x: x.split(" ")).map(lambda x: (x, 1)).reduceByKey(lambda a, b: a + b)

result = output.collect()
for k, v in result:
    if k.isalpha():
        print("%s, %d" % (k.lower(),v))



#Task 2 (1)
#Find the most frequent word
inputdata = sc.textFile("../input/wikipedia-sentences/wikisent2.txt")
output = inputdata.flatMap(lambda x: x.split(" ")).map(lambda x: (x, 1)).reduceByKey(lambda a, b: a + b).sortBy(lambda x: x[1], False).take(1)
for k, v in output:
    print (k)




#Task 2 (2)
#Find the number of "China"
inputdata = sc.textFile("../input/wikipedia-sentences/wikisent2.txt")
Chinas = inputdata.flatMap(lambda x: x.split(" ")).map(lambda x: (x, 1)).reduceByKey(lambda a, b: a + b).filter(lambda x: "China" in x)
result = Chinas.collect()
sum=0
for k, v in result:
    sum+=v
print(sum)


#Task 2 (3)
#Count the total number of (non-unique) words that start with a specific letter.
inputdata = sc.textFile("../input/wikipedia-sentences/wikisent2.txt")
As = inputdata.flatMap(lambda x: x.split(" ")).map(lambda x: (x, 1)).reduceByKey(lambda a, b: a + b)
result = As.collect()
sum=[]
for i in range(26):
    sum.append(0)
for k, v in result:
    if k.startswith("a"):
        sum[0]+=v
    if k.startswith("b"):
        sum[1]+=v
    if k.startswith("c"):
        sum[2]+=v
    if k.startswith("d"):
        sum[3]+=v
    if k.startswith("e"):
        sum[4]+=v
    if k.startswith("f"):
        sum[5]+=v
    if k.startswith("g"):
        sum[6]+=v
    if k.startswith("h"):
        sum[7]+=v
    if k.startswith("i"):
        sum[8]+=v
    if k.startswith("j"):
        sum[9]+=v
    if k.startswith("k"):
        sum[10]+=v
    if k.startswith("l"):
        sum[11]+=v
    if k.startswith("m"):
        sum[12]+=v
    if k.startswith("n"):
        sum[13]+=v
    if k.startswith("o"):
        sum[14]+=v
    if k.startswith("p"):
        sum[15]+=v
    if k.startswith("q"):
        sum[16]+=v
    if k.startswith("r"):
        sum[17]+=v
    if k.startswith("s"):
        sum[18]+=v
    if k.startswith("t"):
        sum[19]+=v
    if k.startswith("u"):
        sum[20]+=v
    if k.startswith("v"):
        sum[21]+=v
    if k.startswith("w"):
        sum[22]+=v
    if k.startswith("x"):
        sum[23]+=v
    if k.startswith("y"):
        sum[24]+=v
    if k.startswith("z"):
        sum[25]+=v

for i in range(26):
    print(sum[i])

sc.stop()












