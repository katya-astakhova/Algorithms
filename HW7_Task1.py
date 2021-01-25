import random


def bubble_sort(arr):

    for i in range(N-1):
        for j in range(N-i-1):
            if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

N = 10
MIN_ITEM = -100
array = [random.randint(MIN_ITEM, 99) for _ in range(N)]
print(array)
print(bubble_sort(array))
