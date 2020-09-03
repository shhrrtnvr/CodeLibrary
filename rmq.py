class SegmentTree:
    def __init__(self, data):
        self.data = data
        self.sz = len(data) - 1
        self.tree = [None] * (4 * len(data))
        self.build(1, 0, self.sz)

    def build(self, v, tl, tr):
        if tl == tr:
            self.tree[v] = self.data[tl]
        else:
            tm = (tl + tr) // 2
            self.build(v << 1, tl, tm)
            self.build((v << 1) + 1, tm + 1, tr)
            self.tree[v] = self.tree[v << 1] + self.tree[(v << 1) + 1]

    def update(self, idx, val):
        self.__update__(1, 0, self.sz, idx, val)

    def __update__(self, v, tl, tr, idx, val):
        if tl == tr:
            self.tree[v] += val
        else:
            tm = (tl + tr) // 2
            if idx <= tm:
                self.__update__(v << 1, tl, tm, idx, val)
            else:
                self.__update__((v << 1) + 1, tm + 1, tr, idx, val)
            self.tree[v] = self.tree[v << 1] + self.tree[(v << 1) + 1]

    def query(self, l, r):
        return self.__query__(1, 0, self.sz, l, r)

    def __query__(self, v, tl, tr, l, r):
        if l > r:
            return 0
        if l == tl and r == tr:
            return self.tree[v]
        tm = (tl + tr) // 2
        left_val = self.__query__(v << 1, tl, tm, l, min(tm, r))
        right_val = self.__query__((v << 1) + 1, tm + 1, tr, max(tm + 1, l), r)
        return left_val + right_val


if __name__ == '__main__':
    n, q = map(int, input().split())
    A = [0] * n
    st = SegmentTree(A)
    for _ in range(q):
        com, x, y = map(int, input().split())
        if com == 0:
            st.update(x - 1, y)
        if com == 1:
            print(st.query(x - 1, y - 1))
