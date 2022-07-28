# 2. Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию. 
# (не использовать sort и sorted)
import random
from random import randint

list_of_nums = []
for i in range (1, 20):
    list_of_nums.append(random.randint(1,10))

with open('text2.txt', mode = 'w') as file:            # каждый раз записывает новые рандомные индексы в файл text.txt
    for i in list_of_nums:
        file.write(f"{i}\n")
file.close()

with open('text2.txt', mode = 'r') as file:
    data = file.read()

list_of_rows = data.split()
for i in range(0, len(list_of_rows)):
    list_of_rows[i] = int(list_of_rows[i])

def sort_the_list(some_list):
    for i in range(0, len(some_list)):
        for j in range(i+1, len(some_list)):
            if some_list[j] < some_list[i]:
                some_list[j], some_list[i] = some_list[i], some_list[j]
print(list_of_nums)
sort_the_list(list_of_rows)
print(list_of_rows)
