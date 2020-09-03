import time


# Library starts

def sieve(n):
    primes, is_prime = [2], [True] * (n >> 1)
    for i in range(3, n, 2):
        cover = i * i
        if cover > n:
            for j in range(i, n, 2):
                if is_prime[j >> 1]:
                    primes.append(j)
            break
        elif is_prime[i >> 1]:
            primes.append(i)
            jump = i << 1
            for j in range(cover, n, jump):
                is_prime[j >> 1] = False
    return primes


# Library ends

if __name__ == '__main__':
    start = time.time()
    primes = sieve(100)
    end = time.time()
    print(end - start)
    print(' '.join(map(str, primes)))
    print(len(primes))
