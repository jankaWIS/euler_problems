import time
t0 = time.time()

def maxPower(x, b):
    """returns the maximal power of b such that b^n < x"""
    n = 0 # the power
    i = b # needed to be able to not change the base while wanting b^n <= x
#    while x % b == 0: #returns the maximal power if it is divisible
        #n +=1
        #x /= b
    while i <= x:
        n += 1
        i = b**n
    # We need the power where b^n does not exceed x
    if i <= x:
        return n
    else:
        return n-1

#print(maxPower(8,2))

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

#prime(6)

def smallestNumber(a):
    """goes over all primes less than a, then checks in which power they are in a
     eventually returns the smallest number which is divisible by all numbers <= a"""
    max = 1
    for i in prime(a):
        max = max * (i ** maxPower(a, i))
        print('i ', i, ' in power of ', maxPower(a,i), ' max ', max)

    return max

print(smallestNumber(20))

t1 =time.time()
perf = t1 - t0
    print("Problem 5\nAnswer:", smallestNumber(20), "runtime:", perf, "seconds")

# # Brute force algorithm
# def ifDividesAll(num):
#     for i in range(2, 21):
#         if num % i != 0:
#             return False
#     return True
#
# num = 20
# while True:
#   if ifDividesAll(num):
#     break
#   else:
#     num = num + 1
# print('brute force', num)

#https://stackoverflow.com/questions/8024911/project-euler-5-in-python-how-can-i-optimize-my-solution