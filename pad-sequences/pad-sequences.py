import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    N = len(seqs) 
    L =max_len
    if max_len == None : 
        L = max(len(seq) for seq in seqs) 
    ans = np.full((N,L),pad_value)
    for index,seq in enumerate(seqs):
        for i,e in enumerate(seq) : 
            if i==L: break 
            ans[index][i]=e
    return ans 
    pass