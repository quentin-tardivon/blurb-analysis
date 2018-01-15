"""Main File"""
import distance
import simple_cluster
import tfidf
from os import listdir
from sklearn import cluster
from sklearn.neighbors import NearestNeighbors
from matplotlib.colors import ListedColormap
from sklearn import cluster
from sklearn import neighbors, datasets
import numpy as np
import matplotlib.pyplot as plt
from textblob import TextBlob as tb
from textblob import Word
from stemming.porter2 import stem
import features

#simple_cluster.run()
PATH = "./blurbs/"
FILENAMES = [PATH + f for f in listdir(PATH)]
files = []
for f in FILENAMES:
    fileOpen = open(f, "r")
    fileString = fileOpen.read()
    files.append(fileString)


# tfidf calculus

print "TFIDF Step"
print "TFIDF for learning"
print tfidf.fast_tf_idf(files, "learning")
print "TFIDF for knn"
print tfidf.fast_tf_idf(files, "knn")
print "TFIDF for neural"
print tfidf.fast_tf_idf(files, "neural")
print "TFIDF for network"
print tfidf.fast_tf_idf(files, "network")
print "TFIDF for deep"
print tfidf.fast_tf_idf(files, "deep")

# Classification by TF
Y = ["learning", "knn", "neural", "network", "deep"]
X = []
for f in files:
    temp = []
    for word in Y:
        temp.append(tfidf.tf(f, word))
    X.append(temp)
print "TF for [learning, knn, neural, network, deep]"
print X

# Hamming Distance
X = []
for f1 in files:
    Y = []
    for f2 in files:
        Y.append(distance.hammingDistance(f1, f2))
    X.append(Y)

print "Matrix of Hamming Distance between all files"
plt.matshow(X)
plt.show()

# Simples clustering
print "Clustering by K_Means on 2 features: size of the document and size of the commentary"
simple_cluster.cluster1()
print "Clustering by K_Means on 6 features: size of each part of the document"
simple_cluster.cluster2()