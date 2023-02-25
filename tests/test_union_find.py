from algorithms.union_find import UnionFind


class TestUnionFind:
    def test_union_index(self):
        uf = UnionFind(10)
        uf.union(1, 3)
        assert uf.index == [0, 3, 2, 3, 4, 5, 6, 7, 8, 9]

        uf.union(5, 9)
        assert uf.index == [0, 3, 2, 3, 4, 9, 6, 7, 8, 9]

        uf.union(3, 7)
        assert uf.index == [0, 3, 2, 7, 4, 9, 6, 7, 8, 9]

    def test_root(self):
        uf = UnionFind(10)

        assert uf.root(1) == 1
        assert uf.root(5) == 5

        uf.union(1, 3)
        assert uf.root(1) == 3

        uf.union(3, 7)
        assert uf.root(1) == 7

    def test_connected(self):
        uf = UnionFind(10)
        uf.union(1, 2)
        uf.union(2, 3)
        uf.union(3, 4)
        uf.union(5, 9)
        uf.union(1, 7)

        assert not uf.connected(1, 3)  # because it was reassigned at the end
        assert not uf.connected(1, 5)
        assert uf.connected(2, 4)
        assert uf.connected(5, 9)
        assert uf.connected(1, 7)
        assert not uf.connected(7, 8)
