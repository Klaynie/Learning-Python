import numpy as numpy
from numpy.random import randn

def test_randomnormal_distribution(n):
    d = {}
    for randomNumber in randn(n):
        if randomNumber <= 1 and randomNumber >= -1:
            d['In mean'] = d.get('In mean', 0) + 1
        else:
            d['Not in mean'] = d.get('Not in mean', 0) + 1
    for key, value in d.items():
        d[key] = value/n*100
    return d

print(test_randomnormal_distribution(100000000))