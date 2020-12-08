#Во втором массиве сохранить индексы четных элементов первого массива.

from random import random

N = 10
arr = []
a = []

for i in range(N):
    arr.append(int(random() * 100))
    if arr[i] % 2 == 0:
        a.append(i)

print(arr)
print(a)
