import numpy as np

def quadratic_equ(a: float,b: float,c: float): # pylint: disable=invalid-name
    """
    solve for roots of quadratic equation with constants a, b, c
    """
    d = b**2 - 4 * a * c # pylint: disable=invalid-name

    num1 = -b + np.sqrt(d)
    num2 = -b - np.sqrt(d)
    den  =  2 * a

    root1 = num1 / den
    root2 = num2 / den

    return root1, root2