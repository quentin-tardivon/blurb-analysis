"""Package to create a tf-idf Matrix from documents"""
from stemming.porter2 import stem
from textblob import TextBlob as tb
import math

def tf(f, word):
    blob = tb(f)
    stemList = []
    tf = 0
    word = stem(word)
    try:
        for words in blob.words:
            stemList.append(stem(words))
        for stemWord in stemList:
            if stemWord == word:
                tf += 1
        return tf
    except UnicodeDecodeError:
        return -1

def idf(data, word):
    d = 1
    for f in data:
        if (tf(f, word) != 0):
            d += 1
    return len(data)/d

def tf_idf(data, f, word):
    return tf(f, word) * idf(data, word)

def fast_tf_idf(data, word):
    X = []
    temp = idf(data, word)
    for f in data:
        x = tf(f, word) * temp
        if x < 0:
            X.append(-1)
        X.append(x)
        
    return X
