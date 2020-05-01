import numpy as np

x ='''
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
'''

arr = np.array(list((x.split())), dtype = int)
arr = arr.reshape(20,20)
res = 0
for i in range(17):
    for j in range(17):
        temp=max(arr[i,j:j+4].prod(), arr[i:i+4,j].prod(),
                 arr[[i,i+1,i+2,i+3],[j,j+1,j+2,j+3]].prod(),
                 arr[[i+3,i+2,i+1,i],[j,j+1,j+2,j+3]].prod())
        if temp>res:
            res=temp
print(res)


## Sol 2
I, J = arr.shape
S, T = arr.strides

horz = np.lib.stride_tricks.as_strided(arr, (I, J-3, 4), (S, T, T)).prod(axis=2)
vert = np.lib.stride_tricks.as_strided(arr, (I-3, J, 4), (S, T, S)).prod(axis=2)
tlbr = np.lib.stride_tricks.as_strided(arr, (I-3, J-3, 4), (S, T, S+T)).prod(axis=2)
bltr = np.lib.stride_tricks.as_strided(arr[3:], (I-3, J-3, 4), (S, T, -S+T)).prod(axis=2)

all_ = horz, vert, tlbr, bltr

midx = [np.unravel_index(o.argmax(), o.shape) for o in all_]
mval = [o[idx] for o, idx in zip(all_, midx)]

hy, hx, vy, vx, ty, tx, by, bx = np.ravel(midx)
a = np.arange(4)
idx = list(map(tuple, np.reshape(np.s_[hy, hx:hx+4, vy:vy+4, vx, ty+a, tx+a, by+a[::-1], bx+a], (4, 2))))

for name, I, V in zip('horizontal vertical topleft-bottomright bottomleft-topright'.split(), idx, mval):
    print('best', name, ':', V, '=', ' x '.join(map(str, arr[I])))



## Sol 3
#data = pd.read_clipboard(header=None).values # read the tray
data = np.copy(arr)
m,n = data.shape
blocksize = 4

arr = np.zeros((m+blocksize,n+1),int) #pad with the right amount of zeros.
arr[:m,:n] = data
flat = arr.ravel()
usefulsize = data.size + m  # indice of last non zero value + 1

shifts = [1,n,n+1,n+2] # - / | \ , the four directions
blocks = np.array([[flat[i*s:][:usefulsize] for s in shifts] \
                                            for i in range(blocksize)]) #15µs
scores=blocks.prod(axis=0) #8µs

print(scores.max())
i,j = np.where(scores==scores.max())
print(blocks[:,i,j])
#
# 70600674
# [[89][94][97][87]]
