# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод: пара-ра-рам рам-пам-папам па-ра-па-дам
# Вывод: Парам пам-пам
# пара-ра-рам рам-пам-папам па-ра-па-дам Парам пам-пам
import os
def clear(): return os.system('cls')
clear()


# def RythmCheck(text):
#     text = text.lower().split()
#     result = []
#     vowels = set('аиеёоуыэюя')
#     for element in range(len(text)):
#         check_element = str(text[element])
#         count = 0
#         for i in range(len(check_element)):
#             if check_element[i] in vowels:
#                 count += 1
#             else:
#                 continue
#         result.append(count)
#     return result

def RythmCheck(text):
    text = text.lower().split()
    result = []
    vowels = set('аиеёоуыэюя')
    for string in text:
        count = 0
        for element in string:
            if element in vowels:
                count += 1
            else:
                continue
        result.append(count)
    return len(set(result)) == 1

def Main(text):
    if RythmCheck(text):
        print('Парам пам-пам')
    else:
        print('Пам парам')


text = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

print(Main(text))

            

