def ismultiple(a):
    if (a % 3 == 0 or a % 5 == 0):
        return a
total = 0
x = []
for i in range(0,1001):
#    print(ismultiple3(i))
    x.append(i)
    if ismultiple(i) != None:
        total +=i

 print(total)
#print(total, x.sum())