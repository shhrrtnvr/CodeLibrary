from itertools import *
#all functions always returns iterator and takes any iterables

c = count(1)  #counter starts from 1

c = cycle([1, 2, 3]) #cycles through the iterable

r = repeat(10, 3) #repeats 10 3times

chained = chain('abc', [1, 2, 3], ['abc', 'def']) #chains all the values from iterables a b c 1 2 3 abc def

chained = chain.from_iterable(['abc', 'def']) # chains a b c d e f

filtered = filter(lambda x : x%2 == 0, range(1, 10)) # fitlers even numbers from range(1, 10)

filtered = filterfalse(lambda x: x%2==0, range(1, 10))  #filters the numbers that are not even

taken = dropwhile(lambda x: x%5 != 0, range(1, 10)) # drops until divisible by 5

taken = takewhile(lambda x: x%5 != 0, range(1, 10)) #takes until divisible by 5

selected = compress([1, 2, 3], [0, 1, 0]) #takes only the values for which 2nd list corresponding element is 1

prefix_sum = accumulate(range(1, 10), lambda a, b: a+b) # prefix sum, for final value use functools.reduce(fn, iterable)

it = islice([1, 2, 5], 1, None, None)  # iterative slice args = list, start_idx, end_idx, step

res = starmap(pow, [(2, 3), ( 4, 5)])  # maps elements by spreading

zipped = zip_longest(range(5), 'ACB', fillvalue='-')

a, b, c = tee(it, 3) #creates 3 independent copies of it

prod = product([1, 2, 3], repeat =  2)  #cartesian product

perm = permutations([1, 2, 3], 2) #nP2

comb = combinations([1, 2, 3], 2) #nC2

combr = combinations_with_replacement([1, 2, 3], 2) #self documentary
