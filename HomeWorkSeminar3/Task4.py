# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input())
number1 = number
result = ''
while number >= 1:
    if number % 2 == 0:
        result += '0'
    else:
        result += '1'
    number //= 2
print(f'Число: {number1} в двоичной системе = {result[::-1]}')
