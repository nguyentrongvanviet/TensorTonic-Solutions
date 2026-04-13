import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    PMF = np.array([(1-p)**(x-1)*p for x in k ])
    # Write code here
    return PMF,1/p
    pass