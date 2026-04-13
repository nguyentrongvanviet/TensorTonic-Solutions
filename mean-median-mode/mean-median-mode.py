import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    a = Counter(x) 
    ma = 0 
    res = 0 
    for key,value in a.items() : 
        if value>ma : 
            ma = value 
            res = key 
        elif value == ma : 
            res = min(res,key) 
    return np.mean(x) , np.median(x),res 