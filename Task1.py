a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность: "))
l = int(input("Введите количество элементов: "))
list1 = list()
n = 1
for i in range (l):
    list1.append(a1 + (n-1) * d)
    print(list1[i])
    n +=1


