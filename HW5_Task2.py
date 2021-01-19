#Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]


from collections import defaultdict
from collections import deque


def dec(n_hex):
    d_q = deque()
    for ch in n_hex:
        d_q.append(int(ddict[ch]))
    det = 0
    for i in range(0, len(d_q)):
        det += d_q[i] * 16 ** (len(d_q) - i - 1)
    return det


def hex(ex):
    numb = deque()
    while ex > 0:
        ost = ex % 16
        ex //= 16
        for i in ddict:
            if ost == ddict[i]:
                numb.appendleft(i)
    return numb


sentence = "0123456789ABCDEF"
k = 0
ddict = defaultdict(int)
for el in sentence:
    ddict[el] = k
    k += 1


number_1 = dec(input("Введите первое шестнадцатеричное число ").upper())
number_2 = dec(input("Введите первое шестнадцатеричное число ").upper())

print(*hex(number_1 + number_2), sep='')
print(*hex(number_1 * number_2), sep='')
