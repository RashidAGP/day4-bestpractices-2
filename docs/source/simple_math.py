"""
A collection of simple math operations
"""

def simple_add(a,b):
    """
    Add Two numbers and return the result. 

    Parameters
    ----------
    a : integer
        This can be any type: integer, floating point and etc, ...
    b : interger
        This can be any type: integer, floating point and etc, ...

    Returns
    -------
    x : integer
        The result of the simple add is returned.
    See Also
    --------
    lookfor, info 

    Examples
    ----------
    >>  
        This add 4 and 7 and return 11 as a result
    """
    return a+b

def simple_sub(a,b):
    return a-b

def simple_mult(a,b):
    return a*b

def simple_div(a,b):
    return a/b

def poly_first(x, a0, a1):
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
