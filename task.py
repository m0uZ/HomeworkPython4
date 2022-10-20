# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141   10^{-1} ≤ d ≤10^{-10}
# from math import pi

# d =  int(input("Введите число для заданной точности числа Пи: "))
# print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# number = int(input('Задайте натуральное число N: '))
# some_list = []
# divisor = 2
# while divisor <= number:
#     if number % divisor == 0:
#         some_list.append(divisor)
#         number = number // divisor
#     else:
#         divisor += 1
# print(some_list)

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# some_list = [2, 3, 4, 4, 7, 4, 6, 6, 2]
# set_list = []

# for i in some_list:
#     if i not in set_list:
#         set_list.append(i)
# print(set_list)

# Через set()
# # a = set(some_list)
# # print(a)

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# from random import randint
# import itertools

# k = 2
# ratios = [randint(1, 10) for i in range(k + 1)]

# f = ['*x**']*(k-1) + ['*x']
# polynomial = [[a, b, c] for a, b, c in itertools.zip_longest(ratios, f, range(k, 1, -1), fillvalue='')]
    
# for x in polynomial:
#     x.append(' + ')
# polynomial = list(itertools.chain(*polynomial))
# polynomial[-1] = ' = 0'
# polynom = "".join(map(str, polynomial)).replace(' 1*x', ' x')

# with open('polynomial.txt', 'w') as data:
#     data.write(polynom)

