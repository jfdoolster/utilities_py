import numpy as np

def quadratic_equ(a:float, b:float, c:float) -> tuple[float, float]:
    """
    solve for roots of quadratic equation with constants a, b, c
    """
    d = b**2 - 4 * a * c

    num1 = -b + np.sqrt(d)
    num2 = -b - np.sqrt(d)
    den  =  2 * a

    root1 = num1 / den
    root2 = num2 / den

    return root1, root2


def moving_average(arr:np.ndarray, n:int=3) -> np.ndarray:
    if n < 1: return arr
    ret = np.cumsum(arr, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    nan_arr = np.empty((n-1,))
    nan_arr[:] = np.nan
    return np.hstack((nan_arr, np.array(ret[n-1:]/n)))
