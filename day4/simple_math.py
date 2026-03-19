"""
A collection of simple math operations
"""

def simple_add(a,b):
    r"""Simple addition of two numbers

    Parameters
    ----------
    a : numeric
        numeric means a python float or integer.
    b : numeric
        numeric means a python float or integer.

    Returns
    -------
    return a numeric value of the addition of the two parameters
    that can be integer or float, depending the original type of
    the input parameter.

    Raises
    ------
    OverflowError
        When the result is too large to be represented.

    Example
    --------
        >>> addition = simple_add(1,1)
        >>> print(addition)
        2
    """
    return a+b

def simple_sub(a,b):
    r"""Simple substraction of two numbers

    Parameters
    ----------
    a : numeric
        numeric means a python float or integer.
    b : numeric
        numeric means a python float or integer.

    Returns
    -------
    return a numeric value of the substraction of the two parameters
    that can be integer or float, depending the original type of
    the input parameter.

    Raises
    ------
    OverflowError
        When the result is too large to be represented.

    Example
    --------
        >>> substraction = simple_sub(1,1)
        >>> print(substraction)
        0
    """
    return a-b

def simple_mult(a,b):
    r"""Simple multiplication of two numbers

    Parameters
    ----------
    a : numeric
        numeric means a python float or integer.
    b : numeric
        numeric means a python float or integer.

    Returns
    -------
    return a numeric value of the multiplication of the two parameters
    that can be integer or float, depending the original type of
    the input parameter.

    Raises
    ------
    OverflowError
        When the result is too large to be represented.

    Example
    --------
        >>> multiplication = simple_mult(1,1)
        >>> print(multiplication)
        1
    """
    return a*b

def simple_div(a,b):
    r"""Simple division of two numbers

    Parameters
    ----------
    a : numeric
        numeric means a python float or integer.
    b : numeric
        numeric means a python float or integer.

    Returns
    -------
    return the float resulting of the division of the two parameters.

    Raises
    ------
    OverflowError
        When the result is too large to be represented.
    ZeroDivisionError
        When the second number is zero.

    Example
    --------
        >>> division = simple_div(1,1)
        >>> print(division)
        1
    """
    return a/b

def poly_first(x, a0, a1):
    r"""Simple first-degree polynomial calculation

    It use the simple following formula:
        f(x) = a0 + a1*x

    Parameters
    ----------
    x : numeric
        numeric means a python float or integer.
    a0 : numeric
        numeric means a python float or integer.
    a1 : numeric
        numeric means a python float or integer.

    Returns
    -------
    return a numeric value of the first-degree polynomial evaluation of
    the three parameters that can be integer or float, depending the
    original type of the input parameter.

    Raises
    ------
    OverflowError
        When the result is too large to be represented.

    Example
    --------
        >>> first_polynomial = poly_first(1,1,1)
        >>> print(first_polynomial)
        2
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    r"""Simple second-degree polynomial calculation

    It use the simple following formula:
        f(x) = a0 + a1*x + a2*(x**2)

    Parameters
    ----------
    x : numeric
        numeric means a python float or integer.
    a0 : numeric
        numeric means a python float or integer.
    a1 : numeric
        numeric means a python float or integer.
    a2 : numeric
        numeric means a python float or integer
    Returns
    -------
    return a numeric value of the second degree polynomial evaluation of
    the four parameters that can be integer or float, depending the
    original type of the input parameter.

    Raises
    ------
    OverflowError
        When the result is too large to be represented.

    Example
    --------
        >>> second_polynomial = poly_second(1,1,1,1)
        >>> print(first_polynomial)
        3
    """
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
