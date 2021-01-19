#HW3 Task3 Во втором массиве сохранить индексы четных элементов первого массива.
import timeit
import cProfile


def func(N):
    import random

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
    return freq_max, num

def func_2(N):
    import random

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
    return num, frequency

def func_3(N):
    import random

    MIN_ITEM = 0
    a = [random.randint(MIN_ITEM, N // 1.5) for _ in range(N)]
    b = max(zip((a.count(item) for item in set(a)), set(a)))
    return b

'''
Данная функция работает медленнее всего, при увеличении значения в 2 раза, 
время выполнения увеличивается в 4 раза.
'''
'''
print(timeit.timeit('func(150)', number = 100, globals = globals()))
print(timeit.timeit('func(300)', number = 100, globals = globals()))
print(timeit.timeit('func(600)', number = 100, globals = globals()))
print(timeit.timeit('func(1200)', number = 100, globals = globals()))
print(timeit.timeit('func(2400)', number = 100, globals = globals()))
print(timeit.timeit('func(4800)', number = 100, globals = globals()))
cProfile.run('func(1500)')
cProfile.run('func(3000)')
cProfile.run('func(6000)')
'''
'''
Самая быстрая функция. При увеличении значения в 2 раза, 
время выполнения увеличивается в 2 раза.
'''
print(timeit.timeit('func_2(150)', number = 100, globals = globals()))
print(timeit.timeit('func_2(300)', number = 100, globals = globals()))
print(timeit.timeit('func_2(600)', number = 100, globals = globals()))
print(timeit.timeit('func_2(1200)', number = 100, globals = globals()))
print(timeit.timeit('func_2(2400)', number = 100, globals = globals()))
cProfile.run('func_2(1500)')
cProfile.run('func_2(3000)')
cProfile.run('func_2(6000)')

'''
Самая быстрая функция. При увеличении значения в 2 раза, 
время выполнения увеличивается в 3 раза.
'''
print(timeit.timeit('func_3(150)', number = 100, globals = globals()))
print(timeit.timeit('func_3(300)', number = 100, globals = globals()))
print(timeit.timeit('func_3(600)', number = 100, globals = globals()))
print(timeit.timeit('func_3(1200)', number = 100, globals = globals()))
print(timeit.timeit('func_3(2400)', number = 100, globals = globals()))
cProfile.run('func_3(1500)')
cProfile.run('func_3(3000)')
cProfile.run('func_3(6000)')

'''
Все три функции имеют линейную сложность с различным коэффициентом k.
Самая медленная первая функция, так как имеется вложенный цикл,
третья работает медленее второй, из-за функции count, которая вызывается в среднем n/2 раз.
'''
