''' modul math '''

# ''' Евклидово расстояние '''
#
#
# x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
#
# p = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5
# print(p)


# ''' Площадь и длина '''
#
# from math import *
#
# r = float(input())
# s = pi * r ** 2
# c = 2 * pi * r
# print(s)
# print(c)

# ''' Средние значения '''
#
# a, b = float(input()), float(input())
#
# c = (a + b) / 2  # среднее арифметическое
# d = (a * b) ** 0.5 # среднее геометрическое
# e = (a * b) * 2 / (a + b) # среднее гармоническое
# f = (((а ** 2) + (b ** 2)) / 2) ** 0.5 # среднее квадратичное
#
# print(c, d, e, f, sep='\n')


# ''' Тригонометрическое выражение '''


# from math import *
#
# x = float(input())
# s = sin(radians(x)) + cos(radians(x)) + (tan(radians(x)) ** 2)
#
# print(s)


# ''' Пол и потолок '''
#
# from math import *
#
# n1 = float(input())
# print(ceil(n1) + floor(n1))


# ''' Квадратное уравнение '''


# from math import *
#
# a, b, c = float(input()), float(input()), float(input())
#
# d = pow(b, 2) - 4 * a * c
# if d > 0:
#     x1 = (-b + sqrt(d) / (2 * a))
#     x2 = (-b - sqrt(d) / (2 * a))
#     print(min(x1, x2))
#     print(max(x1, x2))
# elif d == 0:
#     print(-b / (2 * a))
# else:
#     print("Нет корней")


# ''' или так '''
#
# from math import *
#
# a = float(input())
# b = float(input())
# c = float(input())
# d = b**2-4*a*c
#
# if d < 0:
#     print('Нет корней')
# elif d == 0:
#     print(-b / (2*a))
# elif d > 0:
#     x1 = (-b - d ** 0.5) / (2*a)
#     x2 = (-b + d ** 0.5) / (2*a)
#     print(min(x1, x2))
#     print(max(x1, x2))



# ''' Правильный многоугольник '''
#
# from math import *
#
# n, a = int(input()), float(input())
# s = n * (a ** 2) / (4 * tan(pi / n))
# print(s)