# ДЛЯ 3 ЕГО УРОКА :Задайте список из вещественных чисел. Напишите программу,
#  которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# some_list = [input() for _ in range(int(input()))]
# a = [float('0.' + (i.split('.')[1])) for i in some_list if '.' in i]
# print(a)
# print(max(a) - min(a))

# Фибоначи к 3 уроку задача последняя
# k = int(input("Inset k: "))
#
# fibonacciList = [0]*(k*2+1)
# print(fibonacciList)
# fibonacciList[k] = 0
# fibonacciList[k+1] = 1
#
# for i in range(k+2, len(fibonacciList)):
#     fibonacciList[i] = fibonacciList[i-2]+fibonacciList[i-1]
#
# for i in range(k, -1, -1):
#     fibonacciList[i] = fibonacciList[i+2]-fibonacciList[i+1]
#
# print(fibonacciList)


# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

# n = input("enter numbers splitted by space: ")
# print(n)
# numbers = n.split(' ')
# print('max ', max(numbers))
# print('min ', min(numbers))


# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
    
#     1) с помощью математических формул нахождения корней квадратного уравнения
# a, b, c = int(input('a ')), int(input('b ')), int(input('c '))
# d = pow(b,2) - 4*a*c
# if d < 0:
#     print("корней нет")
# elif d == 0:
#     print(-b/2*a)
# else:
#     print((-b+pow(d,0.5))/2*a)
#     print((-b-pow(d,0.5))/2*a)

    
#     2) с помощью дополнительных библиотек Python
# from sympy import *
# a, b, c = int(input('a ')), int(input('b ')), int(input('c '))

# x = Symbol('x')
# d = solveset(a*x**2+b*x+c,x)
# print(d)

    
# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
