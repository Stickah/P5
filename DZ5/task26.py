A = int(input('Введите число A: '))
B = int(input('Введите его степень: '))
def recurs(A, B):
    if B == 1:
        return A
    if B != 1:
        return (A * recurs(A, B - 1))
print('Результат возведения в степень равен: ', recurs(A, B))