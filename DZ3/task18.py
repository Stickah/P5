from random import randint
N=int(input("Введите N: "))
int_array = [randint(-N // 2, N // 2 + 1) for i in range(N)]
print(f"Массив случайных {N} целых чисел от {-N // 2} до {N // 2}")
print(int_array)

X=int(input("Введите X: "))
distance = {abs(X-num) for num in int_array}
min_distance = min(distance)
numbers = {num for num in int_array if abs(X-num) == min_distance}
print(numbers)
