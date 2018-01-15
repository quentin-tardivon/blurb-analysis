"""Calculate features for each text"""
from textblob import TextBlob as tb
from textblob import Word

def features(data):
    features = []
    blob = tb(data)    
    #features.append(len(blob.words))
    features.append(len(data))
    return features