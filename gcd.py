# for gcd only use math.gcd(a, b)
# for extended gcd use following

# only needed if negative exists !!!EDIT line 18 and add _!!!
def gcd(a, b):
    if b < 0:
        g, y, x = _gcd(b, a)
        return g, x, y
    return _gcd(a, b)


# only needed ends

# extended gcd start
def _gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = gcd(b, a % b)
    return g, y, x - y * (a // b)


# extended gcd ends


if __name__ == '__main__':
    while True:
        try:
            print(gcd(*map(int, input('Enter a and b: ').rstrip().split())))
        except:
            quit()
