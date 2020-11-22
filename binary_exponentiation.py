#fastest builtin function
'''
It takes a, b, mod all 3 arguments
'''

pow_is_binpow = pow


# binary exponentiation start
def bin_pow(a, b):
    res = 1
    while b != 0:
        if b & 1:
            res *= a
        a, b = a * a, b >> 1
    return res


# binary exponentiation end

# binary exponentiation with modulo start
def bin_pow_mod(a, b, m):
    res = 1
    while b != 0:
        if b & 1:
            res = res * a % m
        a, b = a * a % m, b >> 1
    return res


# binary exponentiation with modulo end

if __name__ == '__main__':
    print(bin_pow(37, 89) % 17)
    print(bin_pow_mod(37, 89, 17))
    print(pow_is_binpow(37, 89, 17))
