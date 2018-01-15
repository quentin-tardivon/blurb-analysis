"""Simple package for clustering"""
from os import listdir
from sklearn import cluster
import numpy as np
import matplotlib.pyplot as plt
import features
from sklearn.neighbors import NearestNeighbors


def cluster1():
    PATH = "./blurbs/"
    FILENAMES = [PATH + f for f in listdir(PATH)]
    DATA = np.zeros((len(FILENAMES), 3))

    i = 0
    for f in FILENAMES:
        fileOpen = open(f, "r")
        fileString = fileOpen.read()
        DATA[i][0] = len(fileString)
        fileOpen = open(f, "r")
        j = 0
        lines = fileOpen.readlines()
        for line in lines:
            if line[0:8] == "COMMENTS":
                if j+1 < len(lines):
                    for nextlines in lines[j+1::]:
                        DATA[i][1] += len(nextlines)
            j += 1
        i += 1
    K_MEANS = cluster.KMeans(n_clusters=3)
    K_MEANS.fit(DATA)

    i = 0
    for h in K_MEANS.labels_:
        DATA[i][2] = h
        i += 1
    X = np.zeros(len(DATA))
    Y = np.zeros(len(DATA))
    i = 0
    for d in DATA:
        X[i] = d[0]
        Y[i] = d[1]
        i += 1

    CENTERS = K_MEANS.cluster_centers_
    print CENTERS

    FIG = plt.figure()
    AX = FIG.add_subplot(111)
    SCATTER = AX.scatter(X, Y, c=K_MEANS.labels_, s=50)
    for i, j, h in CENTERS:
        AX.scatter(i, j, s=50, c='red', marker='+')
    AX.set_xlabel('x')
    AX.set_ylabel('y')
    plt.colorbar(SCATTER)
    plt.show()

def cluster2():
    f = features.features()
    nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(f)
    distances, indices = nbrs.kneighbors(f)

    print distances
    print indices


    K_MEANS = cluster.KMeans(n_clusters=5)
    K_MEANS.fit(f)

    X = np.zeros(len(f))
    Y = np.zeros(len(f))
    i = 0
    for d in f:
        X[i] = d[0]
        Y[i] = d[1]
        i += 1

    CENTERS = K_MEANS.cluster_centers_
    print CENTERS

    FIG = plt.figure()
    AX = FIG.add_subplot(111)
    SCATTER = AX.scatter(X, Y, c=K_MEANS.labels_, s=50)
    for i, j, k, l, m, n in CENTERS:
        AX.scatter(i, j, s=50, c='red', marker='+')
    AX.set_xlabel('x')
    AX.set_ylabel('y')
    plt.colorbar(SCATTER)
    plt.show()