from typing import List, Tuple


class UnionFind:
    def __init__(self, size: int) -> None:
        """
        Initialize a UnionFind data structure with size elements.
        """
        # the index is initialized with the id of each element
        self.index: List[int] = list(range(size))

    def union(self, a: int, b: int) -> None:
        """
        Union two elements.
        This will make (a) a child of (b). The structure then represents a tree.
        """
        self.index[a] = self.index[b]

    def root(self, a: int) -> int:
        """
        Find the root of an element.
        """
        node = a
        node_id = self.index[node]
        while node != node_id:
            node = node_id
            node_id = self.index[node]
        return node

    def connected(self, a: int, b: int) -> bool:
        """
        Check if two elements are connected.
        Given that the index is a tree, we will need to follow the tree to the root.
        """
        return self.root(a) == self.root(b)
