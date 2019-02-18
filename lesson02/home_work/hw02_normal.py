_autor_='Кувалдин Е.А.'
import random
import math
import datetime
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
print('Задача №1')
my_random_list =[]
my_results_list =[]
for i in range(0, 20):
    my_random_list.append(random.randrange(1, 100))
print('Исходный список {}'.format(my_random_list))
for t in range(0, len(my_random_list)-1):
    if math.modf(math.sqrt(my_random_list[t]))[0] == 0:
        my_results_list.append(math.ceil(math.sqrt(my_random_list[t])))
print('Итоговый список {}'.format(my_results_list))

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
print('Задача №2')
myData = '02.11.2013'
myDataDict = {'01': "первое",'02': "второе", '03': "третье"}
myDataMonth = {'11': 'норября', '12': 'декабря'}
myDataYar = {'2013': 'две тыясячи тринадцатый'}
dataofData = myData[:2]
monthofData = myData[3:5]
yearofData = myData[-4:]
if (dataofData in myDataDict) == True:
    if (monthofData in myDataMonth) == True:
        if (yearofData in myDataYar) == True:
                print('{} {} {} год'.format(myDataDict[dataofData], myDataMonth[monthofData], myDataYar[yearofData]))

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
print('Задача №3')
myNumbers = []
n = 20
for i in range(n):
    myNumbers.append(random.randint(-100, 100))
print(myNumbers)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
print('Задача №4')
a = []
for i in range(10):
    a.append(random.randint(0, 10))
print('Исходный список {}'.format(a))

new =[]
s = 0
for t in range(0, len(a)):
    for y in range(0, len(a)):
        if a[y] == a[t]:
            s += 1
    if s == 1:
        new.append(a[t])
    s = 0
print('Результат {}'.format(new))

