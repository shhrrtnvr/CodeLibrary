import math
class SegmentTree:
    import sys
    sys.setrecursionlimit(10**9)
    def __init__(self, data, *, fn = sum , default=0):
        self.fun = fn
        self.default = default
        self.sz = len(data) - 1
        self.tree = [default] * (4 * len(data))
        self.__build__(data, 1, 0, self.sz)
        
    def __build__(self, data, v, tl, tr):
        if tl == tr:
            self.tree[v] = data[tl]
        else:
            tm = (tl + tr) >> 1
            self.__build__(data, v << 1, tl, tm)
            self.__build__(data, (v << 1) + 1, tm + 1, tr)
            self.tree[v] = self.fun((self.tree[v << 1], self.tree[(v << 1) + 1]))
 
    def update(self, idx, val):
        self.__update__(1, 0, self.sz, idx, val)
 
    def __update__(self, v, tl, tr, idx, val):
        if tl == tr:
            self.tree[v] = val
        else:
            tm = (tl + tr) >> 1
            if idx <= tm:
                self.__update__(v << 1, tl, tm, idx, val)
            else:
                self.__update__((v << 1) + 1, tm + 1, tr, idx, val)
            self.tree[v] = self.fun((self.tree[v << 1], self.tree[(v << 1) + 1]))
 
    def query(self, l, r):
        return self.__query__(1, 0, self.sz, l, r)
 
    def __query__(self, v, tl, tr, l, r):
        if l > r:
            return self.default
        if l == tl and r == tr:
            return self.tree[v]
        tm = (tl + tr) // 2
        left_val = self.__query__(v << 1, tl, tm, l, min(tm, r))
        right_val = self.__query__((v << 1) + 1, tm + 1, tr, max(tm + 1, l), r)
        return self.fun((left_val, right_val))
 
import sys
input = sys.stdin.readline
from time import time
if __name__ == '__main__':
    t = time()
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    st = SegmentTree(A, fn=min, default=10**10)
    for _ in range(q):
        com, x, y = map(int, input().split())
        if com == 1:
            st.update(x - 1, y)
        if com == 2:
            print(st.query(x - 1, y - 1))
    print('Time taken', (time()-t) * 1000, 'ms')