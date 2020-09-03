class Fenwick:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def psq(self, a):
        if a == 0:
            return 0
        return self.tree[a] + self.psq(a - (a & -a))

    def rsq(self, a, b):
        return self.psq(b) - self.psq(a - 1)

    def adjust(self, k, v):
        if k > len(self.tree):
            return
        self.tree[k] += v
        self.adjust(k + (k & -k), v)


if __name__ == '__main__':
    bit = Fenwick(10)
    for i in range(1, 11):
        bit.adjust(i, i)
    for i in range(1, 11):
        print(bit.psq(i))
