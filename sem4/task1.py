# 1. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

n = int(input("введите число n: "))
def list_length_n(n:int = 0,some_list: list = []):
    for i in range(n):
        some_list.append(randint(-n,n))
    print(some_list)
    return some_list
made_random_list = list_length_n(n,)

with open('text.txt', mode = 'w') as file:            # каждый раз записывает новые рандомные индексы в файл text.txt
    for k in range(0,5):
        file.write(f"\n{randint(0, len(made_random_list)-1)}")
    
with open('text.txt', mode = 'r') as file:
    res = 1
    some_list_index = []
    for line in file.read():
        if line.isdigit():
           res *= made_random_list[int(line)] 
           some_list_index.append(line)
print(f"{some_list_index=}")           
print(f"{made_random_list=}")
print(res)
