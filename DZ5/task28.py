def sum_numbers(max1, min1):
    if min1 > 0:
        max1 = sum_numbers(max1 + 1, min1 - 1)
    return max1


a1 = int(input('Введите первое число: '))
b1 = int(input('Введите второе число: '))

print('Сумма чисел =', sum_numbers(max(a1, b1), min(a1, b1)))