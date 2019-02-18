_autor_='Кувалдин Е.А.'
import random
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

my_fruits = ["яблоко", "банан", "киви", "арбуз"]
i = 0
while i < len(my_fruits):
    print("{}.{}".format((i+1), my_fruits[i]))
    i += 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

print('Задача №2')
my_list_first = [1, 2, 3, 4, 5, 6, 9]
my_list_second = [1, 100, 5, 200]
print('Было: my_list_first {}, my_list_second {}'.format(my_list_first, my_list_second))
for t in range(0, len(my_list_second)-1):
    for i in range(0, len(my_list_first)-1):
        if my_list_first[i] == my_list_second[t]:
            my_list_first.pop(i)
print('Стало после удаления: my_list_first {}, my_list_second {}'.format(my_list_first, my_list_second))

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print('Задача №3')
my_random_list =[]
my_results_list =[]
for i in range(0, 20):
    my_random_list.append(random.randrange(1, 100))
print('Исходный список {}'.format(my_random_list))
for t in range(0, len(my_random_list)-1):
    if (my_random_list[t] % 2) == 0:
        my_random_list[t] = my_random_list[t]/4
    else:
        my_random_list[t] = my_random_list[t]*2
my_results_list = my_random_list
print('Итоговый список {}'.format(my_results_list))
