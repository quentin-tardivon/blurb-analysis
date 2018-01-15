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

"""
X = []
X.append(tfidf.fast_tf_idf(files, "learning"))
X.append(tfidf.fast_tf_idf(files, "knn"))
X.append(tfidf.fast_tf_idf(files, "neural"))
X.append(tfidf.fast_tf_idf(files, "network"))
X.append(tfidf.fast_tf_idf(files, "deep"))
"""
X = []
for f1 in files:
    Y = []
    for f2 in files:
        Y.append(distance.hammingDistance(f1, f2))
    X.append(Y)

plt.matshow(X)
plt.show()