#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    

    import numpy as np
    cleaned_data = []
    abs_residuals = np.abs(net_worths - predictions).flatten()
    cut_off = np.sort(abs_residuals)[::-1][8]
    for i in range(len(abs_residuals)):
        if abs_residuals[i] < cut_off:
            cleaned_data.append((ages[i][0],net_worths[i][0],abs_residuals[i]))
    
    
    return cleaned_data

