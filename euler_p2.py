def fibonacci(a):
    """Returns a list of numbers from Fibonacci sequence where the largest value is less than a and returns
    the number of elements needed"""
    fib = [1,1]
    x = 0
    i = 1
    while x < a:
        x = fib [i] + fib[i-1]
        i += 1
        fib.append(x)
    return i, fib

#print(fibonacci(5)[1])

def sum_odd_fib(fib):
    """Given a list of Fibonacci sequence, return the sum of odd numbers"""
    total = 0
    for number in fib:
        if number % 2 == 0:
            total += number
    return total

c = 4000000
print('sum of odd numbers in Fib seq {} is {}' .format(fibonacci(c)[1], sum_odd_fib(fibonacci(c)[1])))
# 4613732