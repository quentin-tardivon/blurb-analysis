"""Main File"""
import hamming
import simple_cluster
import tfidf
from os import listdir
from sklearn import cluster
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets
import numpy as np
import matplotlib.pyplot as plt
from textblob import TextBlob as tb
from textblob import Word
from stemming.porter2 import stem
import features
import sys
reload(sys)
sys.setdefaultencoding('ascii')

#simple_cluster.run()
PATH = "./blurbs/"
FILENAMES = [PATH + f for f in listdir(PATH)]
files = []
for f in FILENAMES:
    fileOpen = open(f, "r")
    fileString = fileOpen.read()
    files.append(fileString)

X = tfidf.fast_tf_idf(files, 'learning')
Y = np.zeros(len(X))
for i in range(len(X)):
    Y[i] = i
plt.scatter(Y, X)
plt.show()
