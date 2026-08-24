import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    dp=np.dot(a,b)

    anorm=np.linalg.norm(a)
    bnorm=np.linalg.norm(b)
    if anorm == 0 or bnorm == 0:
        return 0.0

    return float(dp/(anorm*bnorm))