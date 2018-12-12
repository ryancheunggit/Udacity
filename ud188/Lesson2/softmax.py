import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    return np.exp(L) / np.exp(L).sum()


if __name__ == '__main__':
    assert np.allclose([0.09003057317038046, 0.24472847105479764, 0.6652409557748219], softmax([5,6,7])), 'seems a bit off'
