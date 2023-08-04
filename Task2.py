from random import randint as rd
n = int(input("Введите количсетво элементов массива: "))
list1 = list()
for i in range(n):
    list1.append(rd(1, 100))
print(list1)
min = int(input("Введите минимальное значение диапазона: "))
max = int(input("Введите максимальное значение диапазона: "))
list2 = list()
for j in range(n):
    if list1[j] < max and list1[j] > min:
        list2.append(j)
if len(list2) > 0:
    print(list2)
else:
    print('Ни один элемент не принадлежит заданному диапазону')



