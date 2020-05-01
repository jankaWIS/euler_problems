import time
t0 = time.time()

a = 0
b = 0
for i in range(1,101):
    a += i
    b += i**2

x = a**2 - b

t1 =time.time()
perf = t1 - t0
print("Problem 6\nAnswer:", x, "runtime:", perf, "seconds")

## cool and short
r = range(1, 101)
print(sum(r) ** 2 - sum(x ** 2 for x in r))