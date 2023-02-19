def algo(a: list) -> list:
    """
    Insertion sort algorithm for sorting a list.
    >>> algo([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> algo([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> algo([1, 2, 3, 4, 1])
    [1, 1, 2, 3, 4]
    """
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j - 1] > a[j]:
            a[j - 1], a[j] = a[j], a[j - 1]
            j -= 1
    return a
