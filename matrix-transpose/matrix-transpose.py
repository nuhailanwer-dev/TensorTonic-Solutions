import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    x=np.asarray(A,dtype=int)
    rows,columns=x.shape
    transpose=np.zeros((columns,rows),dtype=int)

    for i in range(rows):
        for j in range(columns):
            transpose[j][i]=x[i][j]
        
        
    return transpose
