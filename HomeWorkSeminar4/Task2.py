# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

number = int(input('Введите число: '))
number_clone = number
digit = int(2)
result = []
while number > 1:
    if number == 1:
        continue
    if number % digit == 0:
        number /= digit
        result.append(digit)
        digit = 2
    else: 
        digit += 1
print(f'Простые множители числа [{number_clone}] = {result}')
