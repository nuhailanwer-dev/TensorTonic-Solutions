import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Vectorized sigmoid function.
    """
    # Write code here
    value =np.asarray(x,dtype=float)
    
    return (1/(1+np.exp(-value)))