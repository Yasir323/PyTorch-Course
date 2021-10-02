import numpy as np

def softmax(arr):
    expL = np.exp(arr)  # Broadcasting
    sumExpL = sum(expL)
    result = []
    for i in expL:
        result.append(i * 1.0/sumExpL)
    return result