"""
Selection sort will go through a list of items left to right and swap the next
value with the lowest value in the sub array.
"""


def swap(array, pos_1, pos_2):
    """
    Swap items in an array
    :param array:
    :param pos_1:
    :param pos_2:
    :return:
    """
    tmp = array[pos_1]
    array[pos_1] = array[pos_2]
    array[pos_2] = tmp
    return array


def min_val(items, start_index):
    """
    Find the minimum value from a list with a starting index
    :param items:
    :param start_index:
    :return:
    """
    smallest = items[start_index]
    smallest_index = start_index
    for i in range(start_index, len(items)):
        if items[i] < smallest:
            smallest = items[i]
            smallest_index = i

    return smallest_index


def sort_array(items):
    """
    Sort an array
    :param items:
    :return:
    """
    for i in range(0, len(items)):
        min_index = min_val(items, i)
        items = swap(items, min_index, i)

    return items


data = (
    ([2, 3, 4, 1, 5], [1, 2, 3, 4, 5]),
    ([1, 2, 1, 4, 6], [1, 1, 2, 4, 6]),
)

for input_array, expected in data:
    assert sort_array(input_array) == expected
