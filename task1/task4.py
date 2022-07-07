# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
#     *Примеры:*
#     - 6,78 -> 7
#     - 5 -> нет
#    - 0,34 -> 3

number = float(input('enter number: '))
if number - int(number) == 0: print('no')

else:
    answer = number * 10 % 10
    print(int(answer))

