#Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
import random
import sys


def count_var(l):
    sum_size = 0
    for k in range(len(l)):
        sum_size += sys.getsizeof(l[k])
    return sum_size


def func(N):

    MIN_ITEM = 0
    arr = [random.randint(MIN_ITEM, N // 1.5) for _ in range(N)]

    num = arr[0]
    freq_max = 0
    for i in range(N - 1):
        freq = 1
        for j in range(i + 1, N):
            if arr[i] == arr[j]:
                freq += 1
        if freq > freq_max:
            freq_max = freq
            num = arr[i]
    L = [N, MIN_ITEM, arr, num, freq_max, i, freq, j]

    return count_var(L)


def func_2(N):

    MIN_ITEM = 0
    array = [random.randint(MIN_ITEM, N // 1.5) for _ in range(N)]

    counter = {}
    frequency = 1
    num = None
    for item in array:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
        if counter[item] > frequency:
            frequency = counter[item]
            num = item
    L = [N, MIN_ITEM, array, counter, frequency, num, item]
    return count_var(L)


def func_3(N):
    b = []
    MIN_ITEM = 0
    a = [random.randint(MIN_ITEM, N // 1.5) for _ in range(N)]
    for item in set(a):
        a.count(item)
        b.append(a.count(item))
    b = max(zip((b), set(a)))
    L = [N, MIN_ITEM, a, b, item]
    return count_var(L)

N = 10
print(f'Под переменные выделено {func(N)}')
print(f'Под переменные выделено {func_2(N)}')
print(f'Под переменные выделено {func_3(N)}')
#Под переменные выделено 188
#Под переменные выделено 354
#Под переменные выделено 160
#Python 3.6.6 - 32-bit
#Windows 7 - 64-bit

#Вывод: меньше всего памяти выделено в 3-ей функции, т.к. там наименьшее количество переменных.
#И хотя во 2-ой функции переменных меньше, чем в 1-ой, там присутствует словарь, под который выделяется больше памяти,
# чем под список из-за того, что словарь имеет структуру {key : value, ...}