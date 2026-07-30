import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    data = np.zeros(shape=(len(v),len(v))) 
    for i in range(len(v)): 
        data[i,i] = v[i] 
    return data 
    
