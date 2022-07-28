# Задана натуральная степень n. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени n. 
# *Пример: n=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
n = int(input('введите степень: '))
my_list = [random.randint(0,100) for _ in range(n+1)]
print (my_list)

result = []
i = 0
stepen = len(my_list)-1
for elem in my_list:
    if elem !=0 and elem !=1:
        result.append(str(elem) + '*x^' + str(stepen))
    elif elem == 1:
        result.append('x^'+str(stepen))
    stepen = stepen -1

result[-1] = result[-1][:-4]
if result[-2][0].isdigit():
    result[-2] = result[-2][:-2]
else:
    result[-2] = result[-2][:-2]
s = '+'.join(result) + '=0'
print(s)