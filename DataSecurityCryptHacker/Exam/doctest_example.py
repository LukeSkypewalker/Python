def add(a, b):
    """This function demonstrate how doctests work for adding values

    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(10,-1)
    9
    """
    return a + b

def mul(a, b):
    """This function demonstrate how doctests work for multiplying values

    Examples
    --------
    >>> mul(add(2,3), 2)
    10
    >>> mul(10,-1)
    -10
    """
    return a*b

if __name__ == '__main__':
    import doctest
    doctest.testmod()