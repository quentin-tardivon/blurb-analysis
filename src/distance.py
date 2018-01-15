"""Distance Calculations"""
from os import listdir
def sizeDistance(file1, file2):
    """Distance calc based on document size"""
    return abs(len(file1) - len(file2))

def hammingDistance(file1, file2):
    """Hamming Distance"""
    count = 0
    for i in range(min(len(file1), len(file2))):
        if file1[i] != file2[i]:
            count += 1
    count = count + max(len(file1), len(file2)) - min(len(file1), len(file2))
    return count