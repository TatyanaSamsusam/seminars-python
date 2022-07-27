# 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке некое число.

import random

list_of_nums = []
for i in range (1, 20):
    list_of_nums.append(random.randint(1,10))

look_up_number = int(input('enter number to look up: '))

def find_no_in_list (some_list, some_no):
    for i in some_list:
        if i == some_no:
            result = str(some_no) + ' is in list'
            break
        else: 
            result = str(some_no) + ' is not in list'
    return result

print(list_of_nums)
print (find_no_in_list(list_of_nums, look_up_number))


# второй вариант решения:
# my_list = ['2', '1e3', 'er3', '211']
# find_no = 3

# def find_number_pos_in_list(some_list: list, some_no: int):
#     for char in some_list:
#         for symbol in char:
#             if symbol == str(some_no):
#                 return some_list.index(char)
#     return -1

# pos_number = find_number_pos_in_list(my_list, find_no)
# if pos_number != -1:
#     print(pos_number)
# else: print('there is no such number in list')