"""Hamming Distance"""
def sizeDistance(file1, file2):
    """Distance calc based on document size"""
    return abs(len(file1) - len(file2))
