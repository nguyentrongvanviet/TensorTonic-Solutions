import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
        # Write code here
    a = np.asarray(a) 
    b = np.asarray(b) 
    lena = np.linalg.norm(a) 
    lenb = np.linalg.norm(b) 
    if lena ==0 or lenb == 0 : return 0 
    return a.dot(b)/(lena*lenb) 