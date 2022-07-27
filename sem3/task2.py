# 2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# ['a', 'a','b'] -> 'a' по индексу 1

my_list = ['2', '1e3', 'er3', '211']
find_no = 3

def find_number_pos_in_list(some_list: list, some_no: int):
    for char in some_list:
        for symbol in char:
            if symbol == str(some_no):
                return some_list.index(char)
    return -1

pos_number = find_number_pos_in_list(my_list, find_no)
if pos_number != -1:
    print(pos_number)
else: print('there is no such number in list')

