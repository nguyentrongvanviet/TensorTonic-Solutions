import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    k = np.array(k) 
    PMF = (1-p)**(k-1)*p
    # Write code here
    return PMF,1/p
    pass