"""
Contains various functions for computing statistics over 3D volumes
"""
import numpy as np

def Dice3d(a, b):
    """
    This will compute the Dice Similarity coefficient for two 3-dimensional volumes
    Volumes are expected to be of the same size. We are expecting binary masks -
    0's are treated as background and anything else is counted as data

    Arguments:
        a {Numpy array} -- 3D array with first volume
        b {Numpy array} -- 3D array with second volume

    Returns:
        float
    """
    if len(a.shape) != 3 or len(b.shape) != 3:
        raise Exception(f"Expecting 3 dimensional inputs, got {a.shape} and {b.shape}")

    if a.shape != b.shape:
        raise Exception(f"Expecting inputs of the same shape, got {a.shape} and {b.shape}")

    # TASK: Write implementation of Dice3D. If you completed exercises in the lessons
    # you should already have it.
    a[np.where(a>0)] = 1
    b[np.where(b>0)] = 1
    
    # 2 * common_elements / (size_a + size_b)
    
    common_elements = np.logical_and(a, b).sum()
    dice_score = 2 * common_elements / (np.sum(a>0) + np.sum(b>0))
    
    return dice_score

def Jaccard3d(a, b):
    """
    This will compute the Jaccard Similarity coefficient for two 3-dimensional volumes
    Volumes are expected to be of the same size. We are expecting binary masks - 
    0's are treated as background and anything else is counted as data

    Arguments:
        a {Numpy array} -- 3D array with first volume
        b {Numpy array} -- 3D array with second volume

    Returns:
        float
    """
    if len(a.shape) != 3 or len(b.shape) != 3:
        raise Exception(f"Expecting 3 dimensional inputs, got {a.shape} and {b.shape}")

    if a.shape != b.shape:
        raise Exception(f"Expecting inputs of the same shape, got {a.shape} and {b.shape}")

    # TASK: Write implementation of Jaccard similarity coefficient. Please do not use 
    # the Dice3D function from above to do the computation ;)
    a[np.where(a>0)] = 1
    b[np.where(b>0)] = 1

    # common_elements / (size_a + size_b - common_elements)
    
    common_elements = np.logical_and(a, b).sum()
    jaccard_score = common_elements / (np.sum(a>0) + np.sum(b>0) - common_elements)
    
    return jaccard_score

def Sensitivity(a, b):
    """
    This will compute the sensitivity for two 3-dimensional volumes
    Volumes are expected to be of the same size. We are expecting binary masks - 
    0's are treated as background and anything else is counted as data

    Arguments:
        a {Numpy array} -- 3D array with true mask
        b {Numpy array} -- 3D array with predicted

    Returns:
        float
    """
    if len(a.shape) != 3 or len(b.shape) != 3:
        raise Exception(f"Expecting 3 dimensional inputs, got {a.shape} and {b.shape}")

    if a.shape != b.shape:
        raise Exception(f"Expecting inputs of the same shape, got {a.shape} and {b.shape}")
        
    a[np.where(a>0)] = 1
    b[np.where(b>0)] = 1
        
    TP = np.sum(a*b)
    FN = np.sum(a * (1-b))
    sensitivity = (TP / (TP+FN))
        
    return sensitivity

def Specificity(a, b):
    """
    This will compute the specificity for two 3-dimensional volumes
    Volumes are expected to be of the same size. We are expecting binary masks - 
    0's are treated as background and anything else is counted as data

    Arguments:
        a {Numpy array} -- 3D array with true mask
        b {Numpy array} -- 3D array with predicted

    Returns:
        float
    """
    if len(a.shape) != 3 or len(b.shape) != 3:
        raise Exception(f"Expecting 3 dimensional inputs, got {a.shape} and {b.shape}")

    if a.shape != b.shape:
        raise Exception(f"Expecting inputs of the same shape, got {a.shape} and {b.shape}")
        
    a[np.where(a>0)] = 1
    b[np.where(b>0)] = 1
        
    TN = np.sum((1-a) * (1-b))
    FP = np.sum((1-a) * b)
    specificity = (TN / (TN+FP))
        
    return specificity