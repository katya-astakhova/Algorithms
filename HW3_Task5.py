#В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

from random import random

N = 10
arr = []
i = 0
ind = -1

for i in range(N):
    arr.append(int(random() * 100) - 50)
    if arr[i] < 0 and ind == -1:
        ind = i
    elif 0 > arr[i] > arr[ind]:
        ind = i
    i += 1

print(arr)
print(f'Максимальный отрицательный элемент {arr[ind]} находится на позиции {ind + 1} ')
