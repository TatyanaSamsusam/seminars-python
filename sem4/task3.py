# 3.Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

my_list = list(map(int, input('enter numbers: ').split()))
print(my_list)

def find_max_and_min(some_list: list): 
    max_num = my_list[0]
    min_num = my_list[0]
    for number in some_list:
        max_num = max(my_list)
        min_num = min(my_list)
    return max_num, min_num

print(find_max_and_min(my_list))