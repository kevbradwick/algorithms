def algo(items: list) -> list:
    """
    Quicksort is an efficient algorithm for sorting a list of integers. The steps include:
    1. Pick a pivot point
    2. Move all items less than the pivot to the left of the pivot
    3. Move all items greater than the pivot to the right of the pivot
    4. Recursively sort the left and right sides of the pivot
    5. Return the sorted list
    >>> algo([1, 2, 3])
    [1, 2, 3]
    >>> algo([3, 2, 1])
    [1, 2, 3]
    >>> algo([1, 3, 2])
    [1, 2, 3]
    >>> algo([1, 2, 3, 4, 5, 6, 7, 8])
    [1, 2, 3, 4, 5, 6, 7, 8]
    """
    if len(items) <= 1:
        return items
    pivot = items[0]
    left = []
    right = []
    for item in items[1:]:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)
    return algo(left) + [pivot] + algo(right)