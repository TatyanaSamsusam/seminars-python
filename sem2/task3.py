# 3. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

str1 = 'Говорит попугай попугаю: "Я тебя, попугай, попугаю". Отвечает ему попугай:". Попугай, попугай, попугай!'
str2 = 'попуг' 
count = 0

for i in range(0,len(str1)-len(str2)):
    if str2.lower() == str1[i : i + len (str2)].lower():
        count = count + 1

print(f'{count} вхождений')