"""Simple package for clustering"""
from os import listdir
from sklearn import cluster
import numpy as np
import matplotlib.pyplot as plt


def run():
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
