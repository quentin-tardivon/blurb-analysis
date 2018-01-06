"""Main File"""
from os import listdir
import numpy as np
import matplotlib.pyplot as plt

PATH = "./blurbs/"
FILENAMES = [PATH + f for f in listdir(PATH)]
LENTAB = np.zeros(len(FILENAMES))
LENCOMMENTS = np.zeros(len(FILENAMES))

i = 0
for f in FILENAMES:
    fileOpen = open(f, "r")
    fileString = fileOpen.read()
    LENTAB[i] = len(fileString)
    fileOpen = open(f, "r")
    j = 0
    lines = fileOpen.readlines()
    for line in lines:
        if line[0:8] == "COMMENTS":
            if j+1 < len(lines):
                for nextlines in lines[j+1::]:
                    LENCOMMENTS[i] += len(nextlines)
        j += 1
    i += 1

plt.plot(LENTAB, LENCOMMENTS, 'bo')
plt.show()
