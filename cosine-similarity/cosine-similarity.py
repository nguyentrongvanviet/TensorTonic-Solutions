import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
        # Write code here
    ok = np.linalg.norm(a)*np.linalg.norm(b)
    return np.array(a)@np.array(b).T/((np.linalg.norm(a)*np.linalg.norm(b))) if ok else 0 
    pass