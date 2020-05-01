import time

#Time at start of execution
start_time = time.time()

for i in range(1,500):
    for j in range(i, 500):
        #print(i,j)
        k = 1000 - i - j
        if k>0 and (i*i+j*j==k*k):
            print(i, j, k, i*j*k)

#time at the end of execution
end_time = time.time()

#Printing the Time taken
print(end_time - start_time)
