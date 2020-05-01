def prime(a):
    """ returns list of prime numbers less than a"""
    primes = []
    for val in range(1, a + 1):
        # If num is divisible by any number between 2 and val, it is not prime
        if val > 1:
            for n in range(2, val):
                if (val % n) == 0:
                    break
            else:
                primes.append(val)

    return primes

def upper_bound_for_p_n(n):
    if n < 6:
        return 100
    return ceil(n * (log(n) + log(log(n)))) #horni mez

primes = []
a = 10001
while len(primes) < 10001:
    for val in range(1, a + 1):
        # If num is divisible by any number between 2 and val, it is not prime
        if val > 1:
            for n in range(2, val):
                if (val % n) == 0:
                    break
            else:
                primes.append(val)
        a += 100

print(primes[10001])
#90641