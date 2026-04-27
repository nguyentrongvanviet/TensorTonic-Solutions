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
# import numpy as np

# def matrix_normalization(matrix, axis=None, norm_type='l2'):
#     """
#     Chuẩn hóa ma trận dựa trên trục và loại chuẩn (L1, L2, Max).
    
#     Parameters:
#     - matrix: 2D array-like input
#     - axis: 0 (column-wise), 1 (row-wise), hoặc None (toàn bộ ma trận)
#     - norm_type: 'l1', 'l2', hoặc 'max'
#     """
#     # 1. Ánh xạ loại chuẩn (string) sang tham số 'ord' của NumPy
#     norm_mapping = {
#         'l1': 1,
#         'l2': None,
#         'max': np.inf
#     }
    
#     if norm_type not in norm_mapping:
#         return None 
#         # raise ValueError("norm_type phải là 'l1', 'l2', hoặc 'max'")
        
#     # Chuyển đổi input thành mảng NumPy kiểu float để tránh lỗi chia số nguyên
#     mat = np.array(matrix, dtype=float)
#     # mat = matrix
#     # 2. Tính toán ma trận/vector chuẩn (Norms)
#     # keepdims=True là chìa khóa! Nó giúp giữ nguyên số chiều để tự động Broadcasting.
#     # Ví dụ: Nếu tính theo hàng (axis=1), thay vì trả về shape (N,), nó trả về (N, 1)
#     # is_1d = (mat.ndim == 1)
#     if axis!=None: 
#         if 0<=axis and axis<=1 :
#             pass 
#         else : return None 
#     if mat.ndim!=2:
#         # Ép [1, 2, 3] thành [[1, 2, 3]] (1 hàng, N cột) để axis=1 không bị lỗi
#         # mat = np.atleast_2d(mat)
#         return None 
#     # -----------------------------------
#     norms = np.linalg.norm(mat, ord=norm_mapping[norm_type], axis=axis, keepdims=True)
    
#     # 3. Chống lỗi chia cho 0 (Divide by Zero)
#     # Nếu một hàng/cột chứa toàn số 0, norm của nó = 0. Chia cho 0 sẽ ra NaN.
#     # Ta thay các giá trị 0 trong norms thành 1 (vì 0 chia 1 vẫn bằng 0).
#     norms = np.where(norms == 0, 1.0, norms)
#     # 4. Thực hiện chia ma trận cho chuẩn
#     normalized_mat = mat / norms
#     return normalized_mat