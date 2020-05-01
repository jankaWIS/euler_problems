def primes(a):
    prim = []
    i = 2
    while i **2 <= a:
        if a % i != 0:
            i += 1
        else:
            prim.append(i)
            while a % i == 0:
                a //= i

    prim.append(a)
    return prim

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
            print('non divisible ', i)
        else:
            n //= i
            print(n,i)
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


#a = 600851475143
a = 10
print('primes of {} are {} and the maximal is {}' .format(a, prime_factors(a) , max(primes(a))))