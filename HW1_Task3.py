x1 = int(input('Введите 1 координату x '))
x2 = int(input('Введите 2 координату x '))
y1 = int(input('Введите 3 координату y '))
y2 = int(input('Введите 3 координату y '))

if x1 == x2:
    print('Деление на ноль!')
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(f'y = {k} x + {b}')
