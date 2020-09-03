# using extended gcd start
def inv1(a, mod):
    def _gcd(_a, _b):
        if _b == 0:
            return _a, 1, 0
        _g, _x, _y = _gcd(_b, _a % _b)
        return _g, _y, _x - _y * (_a // _b)

    g, x, y = _gcd(a, mod)
    if g == 1:
        return ((x % mod) + mod) % mod


# using binary exponentiation
def inv2(a, mod):
    res, b = 1, mod - 2
    while b != 0:
        if b & 1:
            res = res * a % mod
        a, b = a*a % mod, b >> 1
    return res


if __name__ == '__main__':
    a, m = 13, 11
    print(inv1(a, m) == inv2(a, m))