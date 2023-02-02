# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
n = int(input())
sum = 0
spisok = []
for i in range(1, n + 1):
    sum += (1+(1 / i))**i
    spisok.append((1+(1 / i))**i)
print(sum)
print(spisok)
