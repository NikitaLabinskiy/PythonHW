# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
import os
def clear(): return os.system('cls')
clear()


def Rle_encoder(data):
    encoding = ''
    previous_symbol = ''
    count = 1
    for current_symbol in data:
        if current_symbol != previous_symbol:
            if previous_symbol:
                encoding += str(count) + previous_symbol 
            count = 1
            previous_symbol = current_symbol
        else:
            count += 1
    else:
        encoding += str(count) + previous_symbol
    return encoding

def Rle_decoder(data):
    decoder = ''
    count = ''
    for symbol in data:
        if symbol.isdigit():
            count += symbol
        else:
            decoder += symbol * int(count)
            count = ''
    return decoder



data = str(input('Введите символы: '))

print(Rle_encoder(data))
print(Rle_decoder(Rle_encoder(data)))
