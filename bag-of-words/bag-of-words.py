import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here 
    data = np.zeros(len(vocab),dtype=int) 
    for i,x in enumerate(vocab) : 
        data[i] = tokens.count(x) 
    return data 