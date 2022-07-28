# 4.Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# нок - наименьшее число, которое делится без остатка на оба заданных числа

def find_the_smallest_common_mult (num1, num2):
    scm = min(num1, num2)
    while True:
        if scm % num1 == 0 and scm % num2 == 0:
            break
        scm = scm + 1
    return scm
print(find_the_smallest_common_mult(9,12))