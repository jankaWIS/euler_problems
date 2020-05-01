import numpy as np
import sympy
import math


def get_divisors(n, dic, primes):
    if n in primes:
        # dic['n']=[n, 1]
        dic = [n, 1]
    else:
        for p in primes:
            if n % p == 0:
                # dic['n']=[p,dic[str(n//p)]]
                if n % p ** 2 == 0:
                    dic = [n] + dic[str(n // p)]

                    # check for powers of primes, if it is, do no add them
                    if n != p ** int(math.log(n, p)):

                        # add higher powers of primes, get the maximal power using log of base prime
                        # but adds 24 since I add 12 and 4,8 %TODO -- only add the powers above max in divisitors
                        # now fixed by taking unique
                        for power in range(2, math.floor(math.log(n, p))):
                            if n % p ** power == 0:
                                dic += [p ** power]

                else:  # not a power of a prime
                    dic = [n] + dic[str(n // p)] + [p]
                break
    # return list(set(dic)) # return only unique values
    # https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
    return sorted([*{*dic}])


def triangle(n):
    return np.arange(1, n + 1).sum()


len_div = 0
lower = 2
upper = 50
triangle_numbers = [triangle(1)]

# Get list of primes in given range
primes = list(sympy.primerange(0, upper))
# https://stackoverflow.com/questions/13326673/is-there-a-python-library-to-list-primes

# Crete a dictionary of divisors
divisors = {}
divisors['1'] = [1]

# for i in range(2,m+1):
#     divisors[str(i)]=get_divisors(i, divisors, primes)

# print(divisors)

while len_div < 50:  # 00:
    """
    This part is here so that I do not have to rerun everything if I do not find my result.
    I generate all the primes and factors of all the numbers, then triangle number within this range
    and if the number of the divisors of the given triangle number does not reach my threshold, I increase
    the range. I stop when I find it.
    """

    for i in range(lower, upper + 1):
        divisors[str(i)] = get_divisors(i, divisors, primes)
        # just to make sure I don't have too many triangle numbers
        # I check if the newly added triangle number is within my searching range (where I have divisors),
        # if yes, I add it
        if triangle(len(triangle_numbers) + 1) < upper - 1:
            triangle_numbers.append(triangle(len(triangle_numbers) + 1))
    for t in triangle_numbers:
        len_div = len(divisors[str(t)])

        if len_div == 50:
            print('Triangle number with {} divisitors is {}'.format(len_div, t))
            break
    # Change the boundaries
    lower = upper + 1
    upper += upper
    # Add missing primes from the new range
    primes += list(sympy.primerange(lower, upper))
