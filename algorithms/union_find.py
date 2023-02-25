from typing import List


class UnionFind:
    """
    Union-Find data structure.

    This data structure is used to find connected components in a graph. An example can be
    checking if two people are connected in a social network. It works by representing the
    graph as a tree. Each node in the tree is a connected component. Two nodes are deemed
    connected if they have the same root. The root of a node is the node that is not a
    child of any other node.

    For example;
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] -> has no connections
    [0, 3, 2, 3, 4, 5, 6, 7, 8, 9] -> 1 and 3 are connected
    [0, 3, 2, 7, 4, 5, 6, 7, 8, 9] -> 1, 3 and 7 are connected

    Tests for this data structure can be found in tests/test_union_find.py
    """

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
