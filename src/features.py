"""Calculate features for each text"""
from textblob import TextBlob as tb
from textblob import Word
from os import listdir

def features():
    PATH = "./blurbs/"
    FILENAMES = [PATH + f for f in listdir(PATH)]
    X = []
    for f in FILENAMES:
        Y = []
        count = 0
        fileOpen = open(f, "r")
        fileString = fileOpen.readlines()    
        for line in fileString:
            if line[0:6] == "SOURCE":
                count = 0
            elif (line[0:4] == "GOAL") or (line[0:4] == "DATA") or (line[0:7] == "METHODS") or (line[0:7] == "RESULTS") or (line[0:8] == "COMMENTS"):
                Y.append(count)
                count = 0
            else:
                count += len(line)
        Y.append(count)
        if len(Y) == 6:
            X.append(Y)
    return X