# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81

numberN = int(input('enterN: '))
list = []
list.append(1)

for i in range(0, numberN-1):
    list.append(list[i] * -3)

print(list)