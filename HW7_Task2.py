import random

def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array)//2
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])
    return merge(left, right)


def merge(left, right):
    res = []
    left_point = right_point = 0
    while left_point < len(left) and right_point < len(right):
        if left[left_point] < right[right_point]:
            res.append(left[left_point])
            left_point += 1
        else:
            res.append(right[right_point])
            right_point += 1
    res.extend(left[left_point:])
    res.extend(right[right_point:])
    return res

N = 5
arr = [random.randint(0, 49) for _ in range(N)]
print(arr)
print(merge_sort(arr))
