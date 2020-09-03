import time


def linear_sieve(N):
    lp, primes = [0] * N, []
    for i in range(2, N):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
        for prime in primes:
            x = i * prime
            if prime > lp[i] or x >= N:
                break
            lp[x] = prime
    return primes


if __name__ == '__main__':
    start = time.time()
    primes = linear_sieve(100000000)
    end = time.time()
    print(end - start)
#    print(' '.join(map(lambda x: str(x), primes)))
    print(len(primes))
