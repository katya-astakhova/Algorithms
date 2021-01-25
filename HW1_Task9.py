a = int(input('Введите 1 число '))
b = int(input('Введите 2 число '))
c = int(input('Введите 3 число '))

if ((a > b) and (a < c)) or ((a < b) and (a > c)):
    print(a)
else:
    if ((b > a) and (b < c)) or ((b < a) and (b > c)):
        print(b)
    else:
        print(c)
