import numpy as np

def dropout(x, p, rng=None):
    """
    Applies inverted dropout to the input array.
    
    Args:
        x (numpy.ndarray): The input array.
        p (float): The probability of dropping an element (setting it to zero).
        rng (numpy.random.Generator, optional): Random number generator.
        
    Returns:
        tuple: (output_array, dropout_pattern)
    """
    # Edge case: If p is 1.0, everything is dropped
    x = np.array(x)
    if p == 1.0:
        return np.zeros_like(x), np.zeros_like(x, dtype=bool)
        
    # 1. Generate random numbers uniformly between [0.0, 1.0)
    if rng is not None:
        random_tensor = rng.random(x.shape)
    else:
        random_tensor = np.random.random(x.shape)
        
    # 2. Create the dropout pattern (mask)
    # Elements are kept if their random value is >= p. 
    # This happens with probability (1 - p).
    dropout_pattern = random_tensor >= p
    
    # 3. Calculate the scaling factor
    scale_factor = 1.0 / (1.0 - p)
    
    # 4. Apply the mask and scale simultaneously
    # Multiplying by the boolean array treats True as 1 and False as 0
    oldx = x 
    output = x * dropout_pattern * scale_factor
    
    return output, output/oldx 

# ==========================================
# Example Usage:
# ==========================================
