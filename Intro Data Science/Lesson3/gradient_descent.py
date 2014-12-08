import numpy
import pandas

def compute_cost(features, values, theta):
    """
    Compute the cost of a list of parameters, theta, given a list of features
    (input data points) and values (output data points).
    """
    m = len(values)
    sum_of_square_errors = numpy.square(numpy.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def gradient_descent(features, values, theta, alpha, num_iterations):
    """
    Perform gradient descent given a data set with an arbitrary number of features.
    """

    # Write code here that performs num_iterations updates t                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         o the elements of theta.
    # times. Every time you compute the cost for a given list of thetas, append it
    # to cost_history.
    # See the Instructor notes for hints.

    cost_history = []
    n = len(theta)
    m = len(values)
    for i in range(num_iterations):
        predicted_values = numpy.dot(features, theta)
        theta = theta - alpha/m*numpy.dot((predicted_values - values), features)
        cost_history.append(compute_cost(features, values, theta))


    return theta, pandas.Series(cost_history) # leave this line for the grader
