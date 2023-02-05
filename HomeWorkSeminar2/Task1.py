# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = str(input('Введите число: '))
count = 0
number = number.replace('.', '').replace(',', '')
number = int(number)

while number != 0:
    count += number % 10
    number = number // 10
print(f'Сумма всех цифр числа = {count}')
