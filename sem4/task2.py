# 2. Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию. 
# (не использовать sort и sorted)

from random import randint

with open('text2.txt', mode = 'w') as file:            # каждый раз записывает новые рандомные индексы в файл text.txt
    for i in range(10):
        file.write(f"\n{randint(0, 10)}")

with open('text2.txt', mode = 'r') as file:
