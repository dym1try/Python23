# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9

list = ()
n =int(input('Введите n (кол-во кустов): '))# ввод размера списка

list = [int(input()) for i in range(n)]# ввод значений списка

print("Список по отдельным кустам", list)# вывод списка

#list_res = list(range(len(list)))

list_res = [i for i in range(len(list))]

for i in range(1, len(list) - 1):# середина диапазона
    list_res[i] = list[i] + list[i-1] + list[i+1]

list_res[0] = list[0] + list[1] + list[-1]# считаем первый и 
list_res[-1] = list[-2] + list[-1] + list[0]# последний элементы

print("Список по суммам соседних кустов", list_res)# вывод итогового списка
max_number = max(list_res)# находим максимум
print("Наибольшее число ягод:", max_number)
