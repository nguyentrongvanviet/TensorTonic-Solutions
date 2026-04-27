import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    # Write code here
    norm_map = {
        'l1' :1 , 
        'l2' : None , 
        'max': np.inf 
    }
    # if norm_type == 'l2' : 
    #     type = None 
    # elif norm_type == 'l1' :
    #     type = '1'
    # else : 
    #     type = 'inf'
    if norm_type not in norm_map : 
        return None 
    if np.asarray(matrix).ndim!=2 : return None 
    if axis!=None : 
        if axis>1 or axis<0 : return None 
    array =  np.linalg.norm(matrix,ord=norm_map[norm_type],axis=axis,keepdims=True)
    array = np.where(array == 0, 1.0, array)
    return matrix/array