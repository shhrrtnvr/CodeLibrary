from functools import *
import sys
sys.setrecursionlimit(10**9)

@cache                      #for version >= 3.8
def fact(n):
    return n*fact(n-1) if n else 1

@lru_cache(maxsize=None)    #to get same effect as cache in lower version
def comb(n, r):
    if n == r or r == 0:
        return 1
    return comb(n-1, r-1) + comb(n-1, r) 

print(comb(10, 5))

base2 = partial(int, base=2)   #partial funtion
print(base2('100'))

import operator
multi = reduce(operator.mul, range(1, 10))
print(multi)

