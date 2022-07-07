#2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#   Примеры:
#    - 1, 4, 8, 7, 5 -> 8
#   - 78, 55, 36, 90, 2 -> 90

import random
lst = []
for i in range(5):
    lst.append(random.randint(1,100))
print(lst)

max = lst[0]
for item in range(5):
    if max < item:
        max = item

print (f'максимальное число равно {max}')