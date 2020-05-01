def fibonacci(a):
    i = 1
    fib = [1,1]
    while (fib[i] + fib[i-1]) < a:
        fib.append((fib[i] + fib[i-1]))
        i += 1
    return i, fib

#print(fibonacci(15))

total_even = 0
total_odd = 0
c = 4000000

print(fibonacci(c))

for i in fibonacci(c)[1]:
    if i % 2 == 0:
        #print(i)
        total_even += i
    else:
        total_odd += i

print('total even {}, total odd {}' .format(total_even, total_odd))