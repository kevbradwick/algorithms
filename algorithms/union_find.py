from typing import List


class UnionFind:
    def __init__(self, size: int) -> None:
        """
        Initialize a UnionFind data structure with size elements.
        """
        # the index of the element is the element itself and the value is an id that is
        # unique for each connected component. -1 means that the element is not connected
        # to any other element.
        self.index: List[int] = list(range(size))

    def union(self, a: int, b: int) -> None:
        """
        Union two elements.
        This will change the id of (a) and all connected nodes to the id of (b).
        """

        a_id = self.index[a]
        b_id = self.index[b]

        for i, v in enumerate(self.index):
            if v == a_id:
                self.index[i] = b_id

    def connected(self, p: int, q: int) -> bool:
        """
        Check if two elements are connected.
        """
        if self.index[p] == -1 or self.index[q] == -1:
            return False

        try:
            return self.index[p] == self.index[q]
        except IndexError:
            return False


def test_union_find(a: int, b: int) -> bool:
    """
    Test function for the union find data structure.
    >>> test_union_find(1, 3)
    True
    >>> test_union_find(1, 5)
    False
    >>> test_union_find(5, 9)
    True
    >>> test_union_find(1, 7)
    True
    """
    uf = UnionFind(10)
    uf.union(1, 2)
    uf.union(2, 3)
    uf.union(5, 9)
    uf.union(1, 7)

    return uf.connected(a, b)
