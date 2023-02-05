# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number = int(input('Введите число: '))
fibonacci = [1, 1]
negofibonacci = [1, -1]
zero = [0]

for i in range(2, number):
    fibonacci.append(fibonacci[i - 2] + fibonacci[i - 1])
    negofibonacci.append(negofibonacci[i - 2] - negofibonacci[i - 1])

negofibonacci.reverse()
print(f'Для K = {number} список будет выглядеть так: {negofibonacci + zero + fibonacci}')

