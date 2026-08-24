import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    # Write code here
    difference = np.asarray(x, dtype=float) - np.asarray(y, dtype=float) 
    ed=np.sqrt(np.sum(difference**2))
    return ed