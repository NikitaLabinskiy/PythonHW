# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
import os
def clear(): return os.system('cls')
clear()


def DeleetTheWords(text):
    find = 'абв'
    new_text = text.lower().split()
    result_text = list(filter(lambda i: find not in i, new_text))
    return result_text


text = input('Введите текст: ')
filtered_text = ' '.join(DeleetTheWords(text))
print(filtered_text.capitalize())

