#Посчитать четные и нечетные цифры введенного натурального числа.


def count_num(n):
    even = odd = 0
    while n != 0:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
        n //= 10
    print(f' {even} : {odd}')


print(count_num(int(input('Введите число '))))
