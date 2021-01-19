#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import random

N = 10
arr = []
for i in range(N):
    arr.append(int(random() * 100) - 50)
print(*arr)

max_ind = 0
min_ind = 0

for i in range(N):
    if arr[i] > arr[max_ind]:
        max_ind = i
    elif arr[i] < arr[min_ind]:
        min_ind = i
    i += 1

print(arr[max_ind], arr[min_ind])

arr[max_ind], arr[min_ind] = arr[min_ind], arr[max_ind]
for i in range(N):
    print(arr[i], end=' ')
