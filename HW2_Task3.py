"""
Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
def reverse_num(n):
    num = 0
    while n > 0:
        num = num * 10 + n % 10
        n //= 10
    return num
"""


def reverse_num(n):
    num = 0
    if n > 0:
        num = num * 10 + n % 10
        n //= 10
        return str(num) + str(reverse_num(n))
    else:
        return ''


print(reverse_num(int(input('Введите число '))))
