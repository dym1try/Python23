# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: a(n) = a(1) + (n-1)*d.
# Каждое число вводится с новой строки. 
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

a = int(input("Введите первый элемент прогрессии - число a: "))
d = int(input("Введите шаг прогрессии - число d: "))
n = int(input("Введите количество элементов в прогрессии - число n: "))

list = []# создаем список
a = a - d# уменьшаем первый элемент, чтобы сошлась формула цикла)
for i in range(n):#перебираем все числа 
    a += d
    list.append(a)#добавляем элементы в список
print(list)
