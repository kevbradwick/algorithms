def algo(a: int, b: int) -> int:
    """
    Euclid's algorithm for finding the greatest common divisor of two numbers.
    >>> algo(10, 15)
    5
    >>> algo(10, 20)
    10
    >>> algo(10, 0)
    10
    >>> algo(0, 10)
    10
    >>> algo(0, 0)
    0
    >>> algo(10, 10)
    10
    >>> algo(10, 1)
    1
    >>> algo(2740, 1760)
    20
    """

    while b != 0:
        a, b = b, a % b
    return a
