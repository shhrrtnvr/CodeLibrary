# Euler totient for n start (Number of relative primes to n  upto n)

def phi(n):
    result = n
    for i in range(2, n):
        if i * i > n:
            break
        if n % i == 0:
            while n % i == 0:
                n = n // i
            result -= result // i
    if n > 1:
        result -= result // n
    return result


# Euleer totient for n end

# Euler totient for all numbers in range(1, n) start

def phi_1_to_n(n):
    phi = [i for i in range(0, n + 1)]
    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    return phi


# Euler totient for all numbers in range(1, n) end
if __name__ == '__main__':
    n = int(input())
    res = phi_1_to_n(n)
    for i in range(1, n):
        if res[i] != phi(i):
            break
    else:
        print("Output Matched")
