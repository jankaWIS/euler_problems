number = [1, 2, 3, 4, 5]


# for i in number:
#     l = number[i]*number[i+1]
#     la = i*(i+1)
#     print(l, la)

def max_product(number):
    maxim = 0
    for i in number:
        if i+3 <= len(number):
            tmp = i*(i+1)*(i+2)*(i+3)
        else:
            break

        if tmp > maxim:
            maxim = tmp
    return maxim


print(max_product(number))

# solution
s = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"


#Time module for counting time
import time

#Time at start of execution
start_time = time.time()

def product(s, k):
    """ takes a number in string format, computes the product of elements with a sliding window of size k and returns the maximum of those"""
    max = 0
    tmp = 1
    for i in range(0, len(s)-k):
        for j in range(i, i+k):
            tmp *= int(s[j])
        if tmp > max:
            max = tmp
        tmp = 1 # reset the temporal counter
    return max

print('result', product(s, 13))

# define the same nicer

def productN(s,k):
    max = 0
    for i in range(0, len(s)-k):
        tmp = 1
        for j in range(i, i+k):
            tmp *= inst(s[j])
        if tmp > max:
            max = tmp
    return max


#time at the end of execution
end_time = time.time()

#Printing the Time taken
print(end_time - start_time)