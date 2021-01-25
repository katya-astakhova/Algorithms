#Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
# (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

lst = []
ch_final = []
n = int(input("Введите количество предприятий "))
avg_all = 0
for i in range(0, n):
    name = input("Введите название предприятия ")
    income = input("Введите прибыль за 4 квартала через пробел ").split(' ')
    lst.append(name)
    ch_int = [int(el) for el in income]
    ch = sum(ch_int)
    avg_all += sum(ch_int)
    ch_final.append(ch)

below = []
above = []
Comp = namedtuple('Comp', lst)
comp = Comp(*ch_final)

print(f'Средняя выручка всех предприятий равна {avg_all/n:.2f}')

for i in range(0, n):
    if comp[i] < avg_all/n:
        below.append(lst[i])
    elif comp[i] > avg_all/n:
        above.append(lst[i])

if len(below) != 0:
    print('Предприятия с выручкой ниже среднего:', *below)
elif len(above) != 0:
    print('Предприятия с выручкой выше среднего:', *above)
else:
    print('У всех одинаковая прибыль')
