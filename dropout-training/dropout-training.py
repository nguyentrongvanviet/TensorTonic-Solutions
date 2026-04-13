import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    x = np.array(x)
    # Write code here
    if p == 1 :
        return np.zeros(x.shape),np.zeros(x.shape)
    mask = np.random.random(x.shape) if rng==None else rng.random(x.shape)
    # mask = np.random.random(x.shape) 
    # if rng != None :
    #     mask = rng.random(x.shape) # doan bua 
    mask = np.where(mask>=p,1,0)
    oldx = x 
    x = x*(mask/(1-p))
    mask = mask*(x/oldx)
    return x,mask

    