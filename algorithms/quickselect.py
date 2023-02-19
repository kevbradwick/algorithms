from algorithms import quicksort


def algo(a: list, k: int) -> int:
    """
    Qckselect algorithm for finding the kth smallest element in a list.
    >>> algo([1, 2, 3, 4, 5], 1)
    1
    >>> algo([1, 2, 3, 4, 5], 2)
    2
    >>> algo([1, 2, 3, 4, 5], 3)
    3
    """
    a = quicksort.algo(a)
    return a[k - 1]
