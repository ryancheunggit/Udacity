import numpy as np

def crossEntropy(s, l):
    return -np.sum(l*np.log(s), axis = 0)
    
print crossEntropy([0.7,0.2,0.1], [1,0,0])

print crossEntropy([.7,.2,.1], [[1,0,0],[0,1,0],[0,0,1]])