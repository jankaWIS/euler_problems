def reverse(a):
    a = str(a) # convert into string to be able to reverse and compare
    x = a[::-1] # create a reverse by using indexing
    if x == a: #are palindromic
        return True
    else:
        return False

# we're looking for the biggest, start from 999 and go down
max = 0
for i in range(999,99,-1):
    for j in range(999,99,-1):
        if reverse(i*j):
            if i*j > max: # without this it would print all of them
                max = i*j
                print(i, j, i*j)
