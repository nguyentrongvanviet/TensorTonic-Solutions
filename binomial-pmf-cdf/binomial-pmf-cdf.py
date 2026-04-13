import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    PMF = comb(n,k)*(p**k)*((1-p)**(n-k))
    # CDF = 0 
    CDF = sum((comb(n,i)*(p**i)*((1-p)**(n-i))) for i in range(k+1))
    # Write code here
    return PMF , CDF 
    pass