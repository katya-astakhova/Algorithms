#Определить, какое число в массиве встречается чаще всего.

from random import random

N = 10
arr = []

for i in range(N):
    arr.append(int(random() * 10))
print(arr)

freq_max = 0
for i in range(N - 1):
    freq = 1
    for j in range(i + 1, N):
        if arr[i] == arr[j]:
            freq += 1
    if freq > freq_max:
        freq_max = freq
print(freq_max)
