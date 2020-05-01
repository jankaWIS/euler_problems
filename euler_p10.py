def primes(n):
    i = 2
    while i*i <= n:
        if (n % i) == 0:
            break
        else:
            print(i)
        i += 1


def primes2(n):
    primes = []
    suma = 0
    for num in range(2, n + 1):
        # prime numbers are greater than 1

        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            #print(num)
            suma += suma
            primes.append(num)
    return primes, suma

#print(primes(5))
#print(primes2(2000000))
#print(primes2(2000000))

# https://stackoverflow.com/questions/509211/understanding-slice-notation
#https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n

import time

start = time.time() #setting timer

def primes3(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    #sum = 2
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]
    #return sum

end = time.time() #setting timer
l = primes3(2000000)
print(len(primes3(20000000)), 'time', end-start)
#print(l[:50])

