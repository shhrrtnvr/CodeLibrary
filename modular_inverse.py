# using extended gcd start
def inv1(a, mod):
    def gcd(a, b):
        if b == 0:
            return a, 1, 0
        g, x, y = gcd(b, a % b)
        return g, y, x - y * (a // b)

    g, x, y = gcd(a, mod)
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

#using builtin pow instead of custom binary exponentiation
def inv3(a, mod):
    return pow(a, mod-2, mod)

if __name__ == '__main__':
    a, m = 13, 11
    print(inv1(a, m) == inv3(a, m) and inv2(a, m) == inv3(a, m))