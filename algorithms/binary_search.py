from typing import List, Tuple


def algo(numbers: List[int], search: int) -> Tuple[int, int]:
    """
    Binary search will take a list, sort it, then keep halving the list until it finds 
    the number you are searching for. It will return a tuple containing the index of the 
    number and the number of attempts it took.
    
    >>> algo([1, 2, 3], 2)
    (1, 1)
    >>> algo([1, 2, 3, 4, 5, 6, 7, 8], 6)
    (5, 2)
    >>> algo([2, 4, 1, 6, 3, 5, 8, 7], 6) # unordered
    (5, 2)
    >>> algo(list(range(0, 1_000_000)), 250_000)
    (250000, 19)
    """
    a = 0
    b = len(numbers) - 1
    attempts = 0
    numbers.sort()

    while True:
        attempts += 1
        index = (b + a) // 2
        if numbers[index] == search:
            return index, attempts
        elif numbers[index] > search:
            b = index
        else:
            a = index
