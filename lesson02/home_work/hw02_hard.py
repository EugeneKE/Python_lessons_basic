_autor_='Кувалдин Е.А.'
# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
print("задача №1")
equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y
print('y = {}'.format(x * (-12) + 11111140.2121))


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
#date = '01.11.1985'

# ...Примеры некорректных дат
#date = '01.22.1001'
#date = '1.12.1001'
#date = '-2.10.3001'
print('Задача №2')
def yearFiller (start, end):
    ylf = []
    b = ''
    for i in range(start, end):
        if len(str(i)) < 4:
            b = (4 - len(str(i)))*'0' + str(i)
            ylf.append(b)
        else:
            ylf.append((str(i)))
    return ylf
def myFillOuter (start, end):
    mlf = []
    b = ''
    for i in range(start, end + 1):
        if len(str(i)) == 1:
            b = '0' + str(i)
            mlf.append(b)
        else:
            mlf.append(str(i))
    return mlf

myDataRange = myFillOuter(1, 31)
myMonthRange = myFillOuter(1, 12)
myYarRange = yearFiller(1, 9999)

def myChekker(strdata):
    if (strdata[:2] in myDataRange) == True:
        if (strdata[3:5] in myMonthRange) == True:
            if(strdata[6:] in myYarRange) == True:
                print('Дата {} - вправильном формате'.format(strdata))
##Парианты проверки: выводиться будут даты тоолько в правильном формате
Checkdate = '01.11.1985'
myChekker(Checkdate)
myChekker('23.07.1974')




# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

#myTower = {}
#r = 1 # номер комнаты
#myFlore = 1 # номер этажа
#rooms = [] # номера комнат на этаже
#for i in range(1, 100):
#    while myFlore < (myFlore * i):
 #       rooms.append(r)
 #       r += 1
 #   myTower.update({myFlore: rooms})
 #   myFlore +=1




