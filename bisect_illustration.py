import bisect

if __name__ == '__main__':
    l = [1, 1, 1, 2, 3, 3, 4, 8, 8, 8, 10]
    x = bisect.bisect(l, 3)
    print(x)
    print(bisect.bisect_left(l, 8))
    print(bisect.bisect_left(l, 9))
    print(bisect.bisect(l, 9))
    bisect.insort(l, 7)
    print(l)