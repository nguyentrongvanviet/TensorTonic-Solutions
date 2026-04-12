import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    w = np.zeros(X.shape[1])
    b = 0 
    # Write code here
    while steps >0 : 
        p = _sigmoid(X@w+b)
        deltaW = X.T@(p-y)/X.shape[0] 
        deltaB = np.mean(p-y)
        w = w-lr*deltaW 
        b = b-lr*deltaB 
        steps-=1 
    return w,b
    
    pass