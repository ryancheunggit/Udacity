import numpy as np
import pandas as pd
# Setting the random seed, feel free to change it and see different solutions.
np.random.seed(42)

def stepFunction(t):
    return 1 if t >=0 else 0

def prediction(X, W, b):
    return stepFunction((np.matmul(X,W) + b)[0])

# TODO: Fill in the code below to implement the perceptron trick.
# The function should receive as inputs the data X, the labels y,
# the weights W (as an array), and the bias b,
# update the weights and bias W, b, according to the perceptron algorithm,
# and return W and b.
def perceptronStep(X, y, W, b, learn_rate = 0.01):
    n = X.shape[0]
    for idx in range(n):
        y_pred = prediction(X[idx], W, b)
        if y_pred != y[idx]:
            W += (y[idx] - y_pred) * learn_rate * np.expand_dims(X[idx], -1)
            b += (y[idx] - y_pred) * learn_rate
    return W, b

if __name__ == '__main__':
    data = pd.read_csv('perceptron_alg_data.csv', names=['x1', 'x2', 'y'])
    X, y = data[['x1', 'x2']].values, np.expand_dims(data['y'].values, -1)
    x_min, x_max = min(X.T[0]), max(X.T[0])
    y_min, y_max = min(X.T[1]), max(X.T[1])
    W = np.array(np.random.rand(2,1))
    b = np.random.rand(1)[0] + x_max
    learn_rate = 0.01
    iterations = 100
    print('running for {} iterations with learning rate {}'.format(iterations, learn_rate))
    for iteration in range(iterations):
        y_pred = (X.dot(W) + b >= 0).astype(int)
        mis_classified_idx = np.where(y_pred != y)[0]
        print('iteration {} with mis-classified {}'.format(iteration + 1, len(mis_classified_idx)))
        W, b = perceptronStep(X, y, W, b, learn_rate = learn_rate)
