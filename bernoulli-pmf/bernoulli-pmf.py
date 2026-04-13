import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    x = np.array([p if e==1 else 1-p for e in x ]) 
    return x,p , p*(1-p)
    # Write code here
    pass