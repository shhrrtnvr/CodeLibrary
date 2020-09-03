class UnionFind:
    def __init__(self, n):
        self._num_of_set = n
        self._set_size = [1] * n
        self._rank = [0] * n
        self._parent = [i for i in range(n)]

    def findSet(self, i):
        if self._parent[i] != i:
            self._parent[i] = self.findSet(self._parent[i])
        return self._parent[i]

    def isSameSet(self, i, j):
        return self.findSet(i) == self.findSet(j)

    def numOfDisjointSet(self):
        return self._num_of_set

    def sizeOfSet(self, i):
        return self._set_size[self.findSet(i)]

    def unionSet(self, i, j):
        if self.isSameSet(i, j):
            return
        pi, pj = self.findSet(i), self.findSet(j)
        if self._rank[pi] > self._rank[j]:
            self._parent[pj] = pi
            self._set_size[pi] += self._set_size[pj]
        else:
            self._parent[pi] = pj
            self._set_size[pj] += self._set_size[pi]
            if self._rank[pi] == self._rank[pj]:
                self._rank[pj] += 1
        self._num_of_set -= 1


if __name__ == '__main__':
    uf = UnionFind(5)
    print(uf.numOfDisjointSet())
    uf.unionSet(0, 1)
    uf.unionSet(2, 3)
    uf.unionSet(4, 3)
    print(uf.numOfDisjointSet())
    print(uf.isSameSet(2, 3))
    print(uf.isSameSet(0, 3))
    print(uf.isSameSet(4, 3))

    for i in range(5):
        print(uf.findSet(i), uf.sizeOfSet(i))
    print(uf.numOfDisjointSet())
    uf.unionSet(2, 4)
    print(uf.numOfDisjointSet())
    uf.unionSet(1, 3)
    print(uf.numOfDisjointSet())
    uf.findSet(3)
    print(uf.sizeOfSet(2))


