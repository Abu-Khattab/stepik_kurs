''' функции без параметров'''

# ''' выводит звездный прямоугольник с размерами 14 × 10 '''

## объявление функции
# def draw_box():
#     for i in range(13):
#         if i > 0 and i < 13:
#             print('*        *')
#         if i == 0:
#             print('*' * 10)
#
#     else:
#         print('*' * 10)
# # основная программа
# draw_box()  # вызов функции
#
# ''' или '''
#
# # объявление функции
# def draw_box():
#     print("*" * 10)
#
#     for i in range(12):
#         print("*", "*", sep=" " * 8)
#
#     print("*" * 10)
#
#
# # основная программа
# draw_box()  # вызов функции


# ''' выводит звездный прямоугольный треугольник с катетами, равными 10 '''
#
# # объявление функции
# def draw_triangle():
#     for i in range(11):
#         print(i * '*')
#
# # основная программа
# draw_triangle()  # вызов функции


# ''' или '''
#
# # объявление функции
# def draw_triangle():
#     print(*['*' * i for i in range(1, 11)], sep='\n')
#
# # основная программа
# draw_triangle()  # вызов функции


# ''' функции с параметрами '''
#
#
# h = int(input())
# w = int(input())
# def draw_box(height, width):    # функция принимает два параметра
#     for i in range(height):
#         print('*' * width)
#
# draw_box(h, w)


# ''' Звездный треугольник '''
#
# # объявление функции
# def draw_triangle(fill, base):
#     for i in range(1, base // 2 + 2):
#         print(i * fill)
#     for j in range(base // 2, 0, -1):
#         print(j * fill)
#
# # считываем данные
# fill = input()
# base = int(input())
#
# # вызываем функцию
# draw_triangle(fill, base)
#
#
# ''' или '''
#
# # объявление функции
# def draw_triangle(fill, base):
#     for i in range(base // 2):
#         print(fill * (i + 1))
#
#     for j in range(base // 2, -1, -1):
#         print(fill * (j + 1))
#
#
# # считываем данные
# fill = input()
# base = int(input())
#
# # вызываем функцию
# draw_triangle(fill, base)


# ''' или '''
#
# # объявление функции
# def draw_triangle(fill, base):
#     for i in range(1, base + 1):
#         print(fill * min(i, base - i + 1))
#
# # считываем данные
# fill = input()
# base = int(input())
#
# # вызываем функцию
# draw_triangle(fill, base)



# ''' ФИО '''
#
# # объявление функции
# def print_fio(name, surname, patronymic):
#     lis = [name, surname, patronymic]
#     print(surname[0], name[0], patronymic[0], sep='')
#
# # считываем данные
# name, surname, patronymic = input().upper(), input().upper(), input().upper()
#
# # вызываем функцию
# print_fio(name, surname, patronymic)
#
#
# ''' или '''
#
# # объявление функции
# def print_fio(name, surname, patronymic):
#     full_name = (surname[0] + name[0] + patronymic[0]).upper()
#     print(full_name)
#
#
# # считываем данные
# name, surname, patronymic = input(), input(), input()
#
# # вызываем функцию
# print_fio(name, surname, patronymic)


# ''' или '''
#
# def print_fio(name, surname, patronymic):
#     print(f"{surname[0]}{name[0]}{patronymic[0]}".upper())
#
#
# name, surname, patronymic = input(), input(), input(),
# print_fio(name, surname, patronymic)



# ''' выводит на печать сумму его цифр '''
#
# # объявление функции
# def print_digit_sum(num):
#     s = [sum(int(i) for i in str(num))]
#     print(*s)
#
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print_digit_sum(n)
#
#
# ''' или '''
#
# # объявление функции
# def print_digit_sum(num):
#     digit_sum = 0
#     while num > 0:
#         digit_sum += num % 10
#         num //= 10
#
#     print(digit_sum)
#
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print_digit_sum(n)


