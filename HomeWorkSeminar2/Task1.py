# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = input()
count = 0
number = float(number[::-1])
print((number))

while number != 0:
    count += number % 10
    number = number // 10
print(count)
