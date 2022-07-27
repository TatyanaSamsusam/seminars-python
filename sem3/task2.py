# 2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# ['a', 'a','b'] -> 'a' по индексу 1

my_list = ['21', '1', 'er', '21']
number_to_find = 21
count_of_appearance = 2

def find_in_list (some_list, some_no, some_count):
    for i in range(0, len(some_list)):
        if some_list[i] == str(some_no):
            some_count = some_count - 1
        if some_count == 0:
            return i
    return -1

position_number = find_in_list(my_list, number_to_find, count_of_appearance)
if position_number != -1:
    print(f'second appearance is under index {position_number}')
else: print('there is no second appearance')


# my_list = ['green', 'red', 'blue', 'yellow', 'yellow', 'yellow', 'blue']
# def find_second_enter (some_list):
#     index = 0
#     for i in some_list:
#         index = index + 1
#         second_index = index
#         for j in (some_list[index:]):
#             #print(i,j)
#             if i == j:
#                 result = str(i) + ' appears second time under index ' + str(second_index)
#                 break
#             else: 
#                 result = ' there is no second appear'
#             second_index = second_index + 1
#         if result != ' there is no second appear':
#             break
#     return result

# print(my_list)
# print(find_second_enter(my_list))

